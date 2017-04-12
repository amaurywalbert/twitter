# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Para cada um dos 50 egos coletados, verifica as informações das listas e cria arquivos binários para cada ego contendo o conjunto de listas
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
		followers_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			follower = user_struct.unpack(buffer)
			followers_file.append(follower[0])
	return followers_file

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
			lists = json.loads(user_lists)
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
	i = 0	
	j = 0											#QTDE total de egos
	k = 0											#QTDE de arquivos copiados
	l = 0											#QTDE de erros

	for file in os.listdir(egos_friends_dir):
		i+=1 
		ego = file.split(".dat")
		ego = long(ego[0])
		egos_lists_ownership,egos_lists_subscription = get_lists(ego)
		if egos_lists_ownership:
			try:
				with open(lists_ego_50_bin_ownership+str(ego)+".dat", "w+b") as f:	
					for list in egos_lists_ownership:		
						for member in list:
							f.write(list_struct.pack(member))						# Grava os ids dos amigos no arquivo binário do usuário	
					j+=1
					print ("##############################################")
					print ("Arquivo copiado com sucesso!")
					print ("##############################################")
			except Exception as e:
				l+=1
				print (e)
				
		if egos_lists_subscription:
			try:
				with open(lists_ego_50_bin_subscription+str(ego)+".dat", "w+b") as f:	
					for list in egos_lists_subscription:		
						for member in list:
							f.write(list_struct.pack(member))						# Grava os ids dos amigos no arquivo binário do usuário	
					k+=1
					print ("##############################################")
					print ("Arquivo copiado com sucesso!")
					print ("##############################################")
			except Exception as e:
				l+=1
				print (e)				
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

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/50/bin/"
lists_ego = "/home/amaury/coleta/ego_lists_collected/data/201701300152_ego_lists_overview.json"

lists_ego_50_bin_ownership = "/home/amaury/coleta/lists_info/egos_lists_collected/50/ownership/bin/"
lists_ego_50_bin_subscription = "/home/amaury/coleta/lists_info/egos_lists_collected/50/subscription/bin/"

collected_dir = "/home/amaury/coleta/lists_info/members_lists_collected/bin/"
collected_50_egos = "/home/amaury/coleta/lists_info/members_lists_collected/50/bin/"	

formato = 'l'				################################################### Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(collected_50_egos):
	os.makedirs(collected_50_egos)
if not os.path.exists(lists_ego_50_bin_ownership):
	os.makedirs(lists_ego_50_bin_ownership)
if not os.path.exists(lists_ego_50_bin_subscription):
	os.makedirs(lists_ego_50_bin_subscription)	
#Executa o método main
if __name__ == "__main__": main()