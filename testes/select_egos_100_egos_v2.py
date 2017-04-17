# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Avalia o conjunto de usuarios coletados e verifica quais atendem aos requisitos de ter pelo menos 02 duas.
##								ESSE SCRIPT VERIFICA E COMPLETA OS 100 EGOS
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		lists_file = []
		while f.tell() < tamanho:
			buffer = f.read(list_struct.size)
			lists = list_struct.unpack(buffer)
			lists_file.append(follower[0])
	return lists_file

######################################################################################################################################################################
#
# Obtem as listas já coletadas do ego
#
######################################################################################################################################################################
def get_lists(ego):
	egos_lists_ownership = []
	egos_lists_subscription = []
	eof = False
	with open(lists_ego, 'r') as lists_file:
		for line in lists_file:
			lists = json.loads(line)
			if ego == long(lists['user']):
				print "Ego encontrado! Localizando listas..."
				for list in lists['owner']:
					egos_lists_ownership.append(list['id'])
				for list in lists['subscriptions']:
					egos_lists_subscription.append(list['id'])
				eof = True				
	return egos_lists_ownership,egos_lists_subscription
	
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i										#controla a quantidade de egos a serrem selecionados
	global dictionary
	q = 0											#QTDE total de egos
	l = 0											#QTDE de erros
	
	for file in os.listdir(egos_friends_dir):
		if i < ego_limit:
			j = 0											#QTDE de listas - owner
			k = 0											#QTDE de listas - subs
			q+=1 
			ego = file.split(".dat")
			ego = long(ego[0])
			if not dictionary.has_key(ego):
				egos_lists_ownership,egos_lists_subscription = get_lists(ego)
				print ("Ego nº "+str(i)+": "+str(ego)+" - Lists Ownership: "+str(len(egos_lists_ownership)))
				print ("Ego nº "+str(i)+": "+str(ego)+" - Lists Subscription: "+str(len(egos_lists_subscription)))
				if egos_lists_ownership:
					for list in egos_lists_ownership:
						if os.path.isfile(lists_collected_dir+str(list)+".dat"):
							j+=1
				if egos_lists_subscription:
					for list in egos_lists_ownership:
						if os.path.isfile(lists_collected_dir+str(list)+".dat"):
							k+=1
				qtde_listas = j+k 
				print ("Quantidade de listas coletadas: "+str(qtde_listas))
				if  qtde_listas > 1:	
					try:
						shutil.copy(egos_friends_dir+file,egos_friends_dir_100_egos)
						dictionary[ego] = ego									# Insere o usuário coletado na tabela em memória
						i+=1
						print (str(q)+" - Ok! - Quantidade de listas: "+str(qtde_listas))
						print ("Arquivo copiado com sucesso!")
					except Exception as e:
						print (e)
				else:
					print ("Não atende!")
		
				print ("##############################################")
			
	print
	print ("QTDE de egos verificados: "+str(q))
			
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

ego_limit = 100
egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/bin/"
lists_ego = "/home/amaury/coleta/ego_lists_collected/data/201701300152_ego_lists_overview.json"

egos_friends_dir_100_egos = "/home/amaury/coleta/n1/egos_friends/100/bin/"

lists_collected_dir = "/home/amaury/coleta/lists_info/members_lists_collected/bin/"

formato = 'l'				################################################### Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(egos_friends_dir_100_egos):
	os.makedirs(egos_friends_dir_100_egos)	
if not os.path.exists(lists_ego_100_bin_ownership):
	os.makedirs(lists_ego_100_bin_ownership)
if not os.path.exists(lists_ego_100_bin_subscription):
	os.makedirs(lists_ego_100_bin_subscription)	
	
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados	
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(egos_friends_dir_100_egos):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")	
#Executa o método main
if __name__ == "__main__": main()