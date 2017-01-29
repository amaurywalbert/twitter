# -*- coding: latin1 -*-
################################################################################################
# Script para coletar egos do Twitter:
#	Mínimo de 2 listas
#	Mínimo de 5 membros em cada lista	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, simplejson
import multi_oauth		
#Script que contém as chaves para autenticação do twitter



reload(sys)
sys.setdefaultencoding('utf-8')


##Timeline_collect - APP (por enquanto...)

################################################################################################
##		Status - Versão 9.0 - SCRIPT 01
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
##					8.1.6 - OK - Gerenciador de chaves usando tweepy e gerenciador de chaves multi_oauth.
##
##					8.1.7 - OK - Coletar até 1,5 milhões de seeds para cada script
##					8.1.8 - OK - Espera por 2 segundos antes de trocar de chave
##
##					9.1 - OK - Tratar mensagens de erros - Adiciona uma condição para tratar as exceções.
##					9.2 - STATUS - TESTE - Modificações para deixar o código legígel:
##									- Adicionar variával para guardar o local de armazenamento dos arquivos - facilita a alteração em caso de cópias dos scripts rodando simultaneamente
##
##						STATUS - TESTE - Salvar arquivos JSON com informações das listas e dos egos. - Não realizado  
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
				users_collected = open(dir_data+"users_collected.txt", 'r')											# Arquivo com os seeds (membros das listas selecionadas serão adicionados ao final do arquivo user collect para continuar o processo de busca
				if check(member.id,users_collected):								#Verifica se o usuário já foi adicionado no arquivo de membros coletados.
					print (str(member.id)+" já adicionado! Continuando...")
				else:					
					members.append(str(member.id)+"\n")
				users_collected.close()
		members_file = open(dir_data+"users_collected.txt", 'a+')
		members_file.writelines(members) 												# Salvando os membros adicionados
		members_file.close()


	except tweepy.RateLimitError as t:						# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando 02 segundos.\n")
		print		
		time.sleep(2)		
		api = autentication(auths)
		members_lists(list_id)		
			

	except tweepy.error.TweepError as e: 													#Armazena todos os erros em um único arquivo.
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		members_lists_err = open(dir_error+"members_list.json", "a+") # Abre o arquivo para gravação no final do arquivo
		if e.message:		
			error = {'list':list_id,'reason': e.message,'date':agora}
		else:
			error = {'list':list_id,'reason': str(e),'date':agora}
		json.dump(error, members_lists_err, indent=4, sort_keys=True, separators=(',', ':')) 
		members_lists_err.close()
		print error
		
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
			
			lists_collect = open(dir_data+"lists_collect.txt", 'a+')						# Arquivo com os ids das listas com o mínimo exigido
			lists_id = open(dir_data+"lists_collect.txt", 'r')						# Arquivo com os ids das listas com o mínimo exigido
					
			for list in lists:
				if check(list.id,lists_id):													#Verifica se a lista já foi adicionada no arquivo de listas.
					print ("Lista "+str(list.id)+" já adicionada! Continuando...")
				else:
					users_collected = open(dir_data+"users_collected.txt", 'r') # Arquivo com os seeds (membros das listas selecionadas serão adicionados ao final do arquivo user collect para)
					file = users_collected.readlines()
					if (len(file) < seeds_limit):	#Crescer a lista de seeds até esse limit
						members_lists(list.id)				#Função para recuperar os membros da lista
					else:
						print ("Limite de membros atingido!"+str(len(file)))
					users_collected.close()
					
					lists_collect.writelines(str(list.id)+"\n") 									# Salva o id da lista no arquivo de listas
					print ("Lista "+str(list.id)+" salva com sucesso.")
			
			lists_id.close()
			lists_collect.close()
			
			
			ego_list = open(dir_data+"ego_list.txt",'a+') 										#Lista de egos
			ego_list.writelines(str(user))														# Salva o id do usuário no arquivo de Egos coletados
			print ("Ego salvo com sucesso: "+str(user))		
			ego_list.close()
		
		users_verified = open(dir_data+"users_verified.txt",'a+')							#Arquivo para armazenar a lista de usuários já verificados.
		users_verified.writelines(user)									# Salva o usuário no arquivo de users já verificados.
		users_verified.close()	




	except tweepy.RateLimitError as t:						# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando 02 segundos.\n")
		print
		time.sleep(2)		
		api = autentication(auths)
		search_lists(user)			

	
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		
		lists_err = open(dir_error+"lists_err.json", "a+") # Abre o arquivo para gravação no final do arquivo
 
#		data = {'key': 'value', 'whatever': [1, 42, 3.141, 1337]}
		if e.message:		
			error = {'user':user,'reason': e.message,'date':agora}
		else:
			error = {'user':user,'reason': str(e),'date':agora}
		json.dump(error, lists_err, indent=4, sort_keys=True, separators=(',', ':')) 
				
		lists_err.close()
		print error
#		print("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		users_verified = open(dir_data+"users_verified.txt",'a+')							#Arquivo para armazenar a lista de usuários já verificados.
		users_verified.writelines(user)									# Salva o usuário no arquivo de users já verificados.
		users_verified.close()	


##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():

	users_verified = open(dir_data+"users_verified.txt",'a+')							#Arquivo para armazenar a lista de usuários já verificados.
	users_verified.close()
	users_collected = open(dir_data+"users_collected.txt",'r') 							#Testando com o id do user
	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		account = users_collected.readline()													#Leia scren_name do usuário corrente		
		if (account == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
				eof = True
				#break
		else:
			users_verified = open(dir_data+"users_verified.txt",'r')							#Arquivo para armazenar a lista de usuários já verificados.
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

dir_data = "/home/amaury/coleta/ego_collection/data/"
#dir_data = "/home/amaury/coleta/ego_collection2/data/"				# SCRIPT 2

dir_error = "/home/amaury/coleta/ego_collection/error/"
#dir_error = "/home/amaury/coleta/ego_collection2/error/"			# SCRIPT 2

if not os.path.exists(dir_data):
	os.makedirs(dir_data)

if not os.path.exists(dir_error):
	os.makedirs(dir_error)

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
key = -1					###### Essas duas linhas atribuem as chaves para cada script
key_init = 0
key_limit = len(auths)	###### Usa todas as chaves
#seeds_limit = 3000000
###################################################################################################
############################ PARA USAR COM VÀRIAS CÓPIAS DO SCRIPTS RODANDO SIMULTANEAMENTE########
###################################################################################################
#key = -1					###### Essas linhas atribuem as chaves para cada script		------- SCRIPT 1
#key = 4					###### 																	   ------- SCRIPT 2

#key_init = 0			######																		------- SCRIPT 1			
#key_init = 5			######																		------- SCRIPT 2

#key_limit = 5			###### Usa as primeiras chaves do gerenciador de chaves		------- SCRIPT 1
#key_limit = 10		###### Usa as últimas chaves do gerenciador de chaves    	------- SCRIPT 2

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