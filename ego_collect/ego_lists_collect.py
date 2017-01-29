# -*- coding: latin1 -*-
################################################################################################
# Script para coletar egos do Twitter:
#	Recebe a lista de egos como entrada e busca pelas listas nas quais estão inscritos ou são os donos
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time
import multi_oauth		
#Script que contém as chaves para autenticação do twitter


reload(sys)
sys.setdefaultencoding('utf-8')


################################################################################################
##		Status - Versão 1
##
##					1.0 - Recebe a lista de egos como entrada e busca pelas listas nas quais estão inscritos ou são os donos
##
##						1.0.1 - OK - Salvar arquivos JSON com informações das listas e dos egos.  
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
# Converte formato data para armazenar em formato JSON
#
################################################################################################
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object


################################################################################################
#
# Armazena os objetos (lista) em formato JSON
#
################################################################################################
def save_list(list,ego):
	global count_list
	try:
		list_dictionary = {'ego_id':ego, 'subscriber_count': list.subscriber_count, 'member_count': list.member_count, 'name': list.name, 
			'created_at': list.created_at, 'uri': list.uri, 'mode': list.mode, 'id_str': list.id_str,
			'id': list.id, 'user': list.user._json, 'full_name': list.full_name, 'following': list.following,
			'slug': list.slug, 'description': list.description}
		
		lists_data = open(dir_data+"ego_lists_data.json",'a+')							#Arquivo para armazenar os dados das listas

		lists_data.write(json.dumps(list_dictionary, cls=DateTimeEncoder, sort_keys=True, separators=(',', ':'))+"\n")
		lists_data.close()		
		
		count_list +=1
		print count_list
		try:
			if count_list > count_limit:						#Salva as listas em blocos de 50.000 - evitar arquivos muito grandes.	
				agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
				shutil.move(dir_data+"ego_lists_data.json", dir_data+agora+"_ego_lists_data.json")
				count_list = 0
		except Exception as e:
			print e
			
		print ("Dados da Lista "+str(list.id)+" salvos com sucesso.")
		print
		
	except Exception as e:
		# Just print(e) is cleaner and more likely what you want, but if you insist on printing message specifically whenever possible...
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		if hasattr(e, 'message'):
			error = {'list':list.id,'reason': e.message,'date':agora}
		else:
			error = {'list':list.id,'reason': str(e),'date':agora}

		list_dictionary = {'ego_id':ego,'error': erro}
		
		outfile = open(dir_error+"ego_lists_data.err", "a+") # Abre o arquivo para gravação no final do arquivo
		json.dump(list_dictionary, outfile, sort_keys=True, separators=(',', ':'))
		outfile.write('\n')  
		outfile.close()
		print error 		
	
	return list_dictionary
					
################################################################################################
#
# Obtem as listas de um usuário específico (owner+subscription)
#
################################################################################################

