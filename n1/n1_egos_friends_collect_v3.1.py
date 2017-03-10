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

######################################################################################################################################################################
##		Status - Versão 3.1 - Coletar amigos do Twitter
##						
##						3.1.1 - Usa tabela hash para consultar usuários já coletados
##						3.1.2 - Redução no tamanho da struct para melhorar armazenamento - Uso apenas de um valor Long para armazenar o id do amigo dentro do aquivo
##										Proposta visa eliminar problemas de reaproveitamento dos arquivos de usuários já coletados.
##										 Não há necessidade de um ponteiro indicando o arquivo. Dá pra fazer isso pelo próprio algoritmo. 					
##
##						STATUS - TESTE - Salvar arquivos binários contendo os ids dos amigos de cada usuário.
##
## 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Realiza autenticação da aplicação.
#
######################################################################################################################################################################

def autentication(auths):
	global key
	key += 1
	if (key >= key_limit):
		key = key_init
	print ("Autenticando usando chave número: "+str(key)+"/"+str(key_limit))
	api_key = tweepy.API(auths[key])
	return (api_key)

######################################################################################################################################################################
#
# Converte formato data para armazenar em formato JSON
#
######################################################################################################################################################################
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object

######################################################################################################################################################################
#
# Grava os arquivos binários com os ids dos amigos
#
######################################################################################################################################################################

#Gravando os dados
def grava(f,user,friends_file):
	f.write(user_struct.pack(user,friends_file))


######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a lista de amigos de um usuário específico 
#
######################################################################################################################################################################
def get_friends(user):												#Coleta dos amigos de um usuário específico
	global api																			# API - Tweepy - chave de autenticação usada
	try:
		friends_list = []
		for page in tweepy.Cursor(api.friends_ids,id=user,wait_on_rate_limit_notify=True,count=5000).pages():
			for friend in page:
				friends_list.append(friend)

	except tweepy.RateLimitError as t:											# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print("Erro: ",str(t),". Aguardando "+str(espera)+" segundos.\n")
		print
		time.sleep(espera)		
		api = autentication(auths)
		get_friends(user)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		with open(dir_error+"friends_err.json", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:		
				error = {'user':user,'reason': e.message,'date':agora}
			else:
				error = {'user':user,'reason': str(e),'date':agora}
			outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
		print error
	return (friends_list)
	
######################################################################################################################################################################
#
# Obtem as amigos do ego
#
######################################################################################################################################################################
def save_ego(i,user):

	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de amigos do usuário
	friends_list = get_friends(user)
	
	j = 1
	for friend in friends_list:
		friends_file = data_dir+str(friend)+".dat"
		
		with open(data_dir+str(user)+".dat", "a+b") as f_user:			#Salva o alter e seu endereço no arquivo do ego
			grava(f_user,long(friend),friends_file)
		dictionary = {long(alter):alter_friends_file}						#Salva o alter numa entrada da tabela em memória
		

	friends_file = dir_data+str(user)+".dat"			# Armazena no arquivo da lista de egos o ID do ego a localização do arquivo que contém a lista dos seus amigos (alters)			
	with open(data_dir_ego+"egos_file.dat", "a+b") as egos_file:
		grava(egos_file,user,friends_file)
	
	dictionary = {long(user):friends_file}										#Insere o usuário coletado na tabela em memória
	print ("Amigos do ego "+str(user)+" coletados com sucesso.")
	print

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	with open(users_list_file,'r') as users_list:						#Percorre o arquivo de usuários já verificados
		i = 1
		for k in range(0,ego_limit):
			user = users_list.readline()										#Leia id do usuário corrente
			dir = dictionary.get(long(user))								#Consulta na tabela se o usuário já foi verificado
			if dir:
				print ("Usuário "+str(user)+" já coletado! Continuando...")
				print	
			else:
				print("######################################################################")			
				save_ego(i, long(user))								#Inicia função de busca
				i+=1
				print("######################################################################")
	print("Coleta finalizada!")
	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### DEFINIR SE É TESTE OU NÃO!!! ### ['auths_ok'] OU  ['auths_test'] ################				
oauth_keys = multi_oauth.keys()
auths = oauth_keys['auths_ok']

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
key = -1							####################################### Essas duas linhas atribuem as chaves para cada script
key_init = 0					####################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		####################################### Usa todas as chaves (tamanho da lista de chaves)
data_dir = "/home/amaury/n1/bin/" ################################ Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/n1/error/" ############################### Diretório para armazenamento dos arquivos de erro
users_list_file = "/home/amaury/coleta/n1/egos/egos_list.txt" #### Arquivo contendo a lista dos usuários a serem buscados
ego_limit = 10						#################################### Controla a quantidade de egos a serem pesquisados
espera = 2						####################################### Tempo de espera antes de iniciar nova autenticação (segundos)
formato = 'l'				####################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ############################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
dictionary = {}				####################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)

#Autenticação
try:
	api = autentication(auths)
	print
	print("######################################################################")
	print
except tweepy.error.TweepError as e:
	print("[ERRRO] Não foi possível realizar autenticação. Erro: ",str(e),".\n")
	
	
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.

for file in os.listdir(data_dir):
	data = data_dir+file
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	
	dictionary[user_id] = data

#Executa o método main
if __name__ == "__main__": main()