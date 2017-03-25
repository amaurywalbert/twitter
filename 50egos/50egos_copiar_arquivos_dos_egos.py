# -*- coding: latin1 -*-
################################################################################################
# Script para copiar 50 egos para o diretório: /home/amaury/coleta/n1/egos_friends/50/bin
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Copiar 50 egos para o diretório do primeiro teste de criação das redes
##	
## 
######################################################################################################################################################################

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	i = 0
	with open(egos_lists, 'r') as file:
		while i < ego_limit:
			user = file.readline()
			user_id = user.split("\n")
			user_id = str(user_id[0])
			try:
				origem = str(egos_friends_dir+user_id+".dat")
				destino = str(data_dir+user_id+".dat")
				print origem
				print destino
				print i
				shutil.copy2(origem, destino)
				i +=1
			except Exception as e:
				print e

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
######################################################################################################################
ego_limit = 50
egos_lists = "/home/amaury/coleta/n1/egos_friends/egos_list.txt"####### Arquivo contendo a lista de egos da primeira coleta
egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/bin/"########## Diretório dos usuários ego já coletados
data_dir = "/home/amaury/coleta/n1/egos_friends/50/bin/" ############## Diretório para armazenamento dos arquivos
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)

#Executa o método main
if __name__ == "__main__": main()