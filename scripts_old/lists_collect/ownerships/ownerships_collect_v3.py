# -*- coding: latin1 -*-
################################################################################################
# Script para coletar listas criadas pelas usuários
#
import tweepy, datetime, sys, time, json, os.path

##Timeline_collect - APP (por enquanto...)

##amaurywalbert@live.com
##walbert1810

################################################################################################

##		Teste - Salvar arquivos em formato JSON

################################################################################################
# Verifica quais os limites ainda disponiveis para consumo da API do Twitter
#
def get_api_limits():

	print("Verificando limites da API...")

	# Pode ser que o programa ja inicie com o limite de requisicoes estourado.
	rate_limit_available = False
	
	while not rate_limit_available:
		try:
			rate_limit = api.rate_limit_status()
			rate_limit_available = True
		except tweepy.error.RateLimitError as e:
			t = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')
			rate_limit_err = open("lists_collect"+owner+'.rate_limit_err', 'a+') # Abre o arquivo para gravação no final do arquivo
			rate_limit_err.writelines(t, "Limite para verificar os limites da API atingido. Vamos aguardar 60 seg...")
			rate_limit_err.close()
			print(t, "Limite para verificar os limites da API atingido. Vamos aguardar 60 seg...")
			sys.stdout.flush()
			time.sleep(60)
		except tweepy.error.TweepError as e:
			t = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')
			print(t, e," Erro de conexão. Aguardando 60 seg...")
			cnx_err = open("lists_collect"+owner+'.cnx_err', 'a+') # Abre o arquivo para gravação no final do arquivo
			cnx_err.writelines(t, e,". Erro de conexão. Aguardando 60 seg...")
			cnx_err.close()
			sys.stdout.flush()
			time.sleep(60)

	lists_ownerships_remaining = int(rate_limit['resources']['lists']['/lists/ownerships']['remaining'])
	rate_limit_remaining = int(rate_limit['resources']['application']['/application/rate_limit_status']['remaining'])
	
	print("lists_ownerships_remaining = ",lists_ownerships_remaining)
	print("rate_limit_remaining = ",rate_limit_remaining)
	return {'lists_ownerships_remaining': lists_ownerships_remaining,'rate_limit_remaining': rate_limit_remaining}



################################################################################################
#
# Obtem as listas de um usuário específico
#
def get_lists_ownerships(screen_name):
	print("Recuperando listas de: "+screen_name)
	limits = get_api_limits()
	
	agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')
	
	# Vamos verificar dois limites:
	#
	# . lists_ownerships_remaining  = requisicoes que ainda podem ser feitas
	#                                 para as lista de um usuario especifico
	# . rate_limit_status_remaining = requisicoes que ainda podem ser feitas 
	#                                 sobre qual o limite ainda disponivel 
	#                                 (sim, o twitter limita ate isso)
	#
	while(limits['lists_ownerships_remaining'] == 0 | limits['rate_limit_remaining'] == 0):
		print("Limite de acesso à API excedido. Vamos aguardar por 1 min...")
		sys.stdout.flush()
		time.sleep(60)
		limits = get_api_limits()

	# Pode ser que aconteca de a chamada a seguir estourar
	# os limites de requisicoes da API, causando o erro:
	# tweepy.error.RateLimitError: [{'message': 'Rate limit exceeded', 'code': 88}]
	# Por isso fizemos o teste anterior, para que este erro nunca ocorra.
	
	#Coleta todas as listas criadas por um usuário específico
	try:

		#Função adicionada na liha 1002 do arquivo:
		#/usr/local/lib/python2.7/dist-packages/tweepy/api.py
		#
		#
		
		lists_ownerships = api.get_lists_ownerships(screen_name,count=1000) 

	except tweepy.error.TweepError as e:
		get_list_err = open(screen_name+"_lists_collect_"+agora+".get_list_err", "a+") # Abre o arquivo para gravação no final do arquivo
		get_list_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+screen_name+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		get_list_err.close()
		print("[ERRRO] Não foi possível recuperar as listas de: "+screen_name+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		lists_ownerships = []
	return lists_ownerships


################################################################################################
# Metodo que coleta listas criadas por um usuário

def collect_lists_ownerships(owner):	
	print("Iniciando busca de listas de: "+owner)
	try:
		lists_ownerships = get_lists_ownerships(owner) #the screen name of the owner of the list
	
		# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')	
	
		# Vamos salvar as listas de cada usuario em um arquivo diferente.
		lists_file = open(owner+"_lists_collect_"+agora+".json", 'w')
		
		# Vamos contar a quantidade de listas obtidas.
		i = 0	
		
		# Na tela, imprime as listas obtidas...
		print(lists_ownerships)
    
		# ... no arquivo, imprime a lista inteira.
		lists_file.write(str(lists_ownerships))
		#lists_file.write(json.dumps(lists_ownerships._json))
			
		#Fecha o arquivo para salvar os dados com segurança...
		lists_file.close()

	except tweepy.error.TweepError as e:
		save_list_err = open(owner+"_lists_collect_"+agora+".save_lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		save_list_err.writelines("[ERRRO] Não foi possível salvar as listas de: "+owner+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		save_list_err.close()
		print("[ERRRO] Não foi possível salvar as listas de: "+owner+". Erro: "+str(e)+". Vou ignorar e tocar adiante.")

################################################################################################
# Metodo principal do programa.
# Manda buscar as listas de cada uma das contas especificadas no array (accounts).

def main():
#	arquivo = open('screen_name_seeds.txt', 'r') #Deve ser o screen_name
#	accounts = arquivo.readlines()
	accounts = ['amaurywalbert', 'amaurywcarvalho','thierson']
	for account in accounts:
		collect_lists_ownerships(account)
#	arquivo.close()
	print("Coleta finalizada!", accounts)


################################################################################################
#
# INICIO DO PROGRAMA
#
################################################################################################

# Registre sua aplicacao em https://apps.twitter.com
consumer_key="qvmfyEldFvEmTCAvzFSBTP1wz"
consumer_secret="L4CQ640r3u72eMbdQaw4AvICRJOqSyu2pLpXi60ottICSgOuKA"
access_token="786664983862083584-jWBk9sZ6kLSPuArjaUdOMpJbblcFxD0"
access_token_secret="in67CMCZSDrVGLiPAP0iri5sfEzqRy3qsNOplPer2C2aQ"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()
