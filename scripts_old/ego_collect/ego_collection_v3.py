### -*- coding: latin1 -*-
################################################################################################
# Script para coletar egos do Twitter:
#	Mínimo de 2 listas
#	Mínimo de 5 membros em cada lista	
#
import tweepy, datetime, sys, time, json, os.path, shutil

##Timeline_collect - APP (por enquanto...)

##amaurywalbert@live.com
##walbert1810


################################################################################################
##		Status - OK - Salvando em String
##					OK	- Coletando todas as litas - adicionado Método API.Cursor
##					OK - Considerando o mínimo de 1 lista por usuário
##					OK - Verificando por limites usando apenas o Tweepy
##					Teste - Remover informações completas das listas. Adicionar apenas o necessário para a coleta dos egos:
##							- Listas com pelo menos 5 membros;
##							- Users com no mínimo 01 lista (inscrito ou dono);
##							- Coleta snowball a partir de seeds iniciais e crescendo com a análise dos membros das listas selecionadas. Busca em largura.
##
##					Error - Capurando informações incorretas... abortando.
##
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
# Obtem os membros de uma lista
#
################################################################################################

def members_lists(list_id,members_file):	
	print("Recuperando membros da lista: "+str(list))
	print
	
	members = [] #Inicializando arrays
	try:	
		for page in tweepy.Cursor(api.list_members,list_id=list_id,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=5000).pages():
			for member in page:
				if check(member.screen_name,members_file):	#Verifica se o usuário já foi adicionado no arquivo de membros coletados.
					print (str(member.screen_name)+" já adicionado! Continuando...")
				else:					
					members.append(str(member.screen_name)+"\n")
					print(member.screen_name)

		if (len(members) > 0):
			members_file.writelines(members) # Salvando os membros adicionados
			
			
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		members_lists_err = open("error/"+str(list_id)+"_members_list_"+str(agora)+".subs_lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		members_lists_err.writelines("[ERRRO] Não foi possível recuperar membros da lista: "+str(list_id)+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		members_lists_err.close()
		print("[ERRRO] Não foi possível recuperar membros da lista: "+str(list_id)+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
		
				
################################################################################################
#
# Obtem as listas de subscrições de um usuário específico
#
################################################################################################

def search_lists(user,metodo):
	count = 0
	try:
		members_file = open("data/users_collect.txt", 'a+')	# Arquivo com a lista dos membros das listas
		lists_file = open("data/lists_collect.txt", 'a+')	# Arquivo com os ids das listas com o mínimo exigido
		lists_info = open("data/lists_info.txt", 'a+')	# Arquivo com informações das listas salvas
		
		for page in tweepy.Cursor(metodo,id=user,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,count=1000).pages():						

			for list in page:
				print("id="+str(list.id)+" - member_count="+str(list.member_count)+" - name="+unicode(list.name))			# Na tela, imprime o resumo de cada lista...												

				if (list.member_count >= 5):	#Testa se a quantidade de membros da lista atinge o limite mínimo.
					print ("Lista com mínimo de membros necessários: "+str(list.member_count))
					
					if check(list.id,lists_file):	#Verifica se a lista já foi adicionada no arquivo de listas.
						print "Lista já adicionada! Continuando..."

					else:
						list_info = []			
						list_info.append("id ="+str(list.id))
						list_info.append("members = "+str(list.member_count))
						list_info.append("created_at = "+str(list.created_at))
						list_info.append("user = "+str(list.user))						
						list_info.append("name = "+unicode(list.name))
						lists_file.writelines(str(list.id)+"\n") # Salva o id da lista no arquivo de listas
						lists_info.writelines(str(list_info)+"\n") # Salva o informações da lista no arquivo .info

						print ("Lista salva com sucesso.")
						
						count = count+1
						
						members_lists(list.id,members_file)	#Função para recuperar os membros da lista
				else:

					print ("Lista não atende requisito mínimo: "+str(list.member_count))


		members_file.close()	#Fecha o arquivo para salvar os dados com segurança...
		lists_file.close()
		lists_info.close()
		
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		subs_lists_err = open("error/"+user+"_lists_collect_"+str(agora)+".subs_lists_err", "a+") # Abre o arquivo para gravação no final do arquivo
		subs_lists_err.writelines("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: "+str(e)+". Vou ignorar e tocar adiante.\n")
		subs_lists_err.close()
		print("[ERRRO] Não foi possível recuperar as listas de: "+user+". Erro: ",str(e),". Vou ignorar e tocar adiante.\n")
	
	return(count)

##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	try:	
		shutil.copyfile('data/seeds_iniciais.ini', 'data/users_collect.txt') # Faz backup do arquivo com os seeds iniciais. Os seeds precisam ser ego quanto às restrições necessárias.
		users_collect = open('data/users_collect.txt','a+') #Deve ser o screen_name
		ego_list = open('data/ego_list.txt','a+') #Deve ser o screen_name
	except IOError as e:
		print("Não foi possível preparar o arquivo com os seeds. Erro: "+str(e))
	
	eof = False

	while not eof:
		account = users_collect.readline()
				
		print		
		print("Coletando listas do usuário: "+str(account))
		owner = search_lists(account,api.lists_subscriptions)
		subs = search_lists(account,api.get_lists_ownerships)
		lists = owner + subs
		if (lists >1):
			ego_list.writelines(str(account)+"\n") # Salva o screen_name do usuário no arquivo de Egos coletados
		print("####################################################################################################")

		if (account == ''):
			eof = True
	
	users_collect.close()
	ego_list.close()
	
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