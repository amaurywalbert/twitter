# -*- coding: latin1 -*-
################################################################################################
# Script para coletar egos do Twitter:
#	Mínimo de 2 listas
#	Mínimo de 5 membros em cada lista	
#
import tweepy, datetime, sys, time, json, os.path, shutil, time

reload(sys)
sys.setdefaultencoding('utf-8')


##Timeline_collect - APP (por enquanto...)

##amaurywalbert@live.com
##walbert1810

################################################################################################
##		Status - Versão 7.0 - Script 02
##
##					OK	- Coletando todas as litas - adicionado Método API.Cursor
##					OK - Verificando por limites usando apenas o Tweepy
##					OK - Adicionar apenas o necessário para a coleta dos egos:
##							- Listas com pelo menos 5 membros;
##							- Users com no mínimo 02 lista (inscrito ou dono);
##							- Coleta snowball de egos a partir de seeds iniciais e crescendo com a análise dos membros das listas selecionadas.
##
##					OK - Armazenamento dos ids das listas...
##					OK - verificando pelo id dos users...
##
##		Status - OK - Gerenciador de chaves usando tweepy - Usando chaves 5 a 9 - outro script tá usando 0 a 4.
##
##		Status - OK - Script Funcionando! 
##
## 
################################################################################################


################################################################################################
#
# Realiza autenticação da aplicação.
#
################################################################################################

def autentication(auths):
	global key

	key += 1
	if (key >= 10):
		key = 0

	print ("Autenticando usando chave número: "+str(key))
	api_key = tweepy.API(auths[key])

	print ("Autenticação Realizada!\n")
	print
	print("####################################################################################################")
	print
	
	return (api_key)


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

################################################################################################
#
# Obtem os membros de uma lista
#
################################################################################################

