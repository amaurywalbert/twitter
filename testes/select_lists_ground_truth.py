# -*- coding: latin1 -*-
################################################################################################
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - faz a interseção dos diretórios com informações das listas para criar um diretório contendo as
##								 listas que tiveram todas as informações necessárias para o projeto.
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
	print ("Copiando arquivos...")
	for file in os.listdir(origin_members):
		if os.path.isfile(origin_subscribers+file):
			tam_members = os.path.getsize(origin_members+file)
			tam_subscribers = os.path.getsize(origin_subscribers+file)
			if tam_members != 0 or tam_subscribers != 0:
				try:

					shutil.copy(origin_members+file,dest_members)
					shutil.copy(origin_subscribers+file,dest_subscribers)

				except Exception as e:
					print (e)
		else:
			print ("Não está na interseção! Lista: "+str(file))
	print ("##############################################")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
origin_members = "/home/amaury/coleta_old/lists_info/members_lists_collected/bin/"
origin_subscribers = "/home/amaury/coleta_old/lists_info/subscribers_lists_collected/bin/"

dest_members = "/home/amaury/coleta/ground_truth/members_lists_collected/bin/"
dest_subscribers = "/home/amaury/coleta/ground_truth/subscribers_lists_collected/bin/"

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(dest_members):
	os.makedirs(dest_members)
	
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(dest_subscribers):
	os.makedirs(dest_subscribers)	

print("######################################################################\n")	
#Executa o método main
if __name__ == "__main__": main()