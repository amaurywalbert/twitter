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
##		Status - Versão 6 - Coletar amigos do Twitter
##						
##						6.0 - Usando o conjunto de egos do diretório DATASET - è apenas um subconjunto para facilitar o desenvolvimento do trabalho..
##								Assim que concluída a coleta desse subconjunto, pode-se voltar a coletar usando a versão 5.
##						6.1	Melhoria na recepção de erros da API
##						6.2	Não usa dicionário. Consulta se arquivo existe direto no disco para permitir o uso paralelo de diversas instancias do script.
##						STATUS - EM TESTE - realizado o teste será necessário reescrever o script tirando o dicionário
##
##
##				
##						SALVAR APENAS O NECESSÁRIO PARA ECONOMIZAR ESPAÇO EM DISCO. Coletar tweets completos ocupa muito espaço.
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos BINÀRIOS!! contendo os a tweets favoritados a partir dos autores do tweets favoritados pelo egos.
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
			buffer = f.read(favorites_struct.size)
			tweet, user = favorites_struct.unpack(buffer)
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
	with open(error_dir+"timeline_collect_wait.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
		error = {'user':user,'reason':str(reason) ,'date':agora}
		outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
	print error
	
######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve os favofitos de um usuário específico 
#
######################################################################################################################################################################
def get_favorites(j,k,l,user):												#Coleta dos favoritos
	global dictionary
	global api
	global i
	favorites = []
	try:
		for page in tweepy.Cursor(api.favorites,id=user, count=200, wait_on_rate_limit = True, wait_on_rate_limit_notify = True).pages(16):				#Retorna os favoritos do usuário
			for tweet in page:
				favorites.append(tweet)
		return (favorites)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))

	except tweepy.error.RateLimitError as e:
		print("Limite de acesso à API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))

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
			
			elif e.message == 'Not authorized.': # Usuários não autorizados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".dat", "w") as f:			# Cria arquivo vazio
					print ("Usuário não autorizado. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1											

			elif e.message[0]['code'] == 32 or e.message[0]['code'] == 215 or e.message[0]['code'] == 429 or e.message[0]['code'] == 401:
				save_error(user,e.message)				
					
			elif e.message[0]['code'] == 34 or e.message[0]['code'] == 404:									# Usuários não existentes ou não encontrados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".dat", "w") as f:			# Cria arquivo vazio	
					print ("Usuário inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1
			else:
				save_error(user,e)
		except Exception as e2:
			save_error(user,e2)
######################################################################################################################################################################
#
# Obtem favoritos dos usuários
#
######################################################################################################################################################################
def save_favorites(j,k,l,user):  # j = número do ego que esta sendo coletado - k = numero do alter que esta sendo verificado - l = tamanho da lista de amigos do ego
	global i	# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de tweets do usuário
	t = 0 																# Número de Tweets por usuário
	favorites = get_favorites(j,k,l,user)
	if favorites:	
		try:
			with open(data_dir+str(user)+".dat", "w+b") as f:
				for status in favorites:
					t+=1
					f.write(favorites_struct.pack(status.id,status.user.id))						# Grava os ids dos amigos no arquivo binário do usuário
###
#			tweets_list = read_arq_bin(data_dir+str(user)+".dat") # Função para converter o binário de volta em string em formato json.
#			print tweets_list
####				
			dictionary[user] = user									# Insere o usuário coletado na tabela em memória
			i +=1
			print ("Ego nº: "+str(j)+" - Alter ("+str(k)+"/"+str(l)+"): "+str(user)+" coletados com sucesso. "+str(t)+" tweets. Total coletados: "+str(i))
	
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
	
	for file in os.listdir(egos_favorites_dir):					# Verifica a lista de egos coletados e para cada um, busca os autores de retweets dos alters listados no arquivo do ego.
		j+=1
		authors_list = read_arq_bin(egos_favorites_dir+file) # Função para converter o binário de volta em string em formato json.
		l = len(authors_list)										# Exibe o tamanho/quantidade de autores de retweets do ego
		k = 0																#Exibe o número ordinal do alter que está sendo coletado a lista de amigos
		for author in authors_list:
			k+=1
			if not os.path.isfile(data_dir+str(author)+".dat"):
				save_favorites(j,k,l,author)							#Inicia função de busca
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
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full' 		# 50, 100, 500 ou full
######################################################################################################################
######################################################################################################################
egos_favorites_dir = "/home/amaury/dataset/n3/egos/bin/"												# Arquivo contendo a lista dos usuários ego já coletados
data_dir = "/home/amaury/coleta/n3/alters/"+str(qtde_egos)+"/bin/"								# Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n3/alters/"+str(qtde_egos)+"/error/" 							# Diretório para armazenamento dos arquivos de erro
formato = 'll'				################################################################### Long para o código ('l') e depois o array de chars de X posições:	
favorites_struct = struct.Struct(formato) ################################################# Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
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

# Registre sua aplicacao em https://apps.twitter.com
#App 1
#Access Token	883452349641089025-H7cpOcBL3UGP5RlS1Wpvwzowzuvj56x
#Access Token Secret	X5DGAble5W3kD00sgbhcLMHOqypQQGfRqOrUhLfuVv2vC
#Consumer Key (API Key)	0EMlPO3xsnI7woFX2X1ndE9SZ
#Consumer Secret (API Secret)	5mwAJQ3zUo5A34815TBo2Plk4w4NghzuIXY8l2owSs0Jmd8QOK

#App 2
#Access Token	883452349641089025-XUnIkLA9u6DE8Bmc0D5lwl8Ya1SVhdd
#Access Token Secret	FDfMTIMlSRHNZcy71UyOU8xUvAZ5crsqt8QKnJ4E0E576
#Consumer Key (API Key)	2f18aOuyQU6K8NuMiy0Q1B61P
#Consumer Secret (API Secret)	1mljO1psJeGzAWyT0QqwMULFM1ghj12XcOIcwccv7N3fcszPIg

#App3
#Access Token	883452349641089025-bFOinBoce7oQvueecF9dTMWxoArTPDA
#Access Token Secret	xnRAHwCoSOmFsRppkJtHU3O3mHk54SzSGQBw1fYVBORmD
#Consumer Key (API Key)	TNs9lxCwAqXVd3Fuq0MiM1Y9V
#Consumer Secret (API Secret)	oaE23LzAktOWNxRBRY4dT5icHTQ6nubPZlf8fTWqI6rGfNkRbU

consumer_key = "2f18aOuyQU6K8NuMiy0Q1B61P"
consumer_secret = "1mljO1psJeGzAWyT0QqwMULFM1ghj12XcOIcwccv7N3fcszPIg"
access_token = "883452349641089025-XUnIkLA9u6DE8Bmc0D5lwl8Ya1SVhdd"
access_token_secret = "FDfMTIMlSRHNZcy71UyOU8xUvAZ5crsqt8QKnJ4E0E576"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


	
#Executa o método main
if __name__ == "__main__": main()