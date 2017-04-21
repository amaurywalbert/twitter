# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth_n3
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 3.0 - Coletar favorites dos usuários especificados
##						
##						3.1 - Uso do Tweepy para controlar as autenticações... WAIT
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos JSON contendo os a tweets favoritados dos usuários.
##
##						STATUS - Refazer a coleta até que não tenha nenhuma mensagem de "Rate Limit Exceeded"  - A cada mensagem há um usuário que ficou sem ser coletada
##
## 
######################################################################################################################################################################

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
	global i
	favorites = []
	try:
		for page in tweepy.Cursor(api.favorites,id=user, count=200, wait_on_rate_limit = True, wait_on_rate_limit_notify = True).pages(16):				#Retorna os favoritos do usuário
			for tweet in page:
				favorites.append(tweet)
		return (favorites)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))

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
# Obtem favoritos dos usuários
#
######################################################################################################################################################################
def save_favorites(j,user): # j = número do usuário que esta sendo coletado
	global i	# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de tweets do usuário
	k = 0 																# Número de Tweets por usuário
	favorites = get_favorites(user)
	if favorites:	
		try:
			with open(data_dir+str(user)+".json", "w") as f:	
				for tweet in favorites:
					k+=1
					f.write(json.dumps(tweet._json)+"\n")		# ... no arquivo, imprime o tweet (status) inteiro.
			
			dictionary[user] = user									# Insere o usuário coletado na tabela em memória
			i +=1
			print ("Usuário nº "+str(j)+": "+str(user)+" coletado com sucesso. "+str(k)+" tweets. Total de usuários coletados: "+str(i))
	
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
	else:
		with open(data_dir+str(user)+".json", "w") as f:
			print ("Não há favoritos para este usuário...")


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
	for file in os.listdir(egos_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		j+=1
		ego = file.split(".dat")
		ego = long(ego[0])
		if not dictionary.has_key(ego):
			print (str(j)+" - ego_id: "+str(ego)+" - Coletando...")		
			save_favorites(j, ego)						#Inicia função de busca dos favoritos
#		else:
#			print (str(j)+" - Já coletado!")	
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
oauth_keys = multi_oauth_n3.keys()
auths = oauth_keys['auths_test']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

key_init = 0					#################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		#################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ###################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves
egos_dir = "/home/amaury/coleta/n1/egos_friends/500/bin/"###################### Arquivo contendo a lista dos usuários ego já coletados
data_dir = "/home/amaury/coleta/favorites_collect/500/json/" ################## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/favorites_collect/500/error/" ################ Diretório para armazenamento dos arquivos de erro
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

# Registre sua aplicacao em https://apps.twitter.com

consumer_key = "gOa37Y85DcbM2Oi3IpvvFWMj9"
consumer_secret = "Fh334ZT5fXKDTS8zGJR1N6RU3kDdLKhEAk2ZB97iKydCUCaMQp"
access_token = "849270909034692608-YPMJReaqxI6oVdP7RQ2cfqJinlghtuD"
access_token_secret = "A6g4aVqq17gAzNPmxsDFIPUo9PVb546JlGw0gK3agWgiM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


	
#Executa o método main
if __name__ == "__main__": main()