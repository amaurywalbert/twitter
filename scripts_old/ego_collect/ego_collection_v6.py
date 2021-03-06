# -*- coding: latin1 -*-
################################################################################################
# Script para coletar egos do Twitter:
#	Mínimo de 2 listas
#	Mínimo de 5 membros em cada lista	
#
import tweepy, datetime, sys, time, json, os.path, shutil, time
import simplejson as json

reload(sys)
sys.setdefaultencoding('utf-8')


##Timeline_collect - APP (por enquanto...)

##amaurywalbert@live.com
##walbert1810


################################################################################################
##		Nota - As listas estão sendo salvas em um formato estruturado. É possível ler o conteudo de cada campo lendo o arquivo e acessando list.campo. Ex. list.id, list.name
################################################################################################

################################################################################################
##		Status - OK - Salvando em String
##					OK	- Coletando todas as litas - adicionado Método API.Cursor
##					OK - Verificando por limites usando apenas o Tweepy
##					OK - Adicionar apenas o necessário para a coleta dos egos:
##							- Listas com pelo menos 5 membros;
##							- Users com no mínimo 01 lista (inscrito ou dono);
##							- Coleta snowball de egos a partir de seeds iniciais e crescendo com a análise dos membros das listas selecionadas.
##
##					OK - Armazenamento dos ids das listas...
##					OK - verificando pelo id dos users...	
##					
##					Teste - Verificar se as listas armazenadas conseguem ser lidas e as informações extraídas posteriormente - Testando armazenar arquivos no formato JSON
## 
################################################################################################

################################################################################################
#
# Testa se lista ou usuário já foi adicionada(o) ao arquivo correspondente.
#
################################################################################################
		
def check(search,datafile):
	file = datafile.readlines()
#	print ("Arquivo:"+str(datafile))
#	print file
	found = False
#	print ("Procurando por: ")
#	print search
	for line in file:
#		print ("Comparando com:")		
#		print line
#		time.sleep(20)
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
	print("Coletando membros da lista: "+str(list_id))
	try:
		members = []																				 	#Inicializando arrays	
		for page in tweepy.Cursor(api.list_members,list_id=list_id,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=5000).pages():
			for member in page:
				users_collected = open("data/users_collected.txt", 'r')											# Arquivo com os seeds (membros das listas selecionadas serão adicionados ao final do arquivo user collect para continuar o processo de busca
				if check(member.id,users_collected):								#Verifica se o usuário já foi adicionado no arquivo de membros coletados.
					print (str(member.id)+" já adicionado! Continuando...")
				else:					
					members.append(str(member.id)+"\n")
				users_collected.close()
		members_file = open("data/users_collected.txt", 'a+')
		members_file.writelines(members) 												# Salvando os membros adicionados
		members_file.close()

			
	except tweepy.error.TweepError as e: 													#Armazena todos os erros em um único arquivo.
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		members_lists_err = open("error/members_list.lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		members_lists_err.writelines(str(agora)+" - list_id: "+str(list_id)+". Erro: "+str(e)+"\n")
		members_lists_err.close()
		print("[ERRRO] Não foi possível recuperar membros da lista: "+str(list_id)+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		
	
		
################################################################################################
#
# Obtem as listas de um usuário específico (owner+subscription)
#
################################################################################################

def search_lists(user):
	print("Coletando listas do usuário: "+str(user))	
	lists = []
	try:
		for page in tweepy.Cursor(api.get_lists_ownerships,id=user,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=1000,parser=tweepy.parsers.JSONParser()).pages():
			print page.get("lists")
			#print list
			#print page
			print
			#print page.keys()
			print
			#lists_json = [json.dumps(json_obj) for json_obj in page]
			#print lists_json
			time.sleep(5)



#				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
#					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
#					lists.append(list)
#				else:
#					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+". Não atende requisito mínimo. Continuando...")

#		for page in tweepy.Cursor(api.lists_subscriptions,id=user,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=1000).pages():
#			for list in page:
#				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
#					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
#					lists.append(list)
#				else:
#					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+". Não atende requisito mínimo. Continuando...")
#
#		if (len(lists) > 1):
#			
#			lists_collect = open("data/lists_collect.txt", 'a+')						# Arquivo com os ids das listas com o mínimo exigido
#			lists_info = open("data/lists_info.json", 'a+')							# Arquivo com informações das listas salvas
#			lists_id = open("data/lists_collect.txt", 'r')						# Arquivo com os ids das listas com o mínimo exigido
#					
#			for list in lists:
#				if check(list.id,lists_id):													#Verifica se a lista já foi adicionada no arquivo de listas.
#					print ("Lista "+str(list.id)+" já adicionada! Continuando...")
#				else:
#					members_lists(list.id)														#Função para recuperar os membros da lista
#					lists_collect.writelines(str(list.id)+"\n") 								# Salva o id da lista no arquivo de listas
##					lists_info.writelines(str(lists)+"\n") 										# Salva o informações da lista no arquivo
#					print ("Lista "+str(list.id)+" salva com sucesso.")
#			
#			lists_id.close()
#			lists_info.close()			
#			lists_collect.close()
#			
#			
#			ego_list = open('data/ego_list.txt','a+') 										#Lista de egos
#			ego_list.writelines(str(user))														# Salva o id do usuário no arquivo de Egos coletados
#			print ("Ego salvo com sucesso: "+str(user))		
#			ego_list.close()
#		
#		users_verified = open('data/users_verified.txt','a+')							#Arquivo para armazenar a lista de usuários já verificados.
#		users_verified.writelines(user)									# Salva o usuário no arquivo de users já verificados.
#		users_verified.close()	
	
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		lists_err = open("error/lists_collect.lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
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
	#users_verified = open('data/users_verified.txt','a+')							#Arquivo para armazenar a lista de usuários já verificados.
	#users_verified.close()
	users_collected = open('data/users_collected.txt','r') 							#Testando com o id do user
	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		account = users_collected.readline()													#Leia scren_name do usuário corrente		
		if (account == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
				eof = True
				#break
		else:
			
			users_verified = open('data/users_verified.txt','r')							#Arquivo para armazenar a lista de usuários já verificados.
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
	
print ("Autenticando usando chave número: "+str(2))

api = tweepy.API(auths[0],wait_on_rate_limit=True)

print ("Autenticação Realizada!\n")


# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()