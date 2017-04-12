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
	q = 0											#controla a quantidade de egos a serrem selecionados
	i = 0											#QTDE total de egos
	j = 0											#QTDE de listas - owner
	k = 0											#QTDE de listas - subs
	l = 0											#QTDE de erros

	for file in os.listdir(egos_friends_dir_50_egos):	#Contando quantos egos já existem no diretório...
		q+=1
	
	while q < ego_limit:
		for file in os.listdir(egos_friends_dir):
			i+=1 
			ego = file.split(".dat")
			ego = long(ego[0])
			egos_lists_ownership,egos_lists_subscription = get_lists(ego)
			print ("Ego nº "+str(i)+": "+str(ego)+" - Lists Ownership ("+str(len(egos_lists_ownership))+"): "+str(egos_lists_ownership))
			print ("Ego nº "+str(i)+": "+str(ego)+" - Lists Subscription ("+str(len(egos_lists_subscription))+"): "+str(egos_lists_subscription))
			qtde_listas = len(egos_lists_ownership)+len(egos_lists_subscription) 
			if  qtde_listas > 1:	
				print (str(q)+" - Ok! - Quantidade de listas: "+str(qtde_listas))
				try:
					shutil.copy(egos_friends_dir+file,egos_friends_dir_50_egos)
					print ("Arquivo copiado com sucesso!")
				except Exception as e:
					print (e)
			else:
				print ("Não atende")
		
			print ("##############################################")
			
#		if egos_lists_ownership:
#			try:
#				with open(lists_ego_50_bin_ownership+str(ego)+".dat", "w+b") as f:	
#					for list in egos_lists_ownership:		
#						f.write(list_struct.pack(list))						# Grava os ids dos amigos no arquivo binário do usuário	
#					j+=1
#					print ("##############################################")
#					print ("Arquivo criado com sucesso!")
#					print ("##############################################")
#			except Exception as e:
#				l+=1
#				print (e)
#				
#		if egos_lists_subscription:
#			try:
#				with open(lists_ego_50_bin_subscription+str(ego)+".dat", "w+b") as f:	
#					for list in egos_lists_subscription:
#							f.write(list_struct.pack(list))						# Grava os ids dos amigos no arquivo binário do usuário	
#					k+=1
#					print ("##############################################")
#					print ("Arquivo criado com sucesso!")
#					print ("##############################################")
#			except Exception as e:
#				l+=1
#				print (e)				
	print
	print ("QTDE de egos verificados: "+str(i))
	print ("QTDE de arquivos gerados - owner: "+str(j))
	print ("QTDE de arquivos gerados - subs: "+str(k))
	print ("QTDE de erros: "+str(l))
			
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

ego_limit = 50
egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/50_old/bin/"
lists_ego = "/home/amaury/coleta/ego_lists_collected/data/201701300152_ego_lists_overview.json"

egos_friends_dir_50_egos = "/home/amaury/coleta/n1/egos_friends/50_egos_bin/"

lists_ego_50_bin_ownership = "/home/amaury/coleta/lists_info/egos_lists_collected/50/ownership/bin/"
lists_ego_50_bin_subscription = "/home/amaury/coleta/lists_info/egos_lists_collected/50/subscription/bin/"

formato = 'l'				################################################### Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(egos_friends_dir_50_egos):
	os.makedirs(egos_friends_dir_50_egos)	
if not os.path.exists(lists_ego_50_bin_ownership):
	os.makedirs(lists_ego_50_bin_ownership)
if not os.path.exists(lists_ego_50_bin_subscription):
	os.makedirs(lists_ego_50_bin_subscription)	
#Executa o método main
if __name__ == "__main__": main()