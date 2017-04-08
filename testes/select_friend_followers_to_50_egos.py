# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Para cada um dos 50 egos coletados, verifica na pasta dos seguidores dos amigos e copia o arquivo para a pasta alters_followers/50/
##									Esse processo é apenas para agilizar e organizar os diretórios de followers já coletados.
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
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	for file in os.listdir(egos_friends_dir):
		friends_list = read_arq_bin(egos_friends_dir+file)	# Lista de friends de um determinado ego
		print friends_list
		for user in friends_list:
			try:
				if os.path.isfile(followers_collected_dir+str(user)+".bin"):
					shutil.copy(followers_collected_dir+str(user)+".bin",followers_collected_50_egos)
					print ("Arquivo copiado com sucesso!")
			except Exception as e:
				print (e)

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/50/bin/"

followers_collected_dir = "/home/amaury/coleta/n5/alters_followers/bin/"### Diretório contendo o conjunto de amigos dos ego já coletados. Cada arquivo contém o conjunto de seguidores dos amigos.
followers_collected_50_egos = "/home/amaury/coleta/n5/alters_followers/50/bin/"	

formato = 'l'				################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(followers_collected_50_egos):
	os.makedirs(followers_collected_50_egos)
	
#Executa o método main
if __name__ == "__main__": main()