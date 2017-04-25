# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth_n4
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
	
	for file in os.listdir(egos_50_timeline):
		j+=1
		with open(egos_50_timeline+file,'r') as timeline:
			for line in timeline:
				l+=1
				tweet = json.loads(line)
				try:
					for item in tweet['entities']['user_mentions']:						 					
						user =  item['id']
						try:
							if os.path.isfile(mentions_collected+str(user)+".dat"):
								shutil.copy(mentions_collected+str(user)+".dat",dst_mentions_collected)
								print ("Arquivo copiado com sucesso!")
								k+=1
						except Exception as e:
							print (e)

				except KeyError:
					m+=1
					print "Não há menções!"
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

egos_50_timeline = "/home/amaury/coleta/timeline_collect/50/json/"

mentions_collected = "/home/amaury/coleta_old/n4/timeline_collect/alters/bin/"
dst_mentions_collected = "/home/amaury/coleta/n4/mentions_collect/alters/50/bin/"


#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(dst_mentions_collected):
	os.makedirs(dst_mentions_collected)

#Executa o método main
if __name__ == "__main__": main()