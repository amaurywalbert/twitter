# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth_n6
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 5.0 - Coletar timeline dos alters (seguidroes dos amigos dos egos) - Timeline dos Alters - identificar conjunto de retweeets da timeline.
##
##						
##						5.1 - Uso do Tweepy para controlar as autenticações...
##
##				
##						SALVAR APENAS O NECESSÁRIO PARA ECONOMIZAR ESPAÇO EM DISCO. Coletar tweets completos ocupa muito espaço.
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos BINÀRIOS!! contendo o id do retweet e id do autor a partir da lista de alters dos egos.
##
##						STATUS - Refazer a coleta até que não tenha nenhuma mensagem de "Rate Limit Exceeded"  - A cada mensagem há um usuário que ficou sem ser coletada
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
		retweets_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)
			status = {'retweet':retweet, 'user':user}
			retweets_list.append(status)
	return retweets_list

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_followers_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		followers_file = []
		while f.tell() < tamanho:
			buffer = f.read(followers_struct.size)
			follower = followers_struct.unpack(buffer)
			followers_file.append(follower[0])
	return followers_file

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a timeline de um usuário específico 
#
######################################################################################################################################################################
def get_timeline(user):												#Coleta da timeline
	global key
	global dictionary
	global api
	global i
	timeline = []
	try:
		for page in tweepy.Cursor(api.user_timeline,id=user, count=200).pages(16):				#Retorna os últimos 3200 tweets (16*20)
			for tweet in page:
				timeline.append(tweet)
		return (timeline)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))
			api = autentication(auths)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"timeline_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:
				error = {'user':user,'reason': e.message,'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'user':user,'reason': str(e),'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
		try:
			if e.message[0]['code'] == 32 or e.message[0]['code'] == 215:
				key = random.randint(key_init,key_limit)
				api = autentication(auths)
			if e.message[0]['code'] == 34:									# Usuários não existentes
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio	
					print ("Usuário inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1
		except Exception as e2:
			print ("E2: "+str(e2))
		
		try:
			if e.message == 'Not authorized.': # Usuários não autorizados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio
					print ("Usuário não autorizada. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1	
		except Exception as e3:
			print ("E3: "+str(e3))	
######################################################################################################################################################################
#
# Obtem timeline dos usuários
#
######################################################################################################################################################################
def save_timeline(j,k,l,user):
	global i	# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de tweets do usuário
	t = 0 																# Número de Tweets por usuário
	timeline = get_timeline(user)
	if timeline:	
		try:
			with open(data_dir+str(user)+".dat", "w+b") as f:
				for status in timeline:
					if hasattr(status, 'retweeted_status'):
						t+=1
						f.write(timeline_struct.pack(status.retweeted_status.id, status.retweeted_status.user.id))						# Grava os ids dos retweet  e o id do autor no arquivo binário do usuário
###
#			retweets_list = read_arq_bin(data_dir+str(user)+".dat") # Função para converter o binário de volta em string em formato json.
#			print retweets_list
####				
			dictionary[user] = user									# Insere o usuário coletado na tabela em memória
			i +=1
			print ("Egos_Friend nº: "+str(j)+" - Alter("+str(k)+"/"+str(l)+"): "+str(user)+" coletado com sucesso. "+str(t)+" retweets. Total de usuários coletados: "+str(i))
	
		except Exception as e:	
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(error_dir+"timeline_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
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
# Realiza teste e coleta dos favoritos do user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i 													# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	j = 0															# Exibe o número ordinal do friend que está sendo usado para a coleta da timeline
	k = 0															# Exibe o número ordinal do alter(follower) que está sendo usado para a coleta da timeline
	
	for file in os.listdir(followers_collected_dir):	# Verifica no diretorio.
		j+=1
		followers_list = read_arq_followers_bin(followers_collected_dir+file)	# Lista de alters (friends) de um determinado ego
		l = len(followers_list)									# Exibe o tamanho/quantidade de seguidores do amigo do ego
		for follower in followers_list:
			k+=1
			if not dictionary.has_key(follower):
				save_timeline(j,k,l,follower)							#Inicia função de busca
	print
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### DEFINIR SE É TESTE OU NÃO!!! ### ['auths_ok'] OU  ['auths_test'] ################				
oauth_keys = multi_oauth_n6.keys()
auths = oauth_keys['auths_ok']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

key_init = 0					#################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		#################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ###################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves

followers_collected_dir = "/home/amaury/coleta/n5/alters_followers/50/bin/"#### Diretório contendo o conjunto de amigos dos ego já coletados. Cada arquivo contém o conjunto de seguidores dos amigos.

data_dir = "/home/amaury/coleta/n6/timeline_collect/alters/bin/" ############## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n6/timeline_collect/alters/error/" ########### Diretório para armazenamento dos arquivos de erro

formato = 'll'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
timeline_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário


formato_followers = 'l'				############################################## Long para o código ('l') e depois o array de chars de X posições:	
followers_struct = struct.Struct(formato_followers) ########################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário


wait = 60
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
######################################################################################################################
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