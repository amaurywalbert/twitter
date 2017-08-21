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
##		Status - Versão 6 - Coletar amigos do Twitter
##						
##						6.0 - Usando o conjunto de egos do diretório DATASET - è apenas um subconjunto para facilitar o desenvolvimento do trabalho..
##								Assim que concluída a coleta desse subconjunto, pode-se voltar a coletar usando a versão 5.
##						6.1	Melhoria na recepção de erros da API
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##				
##						SALVAR APENAS O NECESSÁRIO PARA ECONOMIZAR ESPAÇO EM DISCO. Coletar tweets completos ocupa muito espaço.
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos BINÀRIOS!! contendo o id do retweet e id do autor a partir da lista de autores dos retweets do egos.
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
		authors_list = set()
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)
			authors_list.add(user)
	return authors_list

######################################################################################################################################################################
#
# Grava o erro num arquivo específco 
#
######################################################################################################################################################################
def save_error(user,reason):
	agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
	error={}
	with open(error_dir+"timeline_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
		error = {'user':user,'reason':reason ,'date':agora, 'key':key}
		outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
	print error

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a timeline de um usuário específico 
#
######################################################################################################################################################################
def get_timeline(j,k,l,user):												#Coleta da timeline
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
		print ("ERRO - Ego nº: "+str(j)+" - Alter ("+str(k)+"/"+str(l)+"): "+str(user))
		try:
			if e.reason == "Twitter error response: status code = 404":							# Usuários não existentes ou não encontrados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".dat", "w") as f:			# Cria arquivo vazio	
					print ("Usuário não encontrado. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1

			elif e.reason == "Twitter error response: status code = 401":							# Usuários não existentes ou não encontrados
				save_error(user,e.reason)
				api = autentication(auths)
			
			elif e.message == 'Not authorized.': # Usuários não autorizados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".dat", "w") as f:			# Cria arquivo vazio
					print ("Usuário não autorizado. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1											

			elif e.message[0]['code'] == 32 or e.message[0]['code'] == 215 or e.message[0]['code'] == 429 or e.message[0]['code'] == 401:
				save_error(user,e.message)				
				key = random.randint(key_init,key_limit)
				api = autentication(auths)
					
			elif e.message[0]['code'] == 34 or e.message[0]['code'] == 404:									# Usuários não existentes ou não encontrados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".dat", "w") as f:			# Cria arquivo vazio	
					print ("Usuário inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1
			else:
				save_error(user,str(e))
				api = autentication(auths)
		except Exception as e2:
			save_error(user,e2)
			api = autentication(auths)	
######################################################################################################################################################################
#
# Obtem timeline dos usuários
#
######################################################################################################################################################################
def save_timeline(j,k,l,user): # j = número do ego que esta sendo coletado - k = numero do alter que esta sendo verificado - l = tamanho da lista de amigos do ego
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
			print ("Ego nº: "+str(j)+" - Alter ("+str(k)+"/"+str(l)+"): "+str(user)+" coletados com sucesso. "+str(t)+" retweets. Total coletados: "+str(i))
	
		except Exception as e:	
			if e.message:		
				save_error(user,e.message)
			else:
				save_error(user,str(e))
			if os.path.exists(data_dir+str(user)+".dat"):
				os.remove(data_dir+str(user)+".dat")
				print ("Arquivo removido co sucesso...")


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

	for file in os.listdir(egos_retweets_dir):					# Verifica a lista de egos coletados e para cada um, busca os autores de retweets dos alters listados no arquivo do ego.
		j+=1
		authors_list = read_arq_bin(egos_retweets_dir+file) # Função para converter o binário de volta em string em formato json.
		l = len(authors_list)										# Exibe o tamanho/quantidade de autores de retweets do ego
		k = 0																#Exibe o número ordinal do alter que está sendo coletado a lista de amigos
		for authors in authors_list:
			k+=1
			if not dictionary.has_key(authors):
				save_timeline(j,k,l,authors)							#Inicia função de busca
#		print ("Ego: "+str(j)+" - "+str(len(authors_list))+" alters.")
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
auths = oauth_keys['auths_ok']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full' 		# 50, 100, 500 ou full
######################################################################################################################
######################################################################################################################
key_init = 0					############################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		############################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ################################################# Inicia o script a partir de uma chave aleatória do conjunto de chaves
egos_retweets_dir = "/home/amaury/dataset/n2/egos/bin/"				################## Arquivo contendo a lista dos usuários ego já coletados
data_dir = "/home/amaury/coleta/n2/alters/"+str(qtde_egos)+"/bin/" 						###### Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n2/alters/"+str(qtde_egos)+"/error/"					###### Diretório para armazenamento dos arquivos de erro
formato = 'll'				##################################################################  Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato) ################################################# Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
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