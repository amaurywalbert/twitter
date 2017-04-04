# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 5.0 - Coletar favorites dos autores dos tweets marcados como favoritos pelos usuários egos (lista de favoritos dos egos)) - Favoritos dos Alters
##
##						
##						5.1 - Uso do Tweepy para controlar as autenticações...
##
##				
##						SALVAR APENAS O NECESSÁRIO PARA ECONOMIZAR ESPAÇO EM DISCO. Coletar tweets completos ocupa muito espaço.
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos JSON contendo os a tweets favoritados a partir da lista de favoritos dos egos.
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

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve os favofitos de um usuário específico 
#
######################################################################################################################################################################
def get_favorites(user):												#Coleta dos favoritos
	global key
	global dictionary
	global api
	global i
	favorites = []
	try:
		for page in tweepy.Cursor(api.favorites,id=user, count=200).pages(16):				#Retorna os favoritos do usuário
			for tweet in page:
				favorites.append(tweet)
		return (favorites)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))
			api = autentication(auths)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"favorites_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:
				error = {'user':user,'reason': e.message,'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'user':user,'reason': str(e),'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
		try:
			if e.message[0]['code'] == 32 or e.message[0]['code'] == 215 or e.message[0]['code'] == 429:
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
		
		try:
			if e.message == 'Twitter error response: status code = 429' or e.message == 'Twitter error response: status code = 401': #muitas requisições simultâneas
				key = random.randint(key_init,key_limit)
				api = autentication(auths)
				i +=1
		except Exception as e4:
			print ("E4: "+str(e4))			
######################################################################################################################################################################
#
# Obtem favoritos dos usuários
#
######################################################################################################################################################################
def save_favorites(j,l,user): # j = número do usuário ego que esta sendo coletado, l = numero do alter de cada ego que está sendo coletado.
	global i	# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de tweets do usuário
	k = 0 																# Número de Tweets por usuário
	favorites = get_favorites(user)
	if favorites:	
		try:
			with open(data_dir+str(user)+".json", "w") as f:
				for status in favorites:
					tweet = {'tweet':status.id, 'user':status.user.id}
					k+=1
					f.write(json.dumps(tweet, separators=(',', ':'))+"\n")	# ... no arquivo, imprime o apenas o id do tweet e o id do author.
			dictionary[user] = user									# Insere o usuário coletado na tabela em memória
			i +=1
			print ("Ego nº: "+str(j)+" - Alter("+str(l)+"): "+str(user)+" coletado com sucesso. "+str(k)+" tweets. Total de usuários coletados: "+str(i))
	
		except Exception as e:	
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(error_dir+"favorite_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
				if e.message:		
					error = {'user':user,'reason': e.message,'date':agora}
				else:
					error = {'user':user,'reason': str(e),'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			if os.path.exists(data_dir+str(user)+".json"):
				os.remove(data_dir+str(user)+".json")


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
	j = 0															# Exibe o número ordinal do ego que está sendo usado para a coleta dos favoritos
	l = 0															# Exibe o número ordinal do alter que está sendo usado para a coleta dos favoritos
	
	for file in os.listdir(favorites_collected_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		j+=1
		with open(favorites_collected_dir+file,'r') as favorites:
			for line in favorites:
				l+=1
				tweet = json.loads(line)
				user =  tweet['user']['id']
				user = long(user)
				if not dictionary.has_key(user):
					save_favorites(j,l,user)						#Inicia função de busca dos favoritos
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
oauth_keys = multi_oauth.keys()
auths = oauth_keys['auths_ok']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

key_init = 0					#################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		#################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ###################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves

favorites_collected_dir = "/home/amaury/coleta/favorites_collect/50/json/"#### Arquivo contendo a lista dos usuários ego já coletados

data_dir = "/home/amaury/coleta/favorites_collect/alters/json/" ################## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/favorites_collect/alters/error/" ################ Diretório para armazenamento dos arquivos de erro
wait = 5
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
	user_id = file.split(".json")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
#Autenticação
api = autentication(auths)

	
#Executa o método main
if __name__ == "__main__": main()