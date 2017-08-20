# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 6 - Coletar amigos do Twitter
##						
##						6.1 - Usando o conjunto de egos do diretório DATASET - è apenas um subconjunto para facilitar o desenvolvimento do trabalho..
##								Assim que concluída a coleta desse subconjunto, pode-se voltar a coletar usando a versão 5.
##
##				
##						SALVAR APENAS O NECESSÁRIO PARA ECONOMIZAR ESPAÇO EM DISCO. Coletar tweets completos ocupa muito espaço.
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar a atenção com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos BINÀRIOS!! contendo o id do tweet e id do usuário mencionado.
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
		mentions_list = set()
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			tweet, user = timeline_struct.unpack(buffer)
			mentions_list.add(user)
	return mentions_list

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a timeline de um usuário específico 
#
######################################################################################################################################################################
def get_timeline(user):												#Coleta da timeline
	global dictionary
	global api
	global i
	timeline = []
	try:
		for page in tweepy.Cursor(api.user_timeline,id=user,wait_on_rate_limit_notify=True,wait_on_rate_limit=True,count=200).pages(16):				#Retorna os últimos 3200 tweets (16*20)
			for tweet in page:
				timeline.append(tweet)
		return (timeline)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. User: "+str(user)+" - Erro: "+str(e))

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"timeline_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:
				error = {'user':user,'reason': e.message,'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'user':user,'reason': str(e),'date':agora,}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
		try:
			print e.message.__dict__
			if e.message[0]['code'] == 34 or e.message[0]['code'] == 404:									# Usuários não existentes ou não encontrados
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
def save_timeline(j,k,l,user): # j = número do ego que esta sendo coletado - k = numero do alter que esta sendo verificado - l = tamanho da lista de amigos do ego
	global i	# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de tweets do usuário
	timeline = get_timeline(user)
	if timeline:	
		try:
			with open(data_dir+str(user)+".dat", "w+b") as f:
				for status in timeline:
					if not hasattr(status, 'retweeted_status'):	#Despreza retweets...
						mentions = status.entities['user_mentions']
						for mention in mentions:
							user_mentioned = long(mention['id'])
							f.write(timeline_struct.pack(status.id, user_mentioned))		# Grava os ids dos tweet e o id do user mencionado no arquivo binário do usuário

###
#			mentions_list = read_arq_bin(data_dir+str(user)+".dat") # Função para converter o binário de volta em string em formato json.
#			print mentions_list
####				
			dictionary[user] = user									# Insere o usuário coletado na tabela em memória
			i +=1
			print ("Ego nº: "+str(j)+" - Alter ("+str(k)+"/"+str(l)+"): "+str(user)+" coletados com sucesso. Total coletados: "+str(i))
			
	
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
# Realiza teste e coleta dos mencionados do alter especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i 																# numero de usuários com arquivos já coletados / Numero de arquivos no diretório
	j = 0																		# Exibe o número ordinal do ego que está sendo usado para a coleta dos mencionados
	for file in os.listdir(egos_mentions_dir):					# Verifica a lista de egos coletados e para cada um, busca os mencionados.
		j+=1
		mentions_list = read_arq_bin(egos_mentions_dir+file)
		l = len(mentions_list)											# Exibe o tamanho/quantidade de amigos na lista de mencionados
		k = 0																	#Exibe o número ordinal do alter que está sendo coletado
		for mentioned in mentions_list:
			k+=1
			if not dictionary.has_key(mentioned):
				save_timeline(j,k,l,mentioned)								#Inicia função de busca
#		print ("Ego: "+str(j)+" - "+str(len(mentions_list))+" alters.")
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
qtde_egos = 'full' 		#10, 50, 100, 500 ou 'full'
######################################################################################################################
######################################################################################################################

egos_mentions_dir = "/home/amaury/dataset/n4/egos/bin/"												# Arquivo contendo a lista dos usuários ego já coletados
data_dir = "/home/amaury/coleta/n4/alters/"+str(qtde_egos)+"/bin/" 								# Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n4/alters/"+str(qtde_egos)+"/error/" 							# Diretório para armazenamento dos arquivos de erro

formato = 'll'				#################################################### Long para id do tweet e outro long para autor e uma flag (0 ou 1) indicando se é um tetweet
timeline_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

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
#App1
consumer_key = "0EMlPO3xsnI7woFX2X1ndE9SZ"
consumer_secret = "5mwAJQ3zUo5A34815TBo2Plk4w4NghzuIXY8l2owSs0Jmd8QOK"
access_token = "883452349641089025-H7cpOcBL3UGP5RlS1Wpvwzowzuvj56x"
access_token_secret = "X5DGAble5W3kD00sgbhcLMHOqypQQGfRqOrUhLfuVv2vC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



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

	
#Executa o método main
if __name__ == "__main__": main()