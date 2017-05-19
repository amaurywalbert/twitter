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
##		Status - Versão 5.1 - Coletar seguidores do Twitter
##						
##						5.1.1 - Usa tabela hash para consultar usuários já coletados
##						5.1.2 - Redução no tamanho da struct para melhorar armazenamento - Uso apenas de um valor Long para armazenar o id do amigo dentro do aquivo
##										Proposta visa eliminar problemas de reaproveitamento dos arquivos de usuários já coletados.
##										 Não há necessidade de um ponteiro indicando o arquivo. Dá pra fazer isso pelo próprio algoritmo.
##						5.1.3 - Evita o retorno de lista de amigos vazias
##						5.1.4 - Seleciona chave randomicamente para nova autenticação em caso de erro do Tweepy						
##
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
	print
	print("######################################################################")
	print ("Autenticando usando chave número: "+str(key)+"/"+str(key_limit))
	print("######################################################################\n")
	time.sleep(wait)
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
		followers_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			follower = user_struct.unpack(buffer)
			followers_file.append(follower[0])
	return followers_file
	
######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a lista de seguidores de um usuário específico 
#
######################################################################################################################################################################
def get_followers(user):												#Coleta dos seguidores de um usuário específico
	global key
	global dictionary
	global api
	global i
	
	try:
		followers_list = []
		for page in tweepy.Cursor(api.followers_ids,id=user,wait_on_rate_limit_notify=True,wait_on_rate_limit=True,count=5000).pages():
			for follower in page:
				followers_list.append(follower)
		return (followers_list)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))
			api = autentication(auths)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"followers_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:
				error = {'user':user,'reason': e.message,'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'user':user,'reason': str(e),'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
		try:
			if e.message[0]['code'] == 32 or e.message[0]['code'] == 215 or e.message[0]['code'] == 429 or e.message[0]['code'] == 401:
				key = random.randint(key_init,key_limit)
				api = autentication(auths)
			if e.message[0]['code'] == 34:									# Usuários não existentes
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".dat", "w+b") as f:		# Cria arquivo vazio	
					print ("Usuário inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1
		except Exception as e2:
			api = autentication(auths)
			print ("E2: "+str(e2))
		
		try:
			if e.message == 'Not authorized.': # Usuários não autorizados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".dat", "w+b") as f:		# Cria arquivo vazio
					print ("Usuário não autorizado. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1	
		except Exception as e3:
			print ("E3: "+str(e3))
######################################################################################################################################################################
#
# Obtem as seguidores dos amigos dos egos
#
######################################################################################################################################################################
def save_user(k,user): # j = número do ego que esta sendo coletado - k = numero do amigo do ego que esta sendo verificado - l = tamanho da lista de amigos do ego
	global i	# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de amigos do usuário
	
	followers_list = get_followers(user)
	if followers_list:	
		try:
			with open(data_dir+str(user)+".dat", "w+b") as f:	
				for follower in followers_list:
					f.write(user_struct.pack(follower))						# Grava os ids dos amigos no arquivo binário do usuário
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				i +=1
				print ("Seguidores do ego nº "+str(k)+": "+str(user)+" coletados com sucesso. Total coletados: "+str(i))
	
		except Exception as e:	
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(error_dir+"followers_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
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
	k = 0																	#Exibe o número ordinal do ego que está sendo usado para a coleta dos seguidores
	for file in os.listdir(egos_list):							# Verifica a lista de egos coletados e para cada um, busca os seguidores dos egos.
		k+=1 
		user = file.split(".dat")
		user = long(user[0])	
		if not dictionary.has_key(user):
			save_user(k,user)
	
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
auths = oauth_keys['auths_test']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

qtde_egos = 'full' #10,50,100,500,full

key_init = 0					################################################## Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		################################################## Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) #################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves

egos_list = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/" ### Arquivo contendo a lista dos usuários a serem buscados
data_dir = "/home/amaury/coleta/n9/egos_followers/"+str(qtde_egos)+"/bin/" ## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n9/egos_followers/"+str(qtde_egos)+"/error/" # Diretório para armazenamento dos arquivos de erro

formato = 'l'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
wait = 15
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)

###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(data_dir):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
#Autenticação
api = autentication(auths)

	
#Executa o método main
if __name__ == "__main__": main()