# -*- coding: latin1 -*-
################################################################################################
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Avalia o conjunto de usuarios coletados e verifica quais atendem aos requisitos de ter pelo menos 02 listas com pelo menos 05 membros em cada.
##								ESSE SCRIPT VERIFICA APENAS OS 50 EGOS QUE JA'HAVIAM SIDO SELECIONADOS PELO PROTOTIPO MAS NAO TINHAMOS VERIFICADO A SITUAÇÃO DAS LISTAS
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
def get_lists(ego):	# Procura pelo usuário no arquivo das listas e retorna as listas separando as que ele é dono e as que está inscrito.
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
						shutil.copy(egos_friends_dir+file,egos_friends_dir_50_egos)
						dictionary[ego] = ego									# Insere o usuário coletado na tabela em memória
						i+=1
						print (str(q)+" - Ok!")
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

ego_limit = 50
egos_friends_dir = "/home/amaury/coleta_old/n1/egos_friends/50_old/bin/"
lists_ego = "/home/amaury/coleta/ego_lists_collected/data/ego_lists_overview_full.json"

egos_friends_dir_50_egos = "/home/amaury/coleta/n1/egos_friends/50/bin/"

lists_collected_dir = "/home/amaury/coleta/ground_truth/members_lists_collected/bin/" # Apenas pra pagar o id das listas - poderia ser tbm com os subscribers

formato = 'l'				################################################### Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(egos_friends_dir_50_egos):
	os.makedirs(egos_friends_dir_50_egos)
	
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados	
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(egos_friends_dir_50_egos):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")	
#Executa o método main
if __name__ == "__main__": main()