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
	count = 0
	friends_count = 0
	i = 0
	for file in os.listdir(egos_friends_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		alter = file.split(".dat")
		alter = long(alter[0])
		friends_list = read_arq_bin(egos_friends_dir+file)
		l = len(friends_list)										# Exibe o tamanho/quantidade de amigos na lista de amigos do ego
		for friend in friends_list:
			friends_count += l
			if os.path.isfile(egos_friends_collected+str(friend)+".dat")
			count += 1
		i +=1
		print ("Ego nº: "+str(i)+" - Qtde amigos: "+str(l))
	print ("Total de amigos coletados: "+str(count))
	print ("Total de amigos dos "+str(i)+" egos: "+str(friends_count))
	print ("Média de amigos por ego: "+str(friends_count/i))


######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/50/bin/"############### Arquivo contendo a lista dos usuários ego já coletados
egos_friends_collected = "/home/amaury/coleta/n1/egos_and_alters_friends/bin/"############### Arquivo contendo a lista dos usuários ego já coletados
formato = 'l'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Executa o método main
if __name__ == "__main__": main()