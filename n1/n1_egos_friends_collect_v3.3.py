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
##		Status - Versão 3.1 - Coletar amigos do Twitter
##						
##						3.1.1 - Usa tabela hash para consultar usuários já coletados
##						3.1.2 - Redução no tamanho da struct para melhorar armazenamento - Uso apenas de um valor Long para armazenar o id do amigo dentro do aquivo
##										Proposta visa eliminar problemas de reaproveitamento dos arquivos de usuários já coletados.
##										 Não há necessidade de um ponteiro indicando o arquivo. Dá pra fazer isso pelo próprio algoritmo.
##						3.1.3 - Evita o retorno de lista de amigos vazias
##						3.1.4 - Seleciona chave randomicamente para nova autenticação em caso de erro do Tweepy						
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
def get_api_limits(user):
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
			print("Limite para verificar os limites da API atingido. Autenticando novamente...")
			key = random.randint(key_init,key_limit)
			api = autentication(auths)

		except tweepy.error.TweepError as e:
			print e
			if e.message:			
				if e.message[0].has_key('code'):
					if e.message[0]['code'] == 32 or e.message[0]['code'] == 215:
						key = random.randint(key_init,key_limit)
						api = autentication(auths)
	
######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a lista de amigos de um usuário específico 
#
######################################################################################################################################################################
def get_friends(user):												#Coleta dos amigos de um usuário específico
	global api
	global dictionary
	
	limits = get_api_limits(user)
	while(limits['friends_remaining'] == 0 or limits['rate_limit_remaining'] == 0):
		print("Limite de acesso à API excedido.")
		api = autentication(auths)
		limits = get_api_limits(user)
		
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
		if error['reason'] == 'Not authorized.':
			dictionary = {user:user}											# Insere o usuário coletado na tabela em memória
	
######################################################################################################################################################################
#
# Obtem as amigos do ego
#
######################################################################################################################################################################
def save_user(i,user):

	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de amigos do usuário
	
	try:
		friends_list = get_friends(user)
		if friends_list:
			with open(data_dir+str(user)+".dat", "a+b") as f:	
				for friend in friends_list:
					f.write(user_struct.pack(friend))						# Grava os ids dos amigos no arquivo binário do usuário
			dictionary = {user:user}											# Insere o usuário coletado na tabela em memória
			print ("Amigos do ego nº "+str(i)+": "+str(user)+" coletados com sucesso.")
	
	except Exception as e:	
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		with open(error_dir+"friends_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:		
				error = {'user':user,'reason': e.message,'date':agora}
			else:
				error = {'user':user,'reason': str(e),'date':agora}
			outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
			print error
		if os.path.exists(data_dir+str(user)+".dat"):
			os.remove(data_dir+str(user)+".dat")


######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i
	with open(users_list_file,'r') as users_list:						#Percorre o arquivo de usuários já verificados
		for k in range(0,ego_limit):
			user = users_list.readline()										#Leia id do usuário corrente
			user = long(user)
			if dictionary.has_key(user):
				print ("Usuário "+str(user)+" já coletado! Continuando...")
			else:
				save_user(i, user)							#Inicia função de busca
				i+=1
#	for file in os.listdir(data_dir):					#As próximas linhas são usadas para imprimir o conteúdo dos arquivos, possibilitando a verificação de inconsistências.
#		user_id = file.split(".dat")
#		user_id = long(user_id[0])
#		friends_file = read_arq_bin(data_dir+file)
#		print ("User: "+str(user_id)+" - Friends: "+str(friends_file))
	
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

key_init = 0					############################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		############################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ################################# Inicia o script a partir de uma chave aleatória do conjunto de chaves
data_dir = "/home/amaury/coleta/n1/egos_friends/bin/" #################### Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n1/egos_friends/error/" ################# Diretório para armazenamento dos arquivos de erro
users_list_file = "/home/amaury/coleta/n1/egos_friends/egos_list.txt" #### Arquivo contendo a lista dos usuários a serem buscados
ego_limit = 10000						######################################### Controla a quantidade de egos a serem pesquisados
espera = 2						############################################### Tempo de espera antes de iniciar nova autenticação (segundos)
formato = 'l'				################################################## Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ##################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
dictionary = {}				############################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
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