def search_lists(user):
	global api
	global count_overview
	
	print("Coletando listas do usuário: "+str(user))	
	lists_own = []
	lists_subs = []
	
	lists = []

	try:
		for page in tweepy.Cursor(api.get_lists_ownerships,id=user,wait_on_rate_limit_notify=True,count=1000).pages():
			for list in page:				
				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
					lists_own.append(list)
					lists.append(list)
				else:
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+". Não atende requisito mínimo. Continuando...")
					lists_own.append(list)

		for page in tweepy.Cursor(api.lists_subscriptions,id=user,wait_on_rate_limit_notify=True,count=1000).pages():						
			for list in page:												
				if (list.member_count >= 5):													#Testa se a quantidade de membros da lista atinge o limite mínimo.
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count))
					lists_subs.append(list)
					lists.append(list)
				else:
					print ("Lista: "+str(list.id)+" - "+unicode(list.name)+" - número de membros: "+str(list.member_count)+". Não atende requisito mínimo. Continuando...")
					lists_subs.append(list)

		if (len(lists) > 1):			
			egos_statistics_own = []
			egos_statistics_subs = []
			for line in lists_own:
				egos_statistics_own.append(save_list(line,user))
			for line in lists_subs:
				egos_statistics_subs.append(save_list(line,user))
			
			ego_lists_overview = open(dir_data+"ego_lists_overview.json", "a+") # Abre o arquivo para gravação no final do arquivo
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			dictionary = {'user':user,'owner':egos_statistics_own,'subscriptions':egos_statistics_subs,'verified':agora}
			ego_lists_overview.write(json.dumps(dictionary, cls=DateTimeEncoder,sort_keys=True, separators=(',', ':'))+"\n") 		
			ego_lists_overview.close()
			
			count_overview +=1
			try:
				if count_overview > count_limit:						#Salva as listas em blocos de 50.000 - evitar arquivos muito grandes.	
					agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
					shutil.move(dir_data+"ego_lists_overview.json", dir_data+agora+"_ego_lists_overview.json")
					count_overview = 0
			except Exception as e:
				print e
			
		else:
			outfile = open(dir_error+"ego_lists.err", "a+") # Abre o arquivo para gravação no final do arquivo
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			error = {'user':user,'reason': 'Ego não atende requisito mínimo','verified':agora}
			json.dump(error, outfile, sort_keys=True, separators=(',', ':'))
			outfile.write('\n') 		
			outfile.close()
			print error 
									
		egos_verified = open(dir_data+"egos_verified.txt",'a+')							#Arquivo para armazenar a lista de usuários já verificados.
		egos_verified.writelines(user)									# Salva o usuário no arquivo de users já verificados.
		egos_verified.close()	

	except tweepy.RateLimitError as t:						# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando "+str(sleep)+" segundos.\n")
		print
		time.sleep(sleep)		
		api = autentication(auths)
		search_lists(user)			

	
	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		
		outfile = open(dir_error+"ego_lists.err", "a+") # Abre o arquivo para gravação no final do arquivo
 
		if e.message:		
			error = {'user':user,'reason': e.message,'date':agora}
		else:
			error = {'user':user,'reason': str(e),'date':agora}
		json.dump(error, outfile, sort_keys=True, separators=(',', ':'))
		outfile.write('\n') 		
		outfile.close()
		print error

		egos_verified = open(dir_data+"egos_verified.txt",'a+')							#Arquivo para armazenar a lista de usuários já verificados.
		egos_verified.writelines(user)									# Salva o usuário no arquivo de users já verificados.
		egos_verified.close()	


##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():

	egos_verified = open(dir_data+"egos_verified.txt",'a+')						#Arquivo para armazenar a lista de usuários já verificados.
	egos_verified.close()
	
	egos_collected = open(dir_data+"egos_collected.txt",'r') 						#Testando com o id do user

	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		account = egos_collected.readline()												#Leia o id do usuário corrente
		if (account == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
			eof = True
		else:
			egos_verified = open(dir_data+"egos_verified.txt",'r')					#Arquivo para armazenar a lista de usuários já verificados.
			if check(account,egos_verified):												#testa se o usuário já foi verificado, consultando o arquivo correspondente.
				print ("Usuário: "+str(account)+" Já verificado. Continuando...")
				print	
			else:
				print
				print("####################################################################################################")			
				search_lists(account)															#Inicia função de busca das listas e coleta dos membros
				print("####################################################################################################")
			egos_verified.close()
	egos_collected.close()
	
	agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
	if os.path.exists(dir_data+"ego_lists_data.json"):
		shutil.move(dir_data+"ego_lists_data.json", dir_data+agora+"_ego_lists_data.json")
	if os.path.exists(dir_data+"ego_lists_overview.json"):
		shutil.move(dir_data+"ego_lists_overview.json", dir_data+agora+"_ego_lists_overview.json")
	print
	print("Coleta finalizada!")
	
################################################################################################
#
# INICIO DO PROGRAMA
#
################################################################################################

oauth_keys = multi_oauth.keys()

################################### DEFINIR SE É TESTE OU NÃO!!! ###############################									
auths = oauth_keys['auths_ok']
sleep = 1
#USAGE  -- auths = oauth_keys['auths_ok'] - sleep = 1
#USAGE  -- auths = oauth_keys['auths_test'] - sleep = 20
################################################################################################

dir_data = "/home/amaury/coleta/ego_lists_collected/data/"  #Diretório de armazenamento dos arquivos das listas
dir_error = "/home/amaury/coleta/ego_lists_collected/error/"

count_list = 0				#Controle do tamanho de cada arquivo 
count_overview = 0				#Controle do tamanho de cada arquivo
count_limit = 19999

if not os.path.exists(dir_data):
	os.makedirs(dir_data)

if not os.path.exists(dir_error):
	os.makedirs(dir_error)


###################################################################################################
key = -1					###### Essas duas linhas atribuem as chaves para cada script
key_init = 0
key_limit = len(auths)	###### Usa todas as chaves

###################################################################################################
###################################################################################################

try:
	api = autentication(auths)
	print
	print("####################################################################################################")
	print
except tweepy.error.TweepError as e:
	print("[ERRRO] Não foi possível realizar autenticação. Erro: ",str(e),".\n")	
	
# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()	