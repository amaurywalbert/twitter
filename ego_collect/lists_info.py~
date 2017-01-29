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
##		Status - Versão 1.0
##					1.1 - Coletar informações das listas dos egos.
##
##					STATUS - TESTE - Salvar arquivos JSON com informações das listas e dos egos.  
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
	if (key >= key_limit):
		key = key_init
	print ("Autenticando usando chave número: "+str(key))
	api_key = tweepy.API(auths[key])
	return (api_key)


################################################################################################
#
# Testa se lista já foi adicionada ao arquivo correspondente.
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
def save_list(list):
	global count_list
	try:
		list_dict = {'subscriber_count': list.subscriber_count, 'member_count': list.member_count, 'name': list.name, 
			'created_at': list.created_at, 'uri': list.uri, 'mode': list.mode, 'id_str': list.id_str,
			'id': list.id, 'user': list.user._json, 'full_name': list.full_name, 'following': list.following,
			'slug': list.slug, 'description': list.description} 		

		lists_data = open(dir_data+"lists_data.json",'a+')							#Arquivo para armazenar os dados das listas
		lists_data.write(json.dumps(list_dict, cls=DateTimeEncoder)+"\n")
		lists_data.close()
		
		count_list +=1
		print count_list
		try:
			if count_list > count_limit:						#Salva as listas em blocos de 50.000 - evitar arquivos muito grandes.	
				agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
				shutil.move(dir_data+"lists_data.json", dir_data+agora+"_lists_data.json")
				count_list = 0
		except Exception as e:
			print e			
			
		print ("Lista "+str(list.id)+" salva com sucesso.")
		print
		
	except Exception as e:
		# Just print(e) is cleaner and more likely what you want, but if you insist on printing message specifically whenever possible...
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		if hasattr(e, 'message'):
			error = {'list':list.id,'reason': e.message,'date':agora}
		else:
			error = {'list':list.id,'reason': str(e),'date':agora}
		outfile = open(dir_error+"get_lists_data.err", "a+") # Abre o arquivo para gravação no final do arquivo
		json.dump(error, outfile, sort_keys=True, separators=(',', ':'))
		outfile.write('\n')  
		outfile.close()
		print error 			

################################################################################################
#
# Obtem dados das listas
#
################################################################################################

def get_lists_data(list):
	global api
	
	print("Coletando dados da lista: "+str(list))
	list_id = long(list)
	
	try:
		list_downloaded =  api.get_list(list_id=list_id)			#Coleta as listas da API do Twitter
		save_list(list_downloaded)											#FUnção para salvar as listas em formato JSON
		
		lists_downloaded = open(dir_data+"lists_downloaded.txt",'a+')							#Arquivo para armazenar as listas já verificadass.
		lists_downloaded.writelines(list)									# Salva o usuário no arquivo as listas já verificados.
		lists_downloaded.close()

	except tweepy.RateLimitError as t:									#Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando 02 segundos.\n")
		print
		time.sleep(2)		
		api = autentication(auths)
		get_lists_data(list)			

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto		
		outfile = open(dir_error+"list_down.err", "a+")			 #Abre o arquivo para gravação no final do arquivo

		if e.message:		
			error = {'list_id':list,'reason': e.message,'date':agora}
		else:
			error = {'list_id':list,'reason': str(e),'date':agora}
		
		json.dump(error, outfile, sort_keys=True, separators=(',', ':'))
		outfile.write('\n') 
		outfile.close()

		lists_downloaded = open(dir_data+"lists_downloaded.txt",'a+')							#Arquivo para armazenar as listas já verificadass.
		lists_downloaded.writelines(list)									# Salva o usuário no arquivo as listas já verificados.
		lists_downloaded.close()
				
		print error


##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	lists_data = open(dir_data+"lists_data.json",'a+')							#Arquivo para armazenar os dados das listas
	lists_data.close()
	lists_downloaded = open(dir_data+"lists_downloaded.txt",'a+')							#Arquivo para armazenar a lista de usuários já verificados.
	lists_downloaded.close()
	
	lists_collected = open(dir_data+"lists_collected.txt",'r') 							#Arquivo com as listas coletadas
	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		list = lists_collected.readline()													#Leia o id da lista		
		if (list == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
				eof = True
		else:
			lists_downloaded = open(dir_data+"lists_downloaded.txt",'r')							#Arquivo para armazenar a lista de usuários já verificados.
			if check(list,lists_downloaded):													#testa se a lista já foi verificada, consultando o arquivo correspondente.
				print ("Lista: "+str(list)+" já verificada. Continuando...")
				print
			else:
				print
				print("####################################################################################################")			
				get_lists_data(list)																#Inicia função de busca das listas e coleta dos membros
				print("####################################################################################################")
			lists_downloaded.close()
	lists_collected.close()
	print	
	print("Coleta finalizada!")
	
################################################################################################
#
# INICIO DO PROGRAMA
#
################################################################################################

dir_data = "/home/amaury/coleta/ego_collection/data/"
dir_error = "/home/amaury/coleta/ego_collection/error/"


oauth_keys = multi_oauth.keys()

count_list = 0	#Número de listas salvas
count_limit = 49999
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

try:
	api = autentication(auths)
	print
	print("####################################################################################################")
	print
except tweepy.error.TweepError as e:
	print("[ERRRO] Não foi possível realizar autenticação. Erro: ",str(e),".\n")
	
# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()	