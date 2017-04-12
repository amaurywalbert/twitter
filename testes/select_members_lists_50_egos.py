# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Para cada um dos 50 egos coletados, verifica na pasta dos amigos dos amigos e copia o arquivo para a pasta alters_friends/50/
##									Esse processo é apenas para agilizar e organizar os diretórios de friends já coletados.
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
	j = 0											#QTDE total de egos
	k = 0											#QTDE de arquivos copiados
	l = 0											#QTDE de erros
	for file in os.listdir(egos_friends_dir):
		j+=1
		try:
			if os.path.isfile(collected_dir+str(file)):
				shutil.copy(collected_dir+str(file),collected_50_egos)
				k+=1
				print ("Arquivo copiado com sucesso!")
		except Exception as e:
			l+=1
			print (e)
	print
	print ("QTDE de egos verificados: "+str(j))
	print ("QTDE de arquivos copiados: "+str(k))
	print ("QTDE de erros: "+str(l))
			

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/50/bin/"

collected_dir = "/home/amaury/coleta/lists_info/members_lists_collected/bin/"
collected_50_egos = "/home/amaury/coleta/lists_info/members_lists_collected/50/bin/"	

formato = 'l'				################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(collected_50_egos):
	os.makedirs(collected_50_egos)
	
#Executa o método main
if __name__ == "__main__": main()