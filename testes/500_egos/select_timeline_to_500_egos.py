# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Para cada um dos 50 egos coletados, verifica na pasta dos timeline coletados  (10.0000) e copia o arquivo para a pasta timeline/50/
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
	i=0
	for file in os.listdir(egos_friends_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		user = file.split(".dat")
		user = long(user[0])
		try:
			if os.path.isfile(timeline_collected+str(user)+".json"):
				shutil.copy(timeline_collected+str(user)+".json",egos_50_timeline)
				i+=1
				print ("Arquivo copiado com sucesso! "+str(i))
		except Exception as e:
			print (e)

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/500/bin/"

timeline_collected = "/home/amaury/coleta_old/timeline_collect/10mil_egos/json/"
egos_50_timeline = "/home/amaury/coleta/timeline_collect/500/json/"	

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(egos_50_timeline):
	os.makedirs(egos_50_timeline)

#Executa o método main
if __name__ == "__main__": main()