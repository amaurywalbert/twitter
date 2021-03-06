# -*- coding: latin1 -*-
################################################################################################
# V 1.0
# Script para coletar seeds dos trends do Twitter:	
#

import tweepy, time, sys, ConfigParser, datetime, json, os.path, jsonpickle


reload(sys)
sys.setdefaultencoding('utf-8')

################################################################################################
##		Status - Teste - Coletando seeds dos trends do Twitter
## 
################################################################################################


################################################################################################
#
# Testa se lista ou usuário já foi adicionada(o) ao arquivo correspondente.
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


##########################################################################################################################################################################
#
# Armazena os usuários seeds extraídos da coleta dos trends twitter 
#
##########################################################################################################################################################################
def search_seeds(query):
	try: 																					#Tell the Cursor method that we want to use the Search API (api.search) #Also tell Cursor our query, and the maximum number of tweets to return
		maxTweets = 10000 																#Maximum number of tweets we want to collect
		tweetsPerQry = 100 																#The twitter Search API allows up to 100 tweets per query
		tweetCount = 0
		tweets_collected = open('data/tweets_collected.json', 'a+')					#Open a text file to save the tweets to
		for tweet in tweepy.Cursor(api.search,q=query, result_type="recent",wait_on_rate_limit=True,wait_on_rate_limit_notify=True).items(maxTweets):
			tweets_collected.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')				#Write the JSON format to the text file, and add one to the number of tweets we've collecte
			tweetCount += 1
			print("Downloaded {0} tweets".format(tweetCount))				#Display how many tweets we have collected
			seeds_collected = open("data/seeds_collected.txt", 'r')											# Arquivo com os seeds (membros das listas selecionadas serão adicionados ao final do arquivo user collect para continuar o processo de busca			
			if check(tweet.user.id,seeds_collected):												#Adiciona o usuário ao arquivo de seeds
				print (str(tweet.user.id)+" já adicionado! Continuando...")
			else:
				seeds = open("data/seeds_collected.txt", 'a+')		# Arquivo com os seeds (membros das listas selecionadas serão adicionados ao final do arquivo user collect para continuar o processo de busca
				seeds.writelines(str(tweet.user.id)+"\n")
				seeds.close()
		
		seeds_collected.close()
		tweets_collected.close()
			
	except tweepy.error.TweepError as e: 													#Armazena todos os erros em um único arquivo.
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		seeds_lists_err = open("error/seeds_list.err", "a+") # Abre o arquivo para gravação no final do arquivo
		seeds_lists_err.writelines(str(agora)+". Erro: "+str(e)+"\n")
		seeds_lists_err.close()
		print("[ERRRO] Não foi possível recuperar seeds. Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		


##########################################################################################################################################################################
#
# Realiza a coleta dos trends topics do twitter 
#
##########################################################################################################################################################################


def search_trends(search):
	try:
#		search_file = open("data/search.json", 'w') 		# Salvar a pesquisa realizada... apresenta uma lista com todos os locais disponíveis  (no nosso caso o parametro foi global (1), portanto aprensenta apenas ele)
#		search_file.write(json.dumps(search)+"\n")
#		search_file.close()
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		
		
		data = search[0] 										# Apresenta apenas o primeiro elemento da lista


		trends = data['trends']									#Extrai os objetos TRENDS - api Returns the top 10 trending topics for a specific WOEID, if trending information is available for it.

		i = 0
		names = []
		for i in range(10):
			names.append(trends[i]['name'])	
		
		#names = [trend['name'] for trend in trends]								# put all the names together with a ' ' separating them
		#names_file = open("data/names.json", 'w')
		#names_file.write(json.dumps(names)+"\n")
		#names_file.close()
		
		trends_querry = ' OR '.join(names)
		 
		print trends_querry
		
		trends_querry_file = open("data/trends_querry_"+agora+".txt", 'w') 		# Vamos a querry com a data e hora que foi feita a consulta.
		trends_querry_file.write(str(trends_querry)+"\n")
		trends_querry_file.close()


		
		return (trends_querry)
		

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		seeds_err = open("error/seeds_collect.lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		
		seeds_err.writelines(str(agora)+"[ERRRO] Não foi possível recuperar os trends. Erro: "+str(e)+".\n")
		seeds_err.close()
		print("[ERRRO] Não foi possível recuperar os trends. Erro: ",str(e),".\n")	


##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	search = api.trends_place(1) 	# Global information is available by using 1 as the WOEID. # from the end of your code trends1 is a list with only one element in it, which is a dict which we'll put in data.
	search_seeds(search_trends(search))
	
	
################################################################################################
#
# INICIO DO PROGRAMA
#
################################################################################################

# Registre sua aplicacao em https://apps.twitter.com
																											#Usando as 5 primeiras chaves do conjunto disponível no One Note
oauth_keys={'consumer_key':["ffap5ENG3yu0u7phgdhQzIvJx","L8LX4gmyLYpfaUDHPRTmAnO5E","O4t25YPnHGNm7B1i5qaN7Gu3s","R5iaxJ4FpLL6pcDOrr2osLNKr","w9GvsiaQy9jcBDTKIaXomBjQT"],
				'consumer_secret':["bFXgZjBUGMRoSfxbKLNZG8Y0IqjUPoc9O4vgKOtUCs0WSlkT6s","pCte0UiHaPIBbReSTTFm3pGV8mlS9L7b28azjIZ8vr7Sv320m4","v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR","PRNJxduOZgGsmjDlIeZIMuPF8qaauSxzYDlggdLWb1S3A5AOXO","H53rMVNGlrUvYFnN5f5ud1JzrGkhVpz2e335KBK413KrEK8Mwc"],
				'access_token':["813458922967302144-f3aEkz6OsueSD6eCkaN1yYXVcYXPGuZ","813458922967302144-wgByKpL2mDieJRbLrMbKxDySesoSHSS","813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi","813460676475842560-2aJSRKgnhugK16w1T4AERo0pkoNtjxO","813460676475842560-moOTo31XN8tbUbrKM3QOitihXsPD1Z9"],
				'access_token_secret':["OG08x1kx6rgMHwwEcmQKeeEAot88UALSQAY96XlGnpRba","i81wWiwi6MWNUgg8CHz5Z0S9zTUWSq3cSvmy44nBCKPE6","VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB","pSUfiFZmyb68U4YihPMFKWSQYKk2Js4cqGEgKNVbeS5xk","aGuidWdVzC24kkUSJ6BNDxKRwUPchCz0LWtEnVINJShY3"]}
auths = []

j=len(oauth_keys['consumer_key'])

for i in range(j):
	consumer_key = (oauth_keys['consumer_key'][i])
	consumer_secret = (oauth_keys['consumer_secret'][i])
	access_token = (oauth_keys['access_token'][i])
	access_token_secret = (oauth_keys['access_token_secret'][i])

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	auths.append(auth)
	
print ("Autenticando usando chave número: "+str(1))

api = tweepy.API(auths[0],wait_on_rate_limit=True)
print ("Autenticação Realizada!\n")


# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()
