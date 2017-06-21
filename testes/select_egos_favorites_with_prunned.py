# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Para cada um dos 50 egos coletados, verifica na pasta dos favoritos coletados  (10.0000) e copia o arquivo para a pasta favorites/50/
##									Esse processo é apenas para agilizar e organizar os diretórios de favoritos já coletados.
## 
######################################################################################################################################################################

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	for file in os.listdir(fonte):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		user = file.split(".dat")
		user = long(user[0])
		try:
			if not os.path.isfile(destino+str(user)+".json"):
				if os.path.isfile(origem+str(user)+".json"):	
					shutil.copy(origem+str(user)+".json",destino)
					print ("Arquivo copiado com sucesso!")
				else:
					print ("Arquivo não encontrado...! "+str(user))
#			else:
#				print ("Arquivo já existe no destino...")
		except Exception as e:
			print (e)

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

fonte = "/home/amaury/coleta/n1/egos_friends_with_prunned/full/bin/"

origem = "/home/amaury/coleta_old/favorites_collect/ego/json/"
destino = "/home/amaury/coleta/favorites_collect/full_with_prunned/json/"	

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(destino):
	os.makedirs(destino)
	
#Executa o método main
if __name__ == "__main__": main()