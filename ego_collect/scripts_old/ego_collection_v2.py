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
##					OK - Verificando por limites usando apenas o Tweepy
##					Error - Coleta não atende requisitos mínimos do projeto.
################################################################################################

################################################################################################
#
# Testa se lista já foi adicionada.
#
################################################################################################

def check(search,datafile):
	file = datafile.readlines()
	found = False
	for line in file:
		if str(search) in line:
			found = True
			break
		else:
			found = False
	return (found)


################################################################################################
#
# Obtem as listas criadas por um usuário específico
#
################################################################################################

def count_lists_ownerships(user):
	print
	print("Recuperando listas de curadoria do usuário: "+user)
	print
	
	try:

		owner = [] 		#Inicializar array
			
		seeds_file = open("data/seeds_collect.txt", 'a+') # Arquivo com a lista dos usuários que possuem as listas
		lists_file = open("data/lists_collect.txt", 'a+') # Arquivo com os ids das listas com o mínimo exigido
		seeds_lists_file = open("data/users/"+user+"_lists_collect.txt", 'a+') # Arquivo com informações sobre as list
		
		for page in tweepy.Cursor(api.get_lists_ownerships,id=user,wait_on_rate_limit=True,wait_on_rate_limit_notify=True, count=1000).pages():						
			for list in page:
				print(list.id,list.created_at,list.name,list.member_count)			# Na tela, imprime o resumo de cada lista...
				
				if (list.member_count >= 5):	#Testa se a quantidade de membros da lista atinge o limite mínimo.
					seeds_lists_file.write(str(list)+"\n")		# ... no arquivo, imprime as Listas completas (list)
					
					if check(list.id,lists_file):	#Verifica se a lista já foi adicionada no arquivo de listas.
						print "Lista já adicionada! Continuando..."
					else:
						owner.append(list.id) 	#Agrupa os ids das listas ... #Verificar tipo de coleção "deque" ou metodo extend para listas. ex: owner.extend

			if (len(owner) > 0):
				lists_file.write(str(owner)+"\n")
				
				if check(user,seeds_file):	#Verifica se o usuário já foi adicionado no arquivo de seeds.
					print "Usuário já adicionado! Continuando..."
				else:
					seeds_file.write(str(user)+"\n") # Salvando o screen_name do usuário.
		
		seeds_file.close()	#Fecha o arquivo para salvar os dados com segurança...
		lists_file.close()	
		seeds_lists_file.close()
				
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		get_lists_err = open("error/"+user+"_lists_count_"+str(agora)+".get_lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		get_lists_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		get_lists_err.close()
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
	
	try:	
		subs = []	#Inicializar array
		
		seeds_file = open("data/seeds_collect.txt", 'a+')	# Arquivo com a lista dos usuários que possuem as listas
		lists_file = open("data/lists_collect.txt", 'a+')	# Arquivo com os ids das listas com o mínimo exigido
		seeds_lists_file = open("data/users/"+user+"_lists_collect.txt", 'a+')	# Arquivo com informações sobre as listas
		
		for page in tweepy.Cursor(api.lists_subscriptions,id=user,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=1000).pages():						
			for list in page:
				print(list.id,list.created_at,list.name,list.member_count)			# Na tela, imprime o resumo de cada lista...						

				if (list.member_count >= 5):	#Testa se a quantidade de membros da lista atinge o limite mínimo.
					seeds_lists_file.write(str(list)+"\n")		# ... no arquivo, imprime as Listas completas (list)
					
					if check(list.id,lists_file):	#Verifica se a lista já foi adicionada no arquivo de listas.
						print "Lista já adicionada! Continuando..."
					else:
						subs.append(list.id) 	#Agrupa os ids das listas ... #Verificar tipo de coleção "deque" ou metodo extend para listas. ex: owner.extend

			
			if (len(subs) > 0):
				lists_file.write(str(subs)+"\n")
				
				if check(user,seeds_file):	#Verifica se o usuário já foi adicionado no arquivo de seeds.
					print "Usuário já adicionado! Continuando..."
				else:
					seeds_file.write(str(user)+"\n") # Salvando o screen_name do usuário.

		seeds_file.close()	#Fecha o arquivo para salvar os dados com segurança...
		lists_file.close()	
		seeds_lists_file.close()
		
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		subs_lists_err = open("error/"+user+"_lists_collect_"+str(agora)+".subs_lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		subs_lists_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		subs_lists_err.close()
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
	accounts = ['amaurywalbert','thierson']
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
api = tweepy.API(auth,wait_on_rate_limit=True)

print ("Autenticação Realizada!\n")

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()