def members_lists(list_id):
	global api
	
	print("Coletando membros da lista: "+str(list_id))
	try:
		members = []																				 	#Inicializando arrays	
		for page in tweepy.Cursor(api.list_members,list_id=list_id,wait_on_rate_limit_notify=True,count=5000).pages():
			for member in page:
				users_collected = open("/home/amaury/coleta/ego_collection2/data/users_collected.txt", 'r')											# Arquivo com os seeds (membros das listas selecionadas serão adicionados ao final do arquivo user collect para continuar o processo de busca
				if check(member.id,users_collected):								#Verifica se o usuário já foi adicionado no arquivo de membros coletados.
					print (str(member.id)+" já adicionado! Continuando...")
				else:					
					members.append(str(member.id)+"\n")
				users_collected.close()
		members_file = open("/home/amaury/coleta/ego_collection2/data/users_collected.txt", 'a+')
		members_file.writelines(members) 												# Salvando os membros adicionados
		members_file.close()


	except tweepy.RateLimitError as t:						# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando 60 segundos.\n")
		print		
		time.sleep(60)		
		api = autentication(auths,key)
		members_lists(list_id)		
			

	except tweepy.error.TweepError as e: 													#Armazena todos os erros em um único arquivo.
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		members_lists_err = open("/home/amaury/coleta/ego_collection2/error/members_list.lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		members_lists_err.writelines(str(agora)+" - list_id: "+str(list_id)+". Erro: "+str(e)+"\n")
		members_lists_err.close()
		print("[ERRRO] Não foi possível recuperar membros da lista: "+str(list_id)+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
	
		
################################################################################################
#
# Obtem as listas de um usuário específico (owner+subscription)
#
################################################################################################

def search_lists(user):
	global api
	
	print("Coletando listas do usuário: "+str(user))	
	lists = []
	
	try:
		for page in tweepy.Cursor(api.get_lists_ownerships,id=user,wait_on_rate_limit_notify=True,count=1000).pages():
			for list in page:												
				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
					lists.append(list)
				else:
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+". Não atende requisito mínimo. Continuando...")

		for page in tweepy.Cursor(api.lists_subscriptions,id=user,wait_on_rate_limit_notify=True,count=1000).pages():						
			for list in page:												
				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
					lists.append(list)
				else:
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+". Não atende requisito mínimo. Continuando...")

		if (len(lists) > 1):
			
			lists_collect = open("/home/amaury/coleta/ego_collection2/data/lists_collect.txt", 'a+')						# Arquivo com os ids das listas com o mínimo exigido
			lists_id = open("/home/amaury/coleta/ego_collection2/data/lists_collect.txt", 'r')						# Arquivo com os ids das listas com o mínimo exigido
					
			for list in lists:
				if check(list.id,lists_id):													#Verifica se a lista já foi adicionada no arquivo de listas.
					print ("Lista "+str(list.id)+" já adicionada! Continuando...")
				else:
					members_lists(list.id)														#Função para recuperar os membros da lista
					lists_collect.writelines(str(list.id)+"\n") 									# Salva o id da lista no arquivo de listas					
					print ("Lista "+str(list.id)+" salva com sucesso.")
			
			lists_id.close()
			lists_collect.close()
			
			
			ego_list = open('/home/amaury/coleta/ego_collection2/data/ego_list.txt','a+') 										#Lista de egos
			ego_list.writelines(str(user))														# Salva o id do usuário no arquivo de Egos coletados
			print ("Ego salvo com sucesso: "+str(user))		
			ego_list.close()
		
		users_verified = open('/home/amaury/coleta/ego_collection2/data/users_verified.txt','a+')							#Arquivo para armazenar a lista de usuários já verificados.
		users_verified.writelines(user)									# Salva o usuário no arquivo de users já verificados.
		users_verified.close()	




	except tweepy.RateLimitError as t:						# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando 60 segundos.\n")
		print
		time.sleep(60)		
		api = autentication(auths)
		search_lists(user)			

	
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		lists_err = open("/home/amaury/coleta/ego_collection2/error/lists_collect.lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		lists_err.writelines(str(agora)+"[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+".\n")
		lists_err.close()
		print("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")


##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():

	users_verified = open('/home/amaury/coleta/ego_collection2/data/users_verified.txt','a+')							#Arquivo para armazenar a lista de usuários já verificados.
	users_verified.close()
	users_collected = open('/home/amaury/coleta/ego_collection2/data/users_collected.txt','r') 							#Testando com o id do user
	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		account = users_collected.readline()													#Leia scren_name do usuário corrente		
		if (account == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
				eof = True
				#break
		else:
			users_verified = open('/home/amaury/coleta/ego_collection2/data/users_verified.txt','r')							#Arquivo para armazenar a lista de usuários já verificados.
			if check(account,users_verified):													#testa se o usuário já foi verificado, consultando o arquivo correspondente.
				print ("Usuário: "+str(account)+"Já verificado. Continuando...")
				print	
			else:
				print
				print("####################################################################################################")			
				search_lists(account)																#Inicia função de busca das listas e coleta dos membros
				print("####################################################################################################")
			users_verified.close()
	users_collected.close()
	print	
	print("Coleta finalizada!")
	
################################################################################################
#
# INICIO DO PROGRAMA
#
################################################################################################

# Registre sua aplicacao em https://apps.twitter.com
# Usando as primeiras chaves de cada conta do conjunto disponível no EverNote. Total de 10 contas:

oauth_keys={'consumer_key':["ffap5ENG3yu0u7phgdhQzIvJx","O4t25YPnHGNm7B1i5qaN7Gu3s","JeSUTJXGauV6RY7i6RJDSRvoL","qvmfyEldFvEmTCAvzFSBTP1wz","U7NBO7duqO1aTZ81q63Hy61Er","cWJz68mRioD4KYSMQm3F6PbCZ","4GpGgwHB3yeeZ8aQIZD4LLqre","UzOedM4QmOsM1xPsyPGLc2OI4","9sz6NkdPOIZyVM0W7qm5vpTqe","u6Qh4L8oLDINTl743zps4jSmb"],
				'consumer_secret':["bFXgZjBUGMRoSfxbKLNZG8Y0IqjUPoc9O4vgKOtUCs0WSlkT6s","v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR","ZCOMtPUTAJPFuEwm8S50wPIGF0CpVVFRJIQauy1DcSZ4w6v6ox","L4CQ640r3u72eMbdQaw4AvICRJOqSyu2pLpXi60ottICSgOuKA","kVKISoiaUrw1gBAZpTLPJ1op8GfONmHULeTMG01Ofj2OsAMkOg","Oa1N0HhN2Ifd4qzF09TGVflqDndvs77LlJHTH2XXk16gOs6TqJ","McX6jmXUPHu4eSTJQ41U7VY2q24mLJP5ZUcqYB4ovc2EoviOXH","B1TeVvnDgzxvMSjpg5bldlmSTid7C1UusnPmss9tMfvQVgFiCu","stQcxPa5gRCuyDPC4A4uvRNQxiVlV15D2cTZbyJ8Jo1wnj9HJo","iZprT4mlxrKeKnp1WUAcyGjYfDYkEgC6FAzu7H1H68GYqZfMMX"],
				'access_token':["813458922967302144-f3aEkz6OsueSD6eCkaN1yYXVcYXPGuZ","813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi","41112432-fRQMmcN5D6mSgg8kPy9oNZqDRSujUkCjAQcPgwHOb","786664983862083584-jWBk9sZ6kLSPuArjaUdOMpJbblcFxD0","781627388329398273-lrXG081wRlkvHpYAPO0iS77p3fGnijs","817489865466122240-JCAuAIB404lQZqmMMLHLP7je2QtfzlA","817492701889392644-Wji7oss1KCawoGjpGyy1KzlBHmAFCW9","817494567599611904-fYac01KBzyq6vgvMHKkb0AkVHm7SBFS","817495894312493057-ofFWm7CqEbvSPSOKNVHK66BNndGF8YR","817497484285145093-cpyWNWhMvAUkAWu4opV96hNtxMSRQ4g"],
				'access_token_secret':["OG08x1kx6rgMHwwEcmQKeeEAot88UALSQAY96XlGnpRba","VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB","FxU83OnYRfr6eU8IWuj5pP2SviFsyu2UHAaGMJqjyD6a4","in67CMCZSDrVGLiPAP0iri5sfEzqRy3qsNOplPer2C2aQ","cR71hKrAb4zZIyZqGIwDuH0HMnC1Z7BAwN7MKEfe7Uhg7","7rQV42SnR3I2S3GISugRS6a9LI5WMdymlw5iSIf6QXc6v","gxP3I5k0olOqEMSn5kynVfDuHgPNgo6ynLskobwj3P0wg","9KnAZWjg3xq2mu5q3l6Hfqj9CM3neIzOFLdB4Fnb2ZLsZ","13sJjnbfLcJZ76PxIC16bzg8GCSleImnuMRhB1D4TCf1x","PEnlovnA9927h7NUVkt0YE5aYHUJqkHtPS3bBZhjYlvvM"]}
				
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
	
key = 4
	
api = autentication(auths)

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()	