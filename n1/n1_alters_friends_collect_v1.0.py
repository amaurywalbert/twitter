# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de users do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, simplejson
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
##						STATUS - TESTE - Salvar arquivos JSON com informações dos amigos dos amigos do ego.  
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
	print
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
# Obtem as amigos de um usuário específico
#
################################################################################################

def get_friends(user):
	global api
	global count_overview
	
	print("Coletando amigos do usuário: "+str(user))	
	friends = []
	try:
		for page in tweepy.Cursor(api.friends_ids,id=user,wait_on_rate_limit_notify=True,count=5000).pages():
			for list in page:
				friends.append(list)
				
		friends_file = open(dir_data+"friends_data.json", 'a+')								# Arquivo com os dados dos amigos
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')		# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		friends_data = {user_id:long(user),user_friends:friends,'verified':agora}		# Usa informações inseridas no inicio do script (ego/alter) 
		friends_file.write(json.dumps(friends_data, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
		friends_file.close()
		print ("Amigos coletados com sucesso.")
		
		count_overview +=1
		try:
			if count_overview > count_limit:						#Salva as listas em blocos - evitar arquivos muito grandes.	
				agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
				shutil.move(dir_data+"friends_data.json", dir_data+agora+"_friends_data.json")
				count_overview = 0
		except Exception as e:
			print e
			
		users_verified = open(dir_data+"users_verified.txt",'a+')			#Arquivo para armazenar a lista de usuários já verificados.
		users_verified.writelines(str(user)+"\n")												# Salva o usuário no arquivo de users já verificados.
		users_verified.close()	

	except tweepy.RateLimitError as t:					# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando 02 segundos.\n")
		print
		time.sleep(2)		
		api = autentication(auths)
		get_friends(user)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		outfile = open(dir_error+"friends_err.json", "a+") # Abre o arquivo para gravação no final do arquivo
 
		if e.message:		
			error = {'user':user,'reason': e.message,'date':agora}
		else:
			error = {'user':user,'reason': str(e),'date':agora}
		outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
		outfile.close()
		print error
		
		users_verified = open(dir_data+"users_verified.txt",'a+')						#Arquivo para armazenar a lista de usuários já verificados.
		users_verified.writelines(str(user)+"\n")													# Salva o usuário no arquivo de users já verificados.
		users_verified.close()	
	
	
##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	users_verified = open(dir_data+"users_verified.txt",'a+')						#Arquivo para armazenar a lista de usuários já verificados.	
	tree = BSTNode(0)
	for line in users_verified:
		node = line
		tree.add(long(node))
	users_verified.close()

	i = 0
	
	users_list = open(users_list_file,'r')
	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		account = users_list.readline()														#Leia id do usuário corrente
		if (account == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
			eof = True		
		else:
			i += 1
			ego = json.loads(account)
			qtde_total = len(ego['ego_friends'])			
			qtde = len(ego['ego_friends'])			
			for user in ego['ego_friends']:
				print("#####################################################")
				if tree.get(long(user)):														#Consulta na árvore binária se o user já foi verificado.
					print ("Usuário: "+str(user)+" Já verificado. Continuando...")	
				else:		
					get_friends(user)																#Inicia função de busca
				qtde -=1
				print ("Faltam "+str(qtde)+"/"+str(qtde_total)+" amigos do ego nº: "+str(i)+" - chave número: "+str(key)+"/"+str(key_limit))
				print("#####################################################")
	users_list.close()	
	
	agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
	if os.path.exists(dir_data+"friends_data.json"):
		shutil.move(dir_data+"friends_data.json", dir_data+agora+"_friends_data.json")
	print	
	print("Coleta finalizada!")
	
################################################################################################
#
# INICIO DO PROGRAMA
#
#######################################################################################################################################################

################################### DEFINIR SE É TESTE OU NÃO!!! ###############################
################################################################################################									
oauth_keys = multi_oauth.keys()

auths = oauth_keys['auths_ok']
#USAGE  -- auths = oauth_keys['auths_ok']
#USAGE  -- auths = oauth_keys['auths_test']
################################################################################################
################################### CONFIGURAR AS LINHAS A SEGUIR #####################################################################################
################################################################################################
key = -1							##################################################################### Essas duas linhas atribuem as chaves para cada script
key_init = 0
key_limit = len(auths)		##################################################################### Usa todas as chaves

count_overview = 0			##################################################################### Controla o tamanho de cada arquivo
count_limit = 9999

dir_data = "/home/amaury/coleta/n1/alters/" ############################################### Diretório para armazenamento dos arquivos
dir_error = "/home/amaury/coleta/n1/alters/error/"

user_id = 'alter_id'				################################################################## Chaves para os registros: 'ego' ou 'alter'
user_friends = 'alter_friends'

users_list_file = "/home/amaury/coleta/n1/egos/friends_data_full.json" #################### Arquivo contendo a lista dos usuários a serem buscados


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
	
	
	
# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()	