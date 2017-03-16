# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de egos do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 2.0 - # Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
##							2.1 - Autenticação volta a ser pelo Tweepy
##							
##						OBS - Copiar todos os arquivos dos egos para a pasta "data_dir", o script verifica se já existe o arquivo neste diretório evitando assim que haja recoleta de dados...						
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
	time.sleep(espera)
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


################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		friends_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_file.append(friend[0])
	return friends_file
######################################################################################################################################################################
#
# Verifica status da autenticação - Limites disponíveis
#
######################################################################################################################################################################
def get_api_limits():
	global api
	global key
	# Pode ser que o programa ja inicie com o limite de requisicoes estourado.
	rate_limit_available = False
	
	while not rate_limit_available:
		try:
			rate_limit = api.rate_limit_status()
			rate_limit_available = True
			friends_remaining = int(rate_limit['resources']['friends']['/friends/ids']['remaining'])
			rate_limit_remaining = int(rate_limit['resources']['application']['/application/rate_limit_status']['remaining'])
	
			print("friends_remaining = " +str(friends_remaining) + " - rate_limit_remaining = " + str(rate_limit_remaining))
			return {'friends_remaining': friends_remaining,'rate_limit_remaining': rate_limit_remaining}
		
		except tweepy.error.RateLimitError as e:
			print("Limite para verificar os limites da API atingido. Autenticando novamente... "+str(e))
			key = random.randint(key_init,key_limit)
			api = autentication(auths)

		except tweepy.error.TweepError as e:
			print("Erro oa verificar os limites da API. Erro: "+str(e)+" . Autenticando novamente...")
			if e.message:			
				if e.message[0]:
					if e.message[0]['code']:
						if e.message[0]['code'] == 32 or e.message[0]['code'] == 215:
							key = random.randint(key_init,key_limit)
			api = autentication(auths)
	
######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a lista de amigos de um usuário específico 
#
######################################################################################################################################################################
def get_friends(user):												#Coleta dos amigos de um usuário específico
	global key
	global dictionary
	global api

	limits = get_api_limits()

	while(limits['friends_remaining'] = 0 or limits['rate_limit_remaining'] = 0):
		print("Limite de acesso à API excedido.")
		limits = get_api_limits()
		
	try:
		friends_list = []
		for page in tweepy.Cursor(api.friends_ids,id=user,wait_on_rate_limit_notify=True,count=5000).pages():
			for friend in page:
				friends_list.append(friend)
		return (friends_list)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"friends_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:
				error = {'user':user,'reason': e.message,'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'user':user,'reason': str(e),'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error			

		if error['reason'] == 'Not authorized.' or error['reason'][0]['code'] == 34: # Usuários não autorizados ou não existentes
			dictionary[user] = user											# Insere o usuário coletado na tabela em memória
			with open(data_dir+str(user)+".dat", "w+b") as f:		#Cria arquivo vazio	
				print
	
######################################################################################################################################################################
#
# Obtem as amigos do ego
#
######################################################################################################################################################################
def save_user(j,k,l,user): # j = número do ego que esta sendo coletado - k = numero do alter que esta sendo verificado - l = tamanho da lista de amigos do ego
	global i	# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de amigos do usuário
	
#	try:
	friends_list = get_friends(user)
	if friends_list:
		with open(data_dir+str(user)+".dat", "w+b") as f:	
			for friend in friends_list:
				f.write(user_struct.pack(friend))						# Grava os ids dos amigos no arquivo binário do usuário
			dictionary[user] = user											# Insere o usuário coletado na tabela em memória
			i +=1
			print ("Ego nº "+str(j)+" - Alter ("+str(k)+"/"+str(l)+"): "+str(user)+" coletados com sucesso. Total coletados: "+str(i))
	
#	except Exception as e:	
#		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
#		with open(error_dir+"friends_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
#			if e.message:		
#				error = {'user':user,'reason': e.message,'date':agora}
#			else:
#				error = {'user':user,'reason': str(e),'date':agora}
#			outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
#			print error
#		if os.path.exists(data_dir+str(user)+".dat"):
#			os.remove(data_dir+str(user)+".dat")


######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	j = 0																	#Exibe o número ordinal do ego que está sendo usado para a coleta dos amigos dos alters
	k = 0																	#Exibe o número ordinal do alter que está sendo coletado a lista de amigos
	for file in os.listdir(egos_friends_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		j+=1 
		alter = file.split(".dat")
		alter = long(alter[0])
		friends_list = read_arq_bin(egos_friends_dir+file)
		l = len(friends_list)										# Exibe o tamanho/quantidade de amigos na lista de amigos do ego
		for friend in friends_list:
			k+=1
			if dictionary.has_key(friend):
				print ("Ego nº "+str(j)+" - Alter ("+str(k)+"/"+str(l)+"): "+str(friend)+" já coletado! Continuando...")
			else:
				save_user(j,k,l,friend)							#Inicia função de busca
				
	with open("/home/amaury/coleta/n1/egos_and_alters_friends/alters_collected.txt", 'w') as f:	
		for file in os.listdir(data_dir):					#As próximas linhas são usadas para imprimir o conteúdo dos arquivos, possibilitando a verificação de inconsistências.
			user_id = file.split(".dat")
			user_id = long(user_id[0])
			friends_file = read_arq_bin(data_dir+file)
			qtde_friends = len(friends_file)
			friendship = {'alter':user_id,'friends': qtde_friends}
			f.write(json.dumps(friendship, separators=(',', ':'))+"\n")
	
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################")

	
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

key_init = 0					#################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		#################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ###################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves
egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/bin/"# Arquivo contendo a lista dos usuários já coletados
data_dir = "/home/amaury/coleta/n1/egos_and_alters_friends/bin/" ############## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n1/egos_and_alters_friends/error/" ########### Diretório para armazenamento dos arquivos de erro
formato = 'l'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
espera = 15
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
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
i = 0
for file in os.listdir(data_dir):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
	
#Executa o método main
if __name__ == "__main__": main()