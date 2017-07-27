# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		28-07-2017
##		Status - Versão 1 - Recebe lista com 500 egos aleatórios e verifica quais deles extrapolam o número de 5mil alters.
##		Gera arquivo com o id do ego e o número de alters de cada um.
##						
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin_friends(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		friends_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_file.append(friend[0])
	return friends_file

################################################################################################
# Imprime os arquivos binários com os ids dos followers
################################################################################################
def read_arq_bin_followers(file):
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
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	with open(arq1, 'r') as f:
		file = json.load(f)
		for user in file:
			friends_list = read_arq_bin_friends(egos_n1+str(user)+".dat") 			#Verificando número de amigos
			followers_list = read_arq_bin_followers(egos_n9+str(user)+".dat")		#Verificando número de seguidores
			
			if len(friends_list) < 10:
				print ("User: "+str(user)+" - QTDE Friends: "+str(len(friends_list)))
			if len(followers_list) < 10:
				print ("User: "+str(user)+" - QTDE Followers: "+str(len(followers_list)))
					
######################################################################################################################################################################
	
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")


#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

arq1 = "/home/amaury/coleta/subconjunto/random_egos/k10/500.json"					#################### Arquivo com 500 egos aleatórios (de um total de 3980)
egos_over_5k = "/home/amaury/coleta/subconjunto/egos_over_5k/"	 					#################### Saída - Diretório contendo os egos aleatórios podados com k=10

egos_n1 = "/home/amaury/coleta/n1/egos_friends/full_with_prunned/bin/" 			#################### Diretório contendo todos os egos da rede n1
egos_n9 = "/home/amaury/coleta/n9/egos_followers/full_with_prunned/bin/" 		#################### Diretório contendo todos os egos da rede n9


#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(egos_over_5k):
	os.makedirs(egos_over_5k)

formato = 'l'				####################################################### Long para o código ('l') - id dos amigos de cada user
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Executa o método main
if __name__ == "__main__": main()