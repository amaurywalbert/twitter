# -*- coding: latin1 -*-
################################################################################################
#  Script para gerar os converter listas de amigos em formato JSON para arquivos binários individuais
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct	


reload(sys)
sys.setdefaultencoding('utf-8')

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
	
def read_arq_bin(f):
	f.seek(0,2)
	tamanho = f.tell()
	f.seek(0)
	friends_file = {}
	while f.tell() < tamanho:
		buffer = f.read(user_data.size)
		user, friends = user_data.unpack(buffer)
		friends = friends.split("\0")[0] # Como o C utiliza o \0 para terminar uma string no python precisamos tratar isso
		friends_file[user] = friends
	return friends_file

################################################################################################
# Grava os dados em Binário
################################################################################################

def save_bin_ego(user):
	if not os.path.exists(output_dir+str(user['ego_id'])+".dat"):
		with open(output_dir+str(user['ego_id'])+".dat", 'a+b') as f:
			 for friend in user['ego_friends']:
				friends_file = output_dir+str(friend)+".dat"
				f.write(user_data.pack(user['ego_id'],friends_file))
	else:
		print ("Arquivo já existe! User:"+str(user['ego_id']))
		
def save_bin_alter(user):
	if not os.path.exists(output_dir+str(user['alter_id'])+".dat"):
		with open(output_dir+str(user['alter_id'])+".dat", 'a+b') as f:
			 for friend in user['alter_friends']:
				friends_file = "boundarie"
				f.write(user_data.pack(user['alter_id'],friends_file))
	else:
		print ("Arquivo já existe! User:"+str(user['alter_id']))

################################################################################################
# Prepara os arquivos json
################################################################################################
def read_json_ego():	
	with open(egos_file,'r') as user_data:
		eof = False
		while not eof:
			user = user_data.readline()
			if user == "":
				eof = True
			else:
				user = json.loads(user)
				save_bin_ego(user)		

def read_json_alter():	
	with open(alters_file,'r') as user_data:
		eof = False
		while not eof:
			user = user_data.readline()
			if user == "":
				eof = True
			else:
				user = json.loads(user)
				save_bin_alter(user)		
################################################################################################
# Método Principal do Script
################################################################################################
def main():
	tt_i =  datetime.datetime.now()

	read_json_ego()
	read_json_alter()

	tt_f =  datetime.datetime.now()
	tt	= tt_f - tt_i
	print("Tempo total do script: "+str(tt))
	print("Script finalizado!")

################################################################################################
#
# INÍCIO DO PROGRAMA
#
################################################################################################

################################ CONFIGURAR AS LINHAS A SEGUIR #################################
################################################################################################
output_dir = "jsontobin/" 
egos_file = "/home/amaury/coleta/n1_10egos/json/egos/data/friends_data_full.json"
alters_file = "/home/amaury/coleta/n1_10egos/json/alters/data/friends_data_full.json"

users_list_file = "/home/amaury/coleta//n1/egos/egos_list.txt" #### Arquivo contendo a lista dos usuários a serem buscados
ego_limit = 10					####################################### Controla a quantidade de egos a serem pesquisados
formato = 'l50s'				####################################### Long para o código ('l') e depois o array de chars de X posições:	
user_data = struct.Struct(formato) ############################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
################################################################################################
################################################################################################
#Cria os diretórios para armazenamento das redes ego (grafos)
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

#Executa o método main
if __name__ == "__main__": main()