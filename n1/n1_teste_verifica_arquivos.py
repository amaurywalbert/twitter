# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de egos do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct
import multi_oauth
from BSTNode import BSTNode	
#Script que contém as chaves para autenticação do twitter e o outro é uma implementação de árvore para facilitar a busca

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1.0 - Teste para verificar os arquivos coletados 
## 
######################################################################################################################################################################


######################################################################################################################################################################
#
# Grava os arquivos binários com os ids dos amigos
#
######################################################################################################################################################################

#Gravando os dados
def grava(f,user,friends_file):
	f.write(user_data.pack(user,friends_file))
	#imprime(f)

def imprime(f):
	f.seek(0,2)
	tamanho = f.tell()
	f.seek(0)
	while f.tell() < tamanho:
		buffer = f.read(user_data.size)
		user, friends_file = user_data.unpack(buffer)
		print user, friends_file



######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	list = []
	with open(arquivo,'r') as f:
		for line in f:
			dict = json.loads(line) 
			if dict["ego_id"] == 1593586369:
				print len(dict["ego_friends"])


######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
arquivo = "/home/amaury/coleta/n1/egos/json/friends_data_full.json" 	# arquivo a ser verificado




  
#dir_data = "/home/amaury/coleta/n1/egos/bin/" #################### Diretório para armazenamento dos arquivos
#dir_error = "/home/amaury/coleta/n1/egos/bin/error/" ############# Diretório para armazenamento dos arquivos de erro
#users_list_file = "/home/amaury/coleta/n1/egos/egos_list.txt" #### Arquivo contendo a lista dos usuários a serem buscados
#formato = 'l150s'				####################################### Long para o código ('l') e depois o array de chars de X posições:	
#user_data = struct.Struct(formato) ############################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
#dictionary = {}				####################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
######################################################################################################################
######################################################################################################################

###### Iniciando dicionário - tabela hash a partir dos usuários já coletados
#with open(dir_data+"users_verified.txt",'a+') as users_verified:	
#	for line in users_verified:
#		line = long(line)
#		data = dir_data+str(line)+".dat"
#		dictionary[line] = data
#
#Executa o método main
if __name__ == "__main__": main()	