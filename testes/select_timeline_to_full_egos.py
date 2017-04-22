# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Para cada um dos full egos, verifica na pasta dos favoritos coletados  (10.0000) e copia o arquivo para a pasta favorites/50/
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
	for file in os.listdir(egos_set):
		user = file.split(".dat")
		user = long(user[0])
		if not dictionary.has_key(user):
			print ("Usuário ainda não coletado. Verificando no diretório 'coleta_old'. Ego:"+str(user))
			try:
				if os.path.isfile(timeline_collected+str(user)+".json"):
					print ("Arquivo localizado...")
					shutil.copy(timeline_collected+str(user)+".json",egos_timeline)
					print ("Arquivo copiado com sucesso!\n")
					print("######################################################################")
				else:
					print ("Arquivo NÃO encontrado!!!\n")
					print("######################################################################")
			except Exception as e:
				print (e)

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

egos_set = "/home/amaury/coleta/n1/egos_friends/full/bin"

timeline_collected = "/home/amaury/coleta_old/timeline_collect/10mil_egos/json/"
egos_timeline = "/home/amaury/coleta/timeline_collect/full/json/"	


dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(egos_timeline):
	user_id = file.split(".json")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")

#Executa o método main
if __name__ == "__main__": main()