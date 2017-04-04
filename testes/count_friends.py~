# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Recebe lista de usuários e quantidade de egos e apresenta o somatório da quantidade total de seguidores.
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
		friends_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_file.append(friend[0])
	return friends_file


######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	alters_count = 0
	friends_total = 0
	followers_total = 0
	i = 0

	for file in os.listdir(egos_friends_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		user = file.split(".dat")
		user = long(user[0])
		alters_list = read_arq_bin(egos_friends_dir+file)
		l = len(alters_list)										# Exibe o tamanho/quantidade de amigos na lista de amigos do ego
		alters_count += l
		
		for alter in alters_list:
			if os.path.isfile(egos_friends_collected+str(alter)+".dat"):
				friends_total += 1
		
		for alter in alters_list:
			if os.path.isfile(egos_followers_collected+str(alter)+".dat"):
				followers_total += 1

		i +=1
		print ("Ego nº: "+str(i)+" - Qtde amigos: "+str(l))


	print ("Total de amigos dos amigos dos "+str(i)+" egos: "+str(alters_count))
	print ("Média de amigos por ego: "+str(alters_count/i))

	print ("Total de amigos dos amigos coletados: "+str(friends_total))
	print ("Ainda faltam ser coletados: "+str(alters_count-friends_total)+" amigos")

	print ("Total de seguidores dos amigos coletados: "+str(followers_total))
	print ("Ainda faltam ser coletados: "+str(alters_count-followers_total)+" seguidores")


######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/50/bin/"############### Arquivo contendo a lista dos usuários ego já coletados
egos_friends_collected = "/home/amaury/coleta/n1/egos_and_alters_friends/bin/"############### Arquivo contendo a lista dos usuários ego já coletados
egos_followers_collected = "/home/amaury/coleta/n5/alters_followers/bin"		############### Arquivo contendo a lista dos usuários ego já coletados
formato = 'l'									###################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato)					 ######################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Executa o método main
if __name__ == "__main__": main()