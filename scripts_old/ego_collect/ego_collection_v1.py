### -*- coding: latin1 -*-
################################################################################################
# Script para coletar seeds do Twitter:
#	Mínimo de 2 listas
#	Mínimo de 5 membros em cada lista	
#
import tweepy, datetime, sys, time, json, os.path

##Timeline_collect - APP (por enquanto...)

##amaurywalbert@live.com
##walbert1810


################################################################################################
##		Status - OK - Salvando em String
##					OK	- Coletando apenas 1000 listas - Corrigido com uso do Método API.Cursor
##					OK - Considerando o mínimo de 1 lista
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
			t = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M")
			rate_limit_err = open("error/seeds_collect.rate_limit_err", "a+") # Abre o arquivo para gravação no final do arquivo
			rate_limit_err.writelines(t, "Limite para verificar os limites da API atingido. Vamos aguardar 60 seg...")
			rate_limit_err.close()
			print(t, "Limite para verificar os limites da API atingido. Vamos aguardar 60 seg...")
			sys.stdout.flush()
			time.sleep(60)
		except tweepy.error.TweepError as e:
			t = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')
			print(t, e," Erro de conexão. Aguardando 60 seg...")
			cnx_err = open("error/seeds_collect.cnx_err", "a+") # Abre o arquivo para gravação no final do arquivo
			cnx_err.writelines(t, e,". Erro de conexão. Aguardando 60 seg...")
			cnx_err.close()
			sys.stdout.flush()
			time.sleep(60)

	lists_subscriptions_remaining = int(rate_limit['resources']['lists']['/lists/subscriptions']['remaining'])
	lists_ownerships_remaining = int(rate_limit['resources']['lists']['/lists/ownerships']['remaining'])
	rate_limit_remaining = int(rate_limit['resources']['application']['/application/rate_limit_status']['remaining'])
	
	print("lists_subscriptions_remaining = ",lists_subscriptions_remaining)
	print("lists_ownerships_remaining = ",lists_ownerships_remaining)
	print("rate_limit_remaining = ",rate_limit_remaining)
	return {'lists_ownerships_remaining': lists_ownerships_remaining,'lists_subscriptions_remaining': lists_subscriptions_remaining,'rate_limit_remaining': rate_limit_remaining}


################################################################################################
#
# Obtem as listas criadas por um usuário específico
#
################################################################################################

def count_lists_ownerships(user):
	print
	print("Recuperando listas de curadoria do usuário: "+user)
	print
	limits = get_api_limits()
	
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
	
	try:

		owner = [] 		#Inicializar array
			
		seeds_file = open("data/seeds_collect.txt", 'a+') # Arquivo com a lista dos usuários que possuem as listas
		lists_file = open("data/list_collect.txt", 'a+') # Arquivo com os ids das listas com o mínimo exigido
		seeds_list_file = open("data/users/"+user+"list_collect.txt", 'a+') # Arquivo com informações sobre as list
		
		for page in tweepy.Cursor(api.get_lists_ownerships,id=user,wait_on_rate_limit=True, count=1000).pages():						
			for list in page:
				print(user,list.id,list.created_at,list.name,list.member_count)			# Na tela, imprime o resumo de cada lista...
				
				if (list.member_count >= 5):
					owner.append(list.id) 	#Agrupa os ids das listas ... #Verificar tipo de coleção "deque"
					seeds_list_file.write(str(list)+"\n")		# ... no arquivo, imprime as Listas completas (list)
			
			if (len(owner) > 0):
				lists_file.write(str(owner)+"\n")
				seeds_file.write(str(user)+"\n") # Salvando o screen_name do usuário - obs. salvando em duplicidade (em cada função salva o nome de novo).... 		

		seeds_file.close()	#Fecha o arquivo para salvar os dados com segurança...
		lists_file.close()	
		seeds_list_file.close()
				
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		get_list_err = open("error/"+user+"_lists_count_"+str(agora)+".get_list_err", "a+") # Abre o arquivo para gravação no final do arquivo
		get_list_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		get_list_err.close()
		print("[ERRRO] Não foi possível contar as listas de: "+user+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
	
	return (owner)


################################################################################################
#
# Obtem as listas de subscrições de um usuário específico
#
################################################################################################

def count_lists_subscriptions(user):
	print	
	print("Recuperando listas de subscrição do usuário: "+user)
	print
	limits = get_api_limits()
	
	# Vamos verificar dois limites:
	#
	# . lists_subscriptions_remaining  = requisicoes que ainda podem ser feitas
	#                                 para as lista de um usuario especifico
	# . rate_limit_status_remaining = requisicoes que ainda podem ser feitas 
	#                                 sobre qual o limite ainda disponivel 
	#                                 (sim, o twitter limita ate isso)
	#
	
	while(limits['lists_subscriptions_remaining'] == 0 | limits['rate_limit_remaining'] == 0):
		print("Limite de acesso à API excedido. Vamos aguardar por 1 min...")
		sys.stdout.flush()
		time.sleep(60)
		limits = get_api_limits()
	try:
		
		subs = []	#Inicializar array
		
		seeds_file = open("data/seeds_collect.txt", 'a+')	# Arquivo com a lista dos usuários que possuem as listas
		lists_file = open("data/list_collect.txt", 'a+')	# Arquivo com os ids das listas com o mínimo exigido
		seeds_list_file = open("data/users/"+user+"list_collect.txt", 'a+')	# Arquivo com informações sobre as listas
		
		for page in tweepy.Cursor(api.lists_subscriptions,id=user,wait_on_rate_limit=True, count=1000).pages():						
			for list in page:
				print(user,list.id,list.created_at,list.name,list.member_count)			# Na tela, imprime o resumo de cada lista...
				
				if (list.member_count >= 5):
					subs.append(list.id) 	#Agrupa os ids das listas ... #Verificar tipo de coleção "deque"
					seeds_list_file.write(str(list)+"\n")		# ... no arquivo, imprime as Listas completas (list)
			
			if (len(subs) > 0):
				lists_file.write(str(subs)+"\n")
				seeds_file.write(str(user)+"\n") # Salvando o screen_name do usuário - obs. salvando em duplicidade (em cada função salva o nome de novo).... 		

		seeds_file.close()	#Fecha o arquivo para salvar os dados com segurança...
		lists_file.close()	
		seeds_list_file.close()
		
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		subs_list_err = open("error/"+user+"_lists_collect_"+str(agora)+".subs_list_err", "a+") # Abre o arquivo para gravação no final do arquivo
		subs_list_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		subs_list_err.close()
		print("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		
	return (subs)

##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Manda buscar as listas de cada uma das contas especificadas no array (accounts).
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
#	arquivo = open('screen_name_seeds.txt', 'r') #Deve ser o screen_name
#	accounts = arquivo.readlines()
	accounts = ['amaurywalbert', 'amaurywcarvalho','thierson']
	for account in accounts:
		print("####################################################################################################")
		owner = count_lists_ownerships(account)
		subs = count_lists_subscriptions(account)
		lists = len(owner)+len(subs)
		print		
		print("Usuário: "+str(account)+". Total de listas com o mínimo de membros exigido: "+str(lists))	
		print
		print("####################################################################################################")
#	arquivo.close()
	print("Coleta finalizada!")
	

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

print ("Autenticação Realizada!\n")

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()