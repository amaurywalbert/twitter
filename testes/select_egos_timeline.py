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
			if os.path.isfile(origem1+str(user)+".json"):
				shutil.copy(origem1+str(user)+".json",destino)
				print ("Arquivo copiado com sucesso!")
			elif os.path.isfile(origem2+str(user)+".json"):
				shutil.copy(origem2+str(user)+".json",destino)
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
qtde_egos = 10 		#10, 50, 100, 500 ou full
######################################################################################################################

fonte = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"

origem1 = "/home/amaury/coleta_old_01/timeline_collect/full/json/"
origem2 = "/home/amaury/coleta_old_02/timeline_collect/full/json/"

destino = "/home/amaury/coleta/timeline_collect/"+str(qtde_egos)+"/json/"	

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(destino):
	os.makedirs(destino)

#Executa o método main
if __name__ == "__main__": main()