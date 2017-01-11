# -*- coding: latin1 -*-
################################################################################################
# Script para coletar egos do Twitter:
#	Mínimo de 2 listas
#	Mínimo de 5 membros em cada lista	
#
import tweepy, datetime, sys, time, json, os.path, shutil, time
import multi_oauth		
#Script que contém as chaves para autenticação do twitter



reload(sys)
sys.setdefaultencoding('utf-8')


##Timeline_collect - APP (por enquanto...)

################################################################################################
##		Status - Versão 8.0 - SCRIPT 02
##
##					8.1.1 - OK	- Coletando todas as litas - adicionado Método API.Cursor
##					8.1.2 - OK - Verificando por limites usando apenas o Tweepy
##					8.1.3 - OK - Adicionar apenas o necessário para a coleta dos egos:
##						8.1.3.1 - - Listas com pelo menos 5 membros;
##						8.1.3.2 - - Users com no mínimo 02 lista (inscrito ou dono);
##						8.1.3.3 - - Coleta snowball de egos a partir de seeds iniciais e crescendo com a análise dos membros das listas selecionadas.
##
##					8.1.4 - OK - Armazenamento dos ids das listas...
##					8.1.5 - OK - verificando pelo id dos users...
##
##					8.1.6 - OK - Gerenciador de chaves usando tweepy e gerenciador de chaves multi_oauth - Usando chaves 0 a 4 - outro script tá usando 5 a 9.
##
##					8.1.7 - Status - TESTE - Coletar até 1,5 milhões de seeds para cada script
##								Status - TESTE - Arquivo vai crescer muito... 
##
## 
################################################################################################

################################################################################################
#
# Realiza autenticação da aplicação.
#
################################################################################################

def autentication(auths):
# Usando as primeiras chaves de cada conta do conjunto disponível no EverNote. Total de 10 contas:
	global key
	key += 1
	if (key >= key_limit):
		key = key_init

	print ("Autenticando usando chave número: "+str(key))

	api_key = tweepy.API(auths[key])
	
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
					users_collected = open("/home/amaury/coleta/ego_collection2/data/users_collected.txt", 'r') # Arquivo com os seeds (membros das listas selecionadas serão adicionados ao final do arquivo user collect para)
					if (len(users_collected) < seeds_limit):
						members_lists(list.id)				#Função para recuperar os membros da lista
					else:
						print ("Limite de membros atingido!"+str(len(users_collected)))
					users_collected.close()
					
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

oauth_keys = multi_oauth.keys()

################################### DEFINIR SE É TESTE OU NÃO!!! ###############################
################################################################################################									
auths = oauth_keys['auths_ok']
#USAGE  -- auths = oauth_keys['auths_ok']
#USAGE  -- auths = oauth_keys['auths_test']
################################################################################################

###################################################################################################
############################ PARA USAR COM VÀRIAS APENAS UM SCRIPT RODANDO ########################
###################################################################################################
#key = -1					###### Essas duas linhas atribuem as chaves para cada script
#key_init = 0
#key_limit = len(auths)	###### Usa todas as chaves
#seeds_limit = 3000000
###################################################################################################
############################ PARA USAR COM VÀRIAS CÓPIAS DO SCRIPTS RODANDO SIMULTANEAMENTE########
###################################################################################################
#key = -1					###### Essas linhas atribuem as chaves para cada script		------- SCRIPT 1
key = 4				###### 																	   ------- SCRIPT 2

#key_init = 0			######																		------- SCRIPT 1			
key_init = 5			######																		------- SCRIPT 2

#key_limit = 5			###### Usa as primeiras chaves do gerenciador de chaves		------- SCRIPT 1
key_limit = 10		###### Usa as últimas chaves do gerenciador de chaves    	------- SCRIPT 2

seeds_limit = 1500000

try:
	api = autentication(auths)
	print
	print("####################################################################################################")
	print
except tweepy.error.TweepError as e:
	print("[ERRRO] Não foi possível realizar autenticação. Erro: ",str(e),".\n")
	
	
	
# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()	