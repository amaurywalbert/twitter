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
##		Status - Versão 1 - verifica se os alters (autores de retweets) já foram coletados e copia os arquivos deles para o diretório correto
##									Esse processo é apenas para agilizar e organizar os diretórios de timeline já coletados.
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
	m = 0
	
	for file in os.listdir(egos_50_timeline):
		j+=1
		with open(timeline_collected_dir+file,'r') as timeline:
			for line in timeline:
				l+=1
				tweet = json.loads(line)
				try:
					user =  tweet['retweeted_status']['user']['id']
					user = long(user)
						try:
							if os.path.isfile(timeline_collected+str(user)+".json"):
							shutil.copy(timeline_collected+str(user)+".json",egos_50_timeline)
							print ("Arquivo copiado com sucesso!")
						except Exception as e:
							print (e)

				except KeyError:
					m+=1
					print "Não é retweet!"
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

timeline_collected = "/home/amaury/coleta_old/timeline_collect/10mil_egos/json/"
dst_timeline_collected = "/home/amaury/coleta/n2/timeline_collect/alters/50/bin/"




#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(dst_timeline_collected):
	os.makedirs(dst_timeline_collected)

#Executa o método main
if __name__ == "__main__": main()