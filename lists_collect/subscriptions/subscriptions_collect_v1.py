# -*- coding: latin1 -*-
################################################################################################
# Script para coletar listas inscritas pelos usuários
#
import tweepy, datetime, sys, time, json, os.path

##Timeline_collect - APP (por enquanto...)

##amaurywalbert@live.com
##walbert1810


################################################################################################
##		Status - OK - Salvando em String
##						- Coletando apenas 1000 listas 
################################################################################################



################################################################################################
#
# Verifica quais os limites ainda disponiveis para consumo da API do Twitter
#
################################################################################################

def get_api_limits():

	print("Verificando limites da API...")

	# Pode ser que o programa ja inicie com o limite de requisicoes estourado.
	rate_limit_available = False
	
	while not rate_limit_available:
		try:
			rate_limit = api.rate_limit_status()
			rate_limit_available = True
		except tweepy.error.RateLimitError as e:
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')
			rate_limit_err = open("lists_collect"+agora+'.rate_limit_err', 'a+') # Abre o arquivo para gravação no final do arquivo
			rate_limit_err.writelines(t, "Limite para verificar os limites da API atingido. Vamos aguardar 60 seg...")
			rate_limit_err.close()
			print(t, "Limite para verificar os limites da API atingido. Vamos aguardar 60 seg...")
			sys.stdout.flush()
			time.sleep(60)
		except tweepy.error.TweepError as e:
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')
			print(t, e," Erro de conexão. Aguardando 60 seg...")
			cnx_err = open("lists_collect"+agora+'.cnx_err', 'a+') # Abre o arquivo para gravação no final do arquivo
			cnx_err.writelines(t, e,". Erro de conexão. Aguardando 60 seg...")
			cnx_err.close()
			sys.stdout.flush()
			time.sleep(60)

	lists_subscriptions_remaining = int(rate_limit['resources']['lists']['/lists/subscriptions']['remaining'])
	rate_limit_remaining = int(rate_limit['resources']['application']['/application/rate_limit_status']['remaining'])
	
	print("lists_subscriptions_remaining = ",lists_subscriptions_remaining)
	print("rate_limit_remaining = ",rate_limit_remaining)
	return {'lists_subscriptions_remaining': lists_subscriptions_remaining,'rate_limit_remaining': rate_limit_remaining}



################################################################################################
#
# Obtem as listas de um usuário específico
#
################################################################################################

def get_lists_subscriptions(screen_name):
	print("Recuperando listas de: "+screen_name)
	limits = get_api_limits()
	
	agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')
	
	# Vamos verificar dois limites:
	#
	# . lists_subscriptions_remaining  = requisicoes que ainda podem ser feitas
	#                                 para as listas de um usuario especifico
	# . rate_limit_status_remaining = requisicoes que ainda podem ser feitas 
	#                                 sobre qual o limite ainda disponivel 
	#                                 (sim, o twitter limita ate isso)
	#
	while(limits['lists_subscriptions_remaining'] == 0 | limits['rate_limit_remaining'] == 0):
		print("Limite de acesso à API excedido. Vamos aguardar por 1 min...")
		sys.stdout.flush()
		time.sleep(60)
		limits = get_api_limits()

	# Pode ser que aconteca de a chamada a seguir estourar
	# os limites de requisicoes da API, causando o erro:
	# tweepy.error.RateLimitError: [{'message': 'Rate limit exceeded', 'code': 88}]
	# Por isso fizemos o teste anterior, para que este erro nunca ocorra.
	
	#Coleta todas as listas subscritas por um usuário específico
	try:

		lists_subscriptions = api.lists_subscriptions(screen_name,count=1000)

	except tweepy.error.TweepError as e:
		subs_list_err = open(screen_name+"_lists_collect_"+agora+".subs_list_err", "a+") # Abre o arquivo para gravação no final do arquivo
		subs_list_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+screen_name+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		subs_list_err.close()
		print("[ERRRO] Não foi possível recuperar as listas de: "+screen_name+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		lists_subscriptions = []
	return lists_subscriptions


################################################################################################
#
# Metodo que coleta listas criadas por um usuário
#
################################################################################################

def collect_lists_subscriptions(screen_name):	
	print("Iniciando busca de listas de: "+screen_name)
	try:
		lists_subscriptions = get_lists_subscriptions(screen_name) #the screen name of the user of the list
	
		# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')	
	
		# Vamos salvar as listas de cada usuario em um arquivo diferente.
		lists_file = open(screen_name+"subs_lists_collect_"+agora+".txt", 'w')	
		
		i = 0
		
		for list in lists_subscriptions:
			i = i + 1
			
			# Na tela, imprime o resumo de cada lista...
			print(screen_name,i,list.id,list.created_at,list.full_name,list.member_count)
			
			# ... no arquivo, imprime as Listas (list).
			lists_file.write(str(list)+"\n")


			#	Falta salvar em JSON
			#lists_file.write(json.dumps(list._json)+"\n")
			
		#Fecha o arquivo para salvar os dados com segurança...
		lists_file.close()

	except tweepy.error.TweepError as e:
		save_subs_list_err = open(subscriptions+"_lists_collect_"+agora+".save_subs_lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		save_subs_list_err.writelines("[ERRRO] Não foi possível salvar as listas de: "+screen_name+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		save_subs_list_err.close()
		print("[ERRRO] Não foi possível salvar as listas de: "+screen_name+". Erro: "+str(e)+". Vou ignorar e tocar adiante.")



################################################################################################
#
# Metodo principal do programa.
# Manda buscar as listas de cada uma das contas especificadas no array (accounts).
#
################################################################################################

def main():
#	arquivo = open('screen_name_seeds.txt', 'r') #Deve ser o screen_name
#	accounts = arquivo.readlines()
	accounts = ['amaurywalbert', 'amaurywcarvalho','thierson']
	for account in accounts:
		collect_lists_subscriptions(account)
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