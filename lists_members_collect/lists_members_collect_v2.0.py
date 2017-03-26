# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 2.0 - Coletar Membros das listas dos Egos
##						
##						2.1 - Uso do Tweepy para controlar as autenticações...
##
##						OBS> Twitter bloqueou diversas contas por suspeita de spam... redobrar as atenções com os scripts criados.				
##
##						STATUS - Coletando - OK - Salvar arquivos binários contendo os ids dos membros de cada lista.
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
		members_file = []
		while f.tell() < tamanho:
			buffer = f.read(list_struct.size)
			member = list_struct.unpack(buffer)
			members_file.append(member[0])
	return members_file

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a lista de amigos de um usuário específico 
#
######################################################################################################################################################################
def get_members(list):												#Coleta dos membros de uma lista específica
	global key
	global dictionary
	global api
	global i
	
	try:
		members_list = []
		for page in tweepy.Cursor(api.list_members,list_id=list,include_entities=False,skip_status=True,wait_on_rate_limit_notify=True,count=5000).pages():
			for member in page:
				members_list.append(member.id)
		return (members_list)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso à API excedido. Lista: "+str(list)+" - Autenticando novamente... "+str(e))
			api = autentication(auths)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"members_lists_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
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
# Obtem as amigos do ego
#
######################################################################################################################################################################
def save_members(j,list): # j = número da que esta sendo coletada
	global i	# numero de listas com arquivos já coletados / Numero de arquivos no diretório
	 
	# Dicionário - Tabela Hash contendo os usuários já coletados
	global dictionary

	#Chama a função e recebe como retorno a lista de amigos do usuário
	
	members_list = get_members(list)
	if members_list:	
		try:
			with open(data_dir+str(list)+".dat", "w+b") as f:	
				for member in members_list:
					f.write(list_struct.pack(member))						# Grava os ids dos amigos no arquivo binário do usuário
				dictionary[list] = list											# Insere o usuário coletado na tabela em memória
				i +=1
				print ("Lista nº "+str(j)+": "+str(list)+" coletada com sucesso. Total coletadas: "+str(i))
	
		except Exception as e:	
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(error_dir+"members_list_collect.err", "a+") as outfile:								# Abre o arquivo para gravação no final do arquivo
				if e.message:		
					error = {'list':list,'reason': e.message,'date':agora}
				else:
					error = {'list':list,'reason': str(e),'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			if os.path.exists(data_dir+str(list)+".dat"):
				os.remove(data_dir+str(list)+".dat")


######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos membros de cada lista especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	j = 0																	#Exibe o número ordinal da lista que está sendo usada para a coleta dos membros
	eof = False
	with open(lists_collected, 'r') as lists_file:
		while not eof:																			#Enquanto não for final do arquivo
			j+=1
			list = lists_file.readline()													#Leia o id da lista
			if (list == ''):																	#Se id for igual a vazio é porque chegou ao final do arquivo.
					eof = True
			else:
				list = long(list)
				if not dictionary.has_key(list):
					save_members(j, list)																#Inicia função de busca das listas e coleta dos membros

#	with open("/home/amaury/coleta/lists_info/members_lists_collected/lists_members.txt", 'w') as f:
#		print
#		print("######################################################################")		
#		print ("Criando arquivo com resumo da coleta...")	
#		for file in os.listdir(data_dir):					#As próximas linhas são usadas para imprimir o conteúdo dos arquivos, possibilitando a verificação de inconsistências.
#			list_id = file.split(".dat")
#			list_id = long(list_id[0])
#			list_file = read_arq_bin(data_dir+file)
#			qtde_members = len(list_file)
#			members = {'list':list_id,'members': qtde_members}
#			f.write(json.dumps(members, separators=(',', ':'))+"\n")
#		print ("Arquivo criado com sucesso: /home/amaury/coleta/lists_info/members_lists_collected/lists_members.txt" )
#		print("######################################################################\n")
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
auths = oauth_keys['auths_ok']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

key_init = 0					#################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		#################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ###################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves
lists_collected = "/home/amaury/coleta/ego_collection/data/lists_collect.txt"## Arquivo contendo as listas coletadas
data_dir = "/home/amaury/coleta/lists_info/members_lists_collected/bin/" ###### Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/lists_info/members_lists_collected/error/" ### Diretório para armazenamento dos arquivos de erro
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