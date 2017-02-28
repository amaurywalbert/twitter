# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de egos do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct
import multi_oauth
from BSTNode import BSTNode	
#Script que contém as chaves para autenticação do twitter e o outro é uma implementação de árvore para facilitar a busca

reload(sys)
sys.setdefaultencoding('utf-8')

################################################################################################
##		Status - Versão 1.0 - Coletar amigos do Twitter
##						
##						1.0.1 - Usa árvore de busca para consultar usuários já verificados
##
##						STATUS - TESTE - Salvar arquivos binários com ponteiros indicando arquivos com os amigos de cada alter.  
##
## 
################################################################################################

################################################################################################
#
# Realiza autenticação da aplicação.
#
################################################################################################

def autentication(auths):
	global key
	key += 1
	if (key >= key_limit):
		key = key_init
	print ("Autenticando usando chave número: "+str(key)+"/"+str(key_limit))
	api_key = tweepy.API(auths[key])
	return (api_key)

################################################################################################
#
# Converte formato data para armazenar em formato JSON
#
################################################################################################
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object

################################################################################################
#
# Grava os arquivos binários com os ids dos amigos
#
################################################################################################

#Gravando os dados
def grava(f,user,friends_file):
	f.write(user_data.pack(user,friends_file))
	#imprime(f)

def imprime(f):
	f.seek(0,2)
	tamanho = f.tell()
	f.seek(0)
	while f.tell() < tamanho:
		buffer = f.read(user_data.size)
		user, friends_file = user_data.unpack(buffer)
		print user, friends_file

################################################################################################
#
# Grava os alters e busca seus amigos 
#
################################################################################################
def get_alters(f_ego,user):
	global api
	global dictionary
	dir = dictionary.get(long(user))
	if dir:
		grava(f_ego,long(user),dir)
		print ("Usuário "+str(user)+" já verificado! Continuando...")
		
	else:
		print("Coletando amigos do alter: "+str(user))				
		with open(dir_data+str(user)+".dat", "a+b") as f:
			alter_friends_file = dir_data+str(user)+".dat"
			try:
				for page in tweepy.Cursor(api.friends_ids,id=user,wait_on_rate_limit_notify=True,count=5000).pages():
					for friend in page:
						grava(f,friend,alter_friends_file)
					
				grava(f_ego,long(user),alter_friends_file)
				dictionary = {long(user):alter_friends_file}

				with open(dir_data+"users_verified.txt",'a+') as users_verified:
					users_verified.writelines(str(user)+"\n")	

			except tweepy.RateLimitError as t:											# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
				print("Erro: ",str(t),". Aguardando 02 segundos.\n")
				print
				time.sleep(2)		
				api = autentication(auths)
				get_alters(f_ego,user)

			except tweepy.error.TweepError as e:
				agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
				with open(dir_error+"friends_err.json", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
 					if e.message:		
						error = {'user':user,'reason': e.message,'date':agora}
					else:
						error = {'user':user,'reason': str(e),'date':agora}
					outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
			
				with open(dir_data+"users_verified.txt",'a+') as users_verified:						#Arquivo para armazenar a lista de usuários já verificados.
					users_verified.writelines(str(user)+"\n")														# Salva o usuário no arquivo de users já verificados.		
################################################################################################
#
# Obtem as amigos do ego
#
################################################################################################
def get_ego_friends(user):
	global api
	
	print("Coletando amigos do ego: "+str(user))	
	
	with open(dir_data+str(user)+".dat", "a+b") as f:
		try:
			for page in tweepy.Cursor(api.friends_ids,id=user,wait_on_rate_limit_notify=True,count=5000).pages():
				for friend in page:
					get_alters(f,friend)
					

			friends_file = dir_data+str(user)+".dat"			
			with open(dir_data+"egos_file.dat", "a+b") as egos_file:
				grava(egos_file,user,friends_file)
			
			print ("Amigos do ego "+str(user)+" coletados com sucesso.")
			print
			
			with open(dir_data+"users_verified.txt",'a+') as users_verified:		#Arquivo para armazenar a lista de usuários já verificados.
				users_verified.writelines(str(user)+"\n")										# Salva o usuário no arquivo de users já verificados.

		except tweepy.RateLimitError as t:											# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
			print("Erro: ",str(t),". Aguardando 02 segundos.\n")
			print
			time.sleep(2)		
			api = autentication(auths)
			get_ego_friends(user)

		except tweepy.error.TweepError as e:
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(dir_error+"friends_err.json", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
 				if e.message:		
					error = {'user':user,'reason': e.message,'date':agora}
				else:
					error = {'user':user,'reason': str(e),'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
			print error
		
			with open(dir_data+"users_verified.txt",'a+') as users_verified:						#Arquivo para armazenar a lista de usuários já verificados.
				users_verified.writelines(str(user)+"\n")														# Salva o usuário no arquivo de users já verificados.	
	
	
##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	with open(users_list_file,'r') as users_list:	
		for i in range(0,ego_limit):
			user = users_list.readline()														#Leia id do usuário corrente
			if (user == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
				eof = True		
			else:
				
				dir = dictionary.get(long(user))
				if dir:
					print ("Usuário "+str(user)+" já verificado! Continuando...")
					print	
				else:
					print
					print("####################################################################################################")			
					get_ego_friends(long(user))												#Inicia função de busca
					print("####################################################################################################")
	print("Coleta finalizada!")
	
################################################################################################
#
# INICIO DO PROGRAMA
#
#######################################################################################################################################################

################################### DEFINIR SE É TESTE OU NÃO!!! ###############################									
oauth_keys = multi_oauth.keys()
auths = oauth_keys['auths_ok']

################################### CONFIGURAR AS LINHAS A SEGUIR #####################################################################################
################################################################################################
key = -1							##################################################################### Essas duas linhas atribuem as chaves para cada script
key_init = 0
key_limit = len(auths)		##################################################################### Usa todas as chaves

dir_data = "/home/amaury/coleta/n1/egos/bin/" ###################################################### Diretório para armazenamento dos arquivos
dir_error = "/home/amaury/coleta/n1/egos/bin/error/"

users_list_file = "/home/amaury/coleta/n1/egos/egos_list.txt" ####################################### Arquivo contendo a lista dos usuários a serem buscados

ego_limit = 10				######################################################################## Controla a quantidade de egos a serem pesquisados

#Long para o código ('l') e depois o array de chars de X posições:
formato = 'l150s'
user_data = struct.Struct(formato)

dictionary = {}
#######################################################################################################################################################
#######################################################################################################################################################

if not os.path.exists(dir_data):
	os.makedirs(dir_data)

if not os.path.exists(dir_error):
	os.makedirs(dir_error)

try:
	api = autentication(auths)
	print
	print("####################################################################################################")
	print
except tweepy.error.TweepError as e:
	print("[ERRRO] Não foi possível realizar autenticação. Erro: ",str(e),".\n")
	
	
###### Iniciando tabela
with open(dir_data+"users_verified.txt",'a+') as users_verified:	
	for line in users_verified:
		line = long(line)
		data = dir_data+str(line)+".dat"
		dictionary[line] = data

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()	