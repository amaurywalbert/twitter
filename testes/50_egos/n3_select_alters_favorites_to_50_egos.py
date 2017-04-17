# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth_n2
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')


######################################################################################################################################################################
##		Status - Versão 1 - verifica se os alters (autores de tweets favoritados) já foram coletados e copia os arquivos deles para o diretório correto
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
	j = 0
	l = 0
	k = 0
	m = 0
	
	for file in os.listdir(egos_50_favorites):
		j+=1
		with open(egos_50_favorites+file,'r') as favorites:
			for line in favorites:
				l+=1
				
				tweet = json.loads(line)
				user =  tweet['user']['id']

				try:
					if os.path.isfile(favorites_collected+str(user)+".dat"):
						shutil.copy(favorites_collected+str(user)+".dat",dst_favorites_collected)
						print ("Arquivo copiado com sucesso!")
						k+=1
				except Exception as e:
					print (e)
	print
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")

#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

egos_50_favorites = "/home/amaury/coleta/favorites_collect/50/json/"

favorites_collected = "/home/amaury/coleta_old/favorites_collect/alters/bin/"
dst_favorites_collected = "/home/amaury/coleta/favorites_collect/alters/50/bin"


#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(dst_favorites_collected):
	os.makedirs(dst_favorites_collected)

#Executa o método main
if __name__ == "__main__": main()