# -*- coding: latin1 -*-
################################################################################################
# Script para coletar inscritos em listas dos egos
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 2.0 - Coletar Inscritos das listas dos Egos
##						
##						2.1 - Uso do Tweepy para controlar as autenticações...
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos binários contendo os ids dos inscritos de cada lista.
##						STATUS - Refazer a coleta até que não tenha nenhuma mensagem de "Rate Limit Exceeded"  - A cada mensagem há uma lista que ficou sem ser coletada
##
## 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Realiza autenticação da aplicação.
#
######################################################################################################################################################################

def autentication(auths):
	global key
	key += 1
	if (key >= key_limit):
		key = key_init
	print
	print("######################################################################")
	print ("Autenticando usando chave número: "+str(key)+"/"+str(key_limit))
	print("######################################################################\n")
	time.sleep(wait)
	api_key = tweepy.API(auths[key])
	return (api_key)

######################################################################################################################################################################
#
# Converte formato data para armazenar em formato JSON
#
######################################################################################################################################################################
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object


################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		subscribers_file = []
		while f.tell() < tamanho:
			buffer = f.read(list_struct.size)
			subs = list_struct.unpack(buffer)
			subscribers_file.append(subs[0])
	return subscribers_file

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a lista de amigos de um usuário específico 
#
######################################################################################################################################################################
def get_subscribers(list):												#Coleta dos inscritos de uma lista específica
	global key
	global dictionary
	global api
	global i
	
	try:
		subscribers_list = []
		for page in tweepy.Cursor(api.list_subscribers,list_id=list,include_entities=False,skip_status=True,wait_on_rate_limit_notify=True,count=5000).pages():
			for subs in page:
				subscribers_list.append(subs.id)
		return (subscribers_list)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. Lista: "+str(list)+" - Autenticando novamente... "+str(e))
			api = autentication(auths)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"subscribers_lists_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
			if e.message:
				error = {'list':list,'reason': e.message,'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'list':list,'reason': str(e),'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
		try:
			if e.message[0]['code'] == 32 or e.message[0]['code'] == 215:
				key = random.randint(key_init,key_limit)
				api = autentication(auths)
			if e.message[0]['code'] == 34:									# Listas não existentes
				dictionary[list] = list											# Insere a lista coletada na tabela em memória
				with open(data_dir+str(list)+".dat", "w+b") as f:		# Cria arquivo vazio	
					print ("Lista inexistente. List: "+str(list)+" - Arquivo criado com sucesso!")
				i +=1
		except Exception as e2:
			print ("E2: "+str(e2))
		
		try:
			if e.message == 'Not authorized.': # Usuários não autorizados
				dictionary[list] = list											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(list)+".dat", "w+b") as f:		# Cria arquivo vazio
					print ("Lista não autorizada. List: "+str(list)+" - Arquivo criado com sucesso!")
				i +=1	
		except Exception as e3:
			print ("E3: "+str(e3))
######################################################################################################################################################################
#
# Obtem inscritos nas listas dos egos
#
######################################################################################################################################################################
def save_subscribers(j,k,list): # j = número do ego que está sendo coletado - k = número da lista que esta sendo coletada
	global i	# numero de listas com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de amigos do usuário
	
	subscribers_list = get_subscribers(list)
	if subscribers_list:	
		try:
			with open(data_dir+str(list)+".dat", "w+b") as f:	
				for subs in subscribers_list:
					f.write(list_struct.pack(subs))						# Grava os ids dos amigos no arquivo binário do usuário
				dictionary[list] = list											# Insere o usuário coletado na tabela em memória
				i +=1
				print ("User nº "+str(j)+ " - Lista nº "+str(k)+": "+str(list)+" coletada com sucesso. Total coletadas: "+str(i))
	
		except Exception as e:	
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(error_dir+"subscribers_list_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
				if e.message:		
					error = {'list':list,'reason': e.message,'date':agora}
				else:
					error = {'list':list,'reason': str(e),'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			if os.path.exists(data_dir+str(list)+".dat"):
				os.remove(data_dir+str(list)+".dat")

######################################################################################################################################################################
#
# Obtem as listas já coletadas do ego
#
######################################################################################################################################################################
def get_lists(ego):
	egos_lists = []
	eof = False
	with open(lists_ego, 'r') as lists_file:
		while not eof:																			# Enquanto não for final do arquivo
			user_lists = lists_file.readline()											# Leia o id da lista
			if (user_lists == ''):															# Se id for igual a vazio é porque chegou ao final do arquivo.
					eof = True
			else:
				lists = json.loads(user_lists)
				if ego == long(lists['user']):
					print "Ego encontrado! Localizando listas..."
					for list in lists['owner']:
						egos_lists.append(list['id'])
					for list in lists['subscriptions']:
						egos_lists.append(list['id'])
					eof = True				
	return egos_lists
	
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos inscritos de cada lista especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	j = 0																	# Exibe o número ordinal da lista que está sendo usada para a coleta dos membros
	for file in os.listdir(egos_friends_dir):					# Verifica a lista de egos coletados e para cada um, busca os amigos dos alters listados no arquivo do ego.
		k = 0																# Exibe o número ordinal do alter que está sendo coletado a lista de amigos
		j+=1 
		ego = file.split(".dat")
		ego = long(ego[0])
		egos_lists = get_lists(ego)
		if egos_lists:
			for list in egos_lists:
				k+=1
				list = long(list)
				if not dictionary.has_key(list):
					save_subscribers(j, k, list)																#Inicia função de busca das listas e coleta dos membros
	
	#As próximas linhas são usadas para imprimir o conteúdo dos arquivos, possibilitando a verificação de inconsistências.
	with open("/home/amaury/coleta/lists_info/subscribers_lists_collected/lists_subscribers.json", 'w') as f:
		print
		print("######################################################################")		
		print ("Criando arquivo com resumo da coleta...")	
		for file in os.listdir(data_dir):
			list_id = file.split(".dat")
			list_id = long(list_id[0])
			list_file = read_arq_bin(data_dir+file)
			qtde_subscribers = len(list_file)
			subscribers = {'list':list_id,'subscribers': qtde_subscribers}
			f.write(json.dumps(subscribers, separators=(',', ':'))+"\n")
		print ("Arquivo criado com sucesso: /home/amaury/coleta/lists_info/subscribers_lists_collected/lists_subscribers.json" )
		print("######################################################################\n")
	print
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### DEFINIR SE É TESTE OU NÃO!!! ### ['auths_ok'] OU  ['auths_test'] ################				
oauth_keys = multi_oauth.keys()
auths = oauth_keys['auths_test']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

key_init = 0					#################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		#################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ###################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves

lists_ego = "/home/amaury/coleta/ego_lists_collected/data/201701300152_ego_lists_overview.json"

egos_friends_dir = "/home/amaury/coleta/n1/egos_friends/50/bin/"################## Arquivo contendo a lista dos usuários ego já coletados


lists_collected = "/home/amaury/coleta/ego_collection/data/lists_collect.txt"## Arquivo contendo as listas coletadas
data_dir = "/home/amaury/coleta/lists_info/subscribers_lists_collected/bin/" ## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/lists_info/subscribers_lists_collected/error/" # Diretório para armazenamento dos arquivos de erro
formato = 'l'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
list_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
wait = 5
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
######################################################################################################################
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)

###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(data_dir):
	list_id = file.split(".dat")
	list_id = long(list_id[0])
	dictionary[list_id] = list_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
#Autenticação
api = autentication(auths)

	
#Executa o método main
if __name__ == "__main__": main()