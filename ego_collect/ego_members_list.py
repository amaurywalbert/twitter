# -*- coding: latin1 -*-
################################################################################################
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, simplejson
import multi_oauth		
#Script que contém as chaves para autenticação do twitter



reload(sys)
sys.setdefaultencoding('utf-8')

##Timeline_collect - APP (por enquanto...)

################################################################################################
##		Status - Versão 1.0 - SCRIPT 01
##					1.1 - Coletar informações dos membros das listas dos egos.
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
# Armazena os objetos (list members) em formato JSON
#
################################################################################################
def save_members(obj,list_id):		#armazena uma lista com todos os membros de cada lista do twitter
	global count_members
	try:
		members_dict = {'list_id': list_id, 'users': obj, 'collected_at':datetime.datetime.now()} 		

		members_data = open(dir_data+"members_data.json",'a+')							#Arquivo para armazenar os dados
		members_data.write(json.dumps(members_dict, cls=DateTimeEncoder)+"\n")
		members_data.close()
		
		count_members +=1
		print count_members
		try:
			if count_members > count_limit:						#Salva as listas em blocos de 50.000 - evitar arquivos muito grandes.	
				agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
				shutil.move(dir_data+"members_data.json", dir_data+agora+"_members_data.json")
				count_members = 0
	
		print ("Membros da lista "+str(list_id)+" salvos com sucesso.")
		print

	except Exception as e:
		# Just print(e) is cleaner and more likely what you want, but if you insist on printing message specifically whenever possible...
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		if hasattr(e, 'message'):
			error = {'list':list_id,'reason': e.message,'date':agora}
		else:
			error = {'list':list_id,'reason': str(e),'date':agora}
		outfile = open(dir_error+"get_members_data.err", "a+") # Abre o arquivo para gravação no final do arquivo
		json.dump(error, outfile, sort_keys=True, separators=(',', ':'))
		outfile.write('\n') 
		outfile.close()
		print error

################################################################################################
#
# Obtém os membros de uma lista
#
################################################################################################

def get_members(list):
	global api
	
	print("Coletando membros da lista: "+str(list))
	list_id = long(list)
	members = []
	try:	
		for page in tweepy.Cursor(api.list_members,list_id=list_id,wait_on_rate_limit_notify=True,count=5000).pages():
			for member in page:
				members.append(member._json)
		save_members(members,list_id)

		members_downloaded = open(dir_data+"members_downloaded.txt",'a+')							#Arquivo para armazenar as listas já verificadass.
		members_downloaded.writelines(list)									# Salva o usuário no arquivo as listas já verificados.
		members_downloaded.close()

	except tweepy.RateLimitError as t:						# Verifica se o erro ocorreu por limite excedido, faz nova autenticação e chama a função novamente.
		print
		print("Erro: ",str(t),". Aguardando 02 segundos.\n")
		print		
		time.sleep(2)		
		api = autentication(auths,key)
		get_members(list)		
			

	except tweepy.error.TweepError as e: 													#Armazena todos os erros em um único arquivo.
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		outfile = open(dir_error+"members_data.err", "a+") # Abre o arquivo para gravação no final do arquivo
		if e.message:		
			error = {'list':list,'reason': e.message,'date':agora}
		else:
			error = {'list':list,'reason': str(e),'date':agora}
		json.dump(error, outline, sort_keys=True, separators=(',', ':'))
		outfile.write('\n') 
		outline.close()

		members_downloaded = open(dir_data+"members_downloaded.txt",'a+')							#Arquivo para armazenar as listas já verificadass.
		members_downloaded.writelines(list)									# Salva o usuário no arquivo as listas já verificados.
		members_downloaded.close()
				
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
	obj_data = open(dir_data+"members_data.json",'a+')							#Arquivo para armazenar os dados das listas
	obj_data.close()
	members_downloaded = open(dir_data+"members_downloaded.txt",'a+')
	members_downloaded.close()
	
	lists_collected = open(dir_data+"lists_collected.txt",'r') 							#Arquivo com as listas coletadas
	eof = False
	while not eof:																					#Enquanto não for final do arquivo
		list = lists_collected.readline()													#Leia o id da lista		
		if (list == ''):																		#Se id for igual a vazio é porque chegou ao final do arquivo.
				eof = True
		else:
			members_downloaded = open(dir_data+"members_downloaded.txt",'r')
			if check(list,members_downloaded):													#testa se a lista já foi verificada, consultando o arquivo correspondente.
				print ("Lista: "+str(list)+" já verificada. Continuando...")
				print
			else:
				print
				print("####################################################################################################")			
				get_members(list)																#Inicia função de busca das listas e coleta dos membros
				print("####################################################################################################")
			members_downloaded.close()
	lists_collected.close()

	agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
	shutil.move(dir_data+"members_data.json", dir_data+agora+"_members_data.json")

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

count_members = 0
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