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
	for file in os.listdir(egos_friends_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		user = file.split(".dat")
		user = long(user[0])
		try:
			if os.path.isfile(timeline_collected+str(user)+".json"):
				shutil.copy(timeline_collected+str(user)+".json",egos_50_timeline)
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

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/10/bin/"

timeline_collected = "/home/amaury/coleta/timeline_collect/50/json/"
egos_50_timeline = "/home/amaury/coleta/timeline_collect/10/json/"	


#Executa o método main
if __name__ == "__main__": main()