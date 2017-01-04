# -*- coding: latin1 -*-
################################################################################################
# Script para coletar egos do Twitter:
#	Mínimo de 2 listas
#	Mínimo de 5 membros em cada lista	
#
import tweepy, datetime, sys, time, json, os.path, shutil

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
##					OK - Remover informações completas das listas. Adicionar apenas o necessário para a coleta dos egos:
##							- Listas com pelo menos 5 membros;
##							- Users com no mínimo 01 lista (inscrito ou dono);
##							- Coleta snowball de egos a partir de seeds iniciais e crescendo com a análise dos membros das listas selecionadas.
##					ERROR - Listas não estão sendo armazenadas de maneira correta. (ids))
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

################################################################################################
#
# Obtem os membros de uma lista
#
################################################################################################

def members_lists(list_id):
	members_file = open("data/users_collect.txt", 'a+')								# Arquivo com a lista dos membros das listas (serão adicionados ao final do arquivo user collect para continuar o processo de busca
	print	
	members = []																				 	#Inicializando arrays
	try:	
		for page in tweepy.Cursor(api.list_members,list_id=list_id,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=5000).pages():
			for member in page:
				if check(member.screen_name,members_file):								#Verifica se o usuário já foi adicionado no arquivo de membros coletados.
					print (str(member.screen_name)+" já adicionado! Continuando...")
				else:					
					members.append(str(member.screen_name)+"\n")
					print(member.screen_name)
			members_file.writelines(members) 												# Salvando os membros adicionados

#Colocar todos os erros num único arquivo...			
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		members_lists_err = open("error/"+str(list_id)+"_members_list_"+str(agora)+".lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		members_lists_err.writelines("[ERRRO] Não foi possível recuperar membros da lista: "+str(list_id)+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		members_lists_err.close()
		print("[ERRRO] Não foi possível recuperar membros da lista: "+str(list_id)+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		
				
################################################################################################
#
# Obtem as listas de um usuário específico (owner+subscription)
#
################################################################################################

def search_lists(user):
	lists = []
	
	try:
		ego_list = open('data/ego_list.txt','a+') 										#Lista de egos
		lists_file = open("data/lists_collect.txt", 'a+')								# Arquivo com os ids das listas com o mínimo exigido
		lists_info = open("data/lists_info.txt", 'a+')									# Arquivo com informações das listas salvas
		
		for page in tweepy.Cursor(api.get_lists_ownerships,id=user,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=1000).pages():						
			for list in page:												
				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
					lists.append(list)
				else:
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+".\nNão atende requisito mínimo. Continuando...")

		for page in tweepy.Cursor(api.lists_subscriptions,id=user,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=1000).pages():						
			for list in page:												
				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
					lists.append(list)
				else:
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+".\nNão atende requisito mínimo. Continuando...")

		if (len(lists) > 1):
#			len_list = len(lists)
#			print ("Quantidade de listas do usuário: "+str(len_list)
			ego_list.writelines(str(user))											# Salva o screen_name do usuário no arquivo de Egos coletados
			print ("Ego salvo com sucesso: "+str(user))
			
			for list in lists:
				if check(list.id,lists_file):													#Verifica se a lista já foi adicionada no arquivo de listas.
					print ("Lista "+str(list)+" já adicionada! Continuando...")

				else:
					lists_file.writelines(str(list.id)+"\n") 								# Salva o id da lista no arquivo de listas
					lists_info.writelines(str(list)+"\n") 									# Salva o informações da lista no arquivo
					print ("Lista "+str(list)+" salva com sucesso. Recuperando membros...")
					members_lists(list.id)														#Função para recuperar os membros da lista
			
		lists_file.close()
		lists_info.close()
		ego_list.close()
		
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		lists_err = open("error/"+user+"_lists_collect_"+str(agora)+".lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		lists_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
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
	try:	
		users_collect = open('data/users_collect.txt','r') 							#Deve ser o screen_name
#		ego_list = open('data/ego_list.txt','r') 											#Lista de egos
	except IOError as e:
		print("Não foi possível preparar o arquivo com os seeds. Erro: "+str(e))
	
	eof = False

	while not eof:																					#Enquanto não for final do arquivo
		account = users_collect.readline()													#Leia scren_name do usuário corrente		
	
		if (account == ''):																		#Se screen_name for igual a vazio é porque chegou ao final do arquivo.
				eof = True
				break
		else:
			users_verified = open('data/users_verified.txt','a+')							#Arquivo para armazenar a lista de usuários já verificados.			

#			if check(account,ego_list:)															#testa se o nome do usuário já está no arquivo de Egos.
#				print ("Usuário: "+str(account)+" já adicionado à lista de Egos. Continuando...")		

			if check(account,users_verified):													#testa se o usuário já foi verificado, consultando o arquivo correspondente.
				print ("Usuário: "+str(account)+"Já verificado. Continuando...")
				print	
			else:
				print
				print("####################################################################################################")			
				print("Coletando listas do usuário: "+str(account))
				search_lists(account)																#Inicia função de busca das listas e coleta dos membros
				users_verified.writelines(str(account))									# Salva o usuário no arquivo de users já verificados.
				print("####################################################################################################")
			users_verified.close()	
	
	users_collect.close()
#	ego_list.close()
	print	
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