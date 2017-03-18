# -*- coding: latin1 -*-
################################################################################################
# Script para coletar membros das listas dos egos do Twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 3.1 - Coletar membros das listas
##						STATUS - TESTE - Salvar arquivos binários contendo os ids dos membros das listas.
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
	print ("Autenticando usando chave número: "+str(key)+"/"+str(key_limit))
	api_key = tweepy.API(auths[key])
	time.sleep(wait)
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
# Imprime os arquivos binários com os ids dos membros das listas
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		friends_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_file.append(friend[0])
	return friends_file
	


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
				if dictionary.has_key(list):
					print ("Lista nº "+str(j)+": "+str(list)+" já coletada! Continuando...")
				else:
					print list			
					#save_user(j, list)																#Inicia função de busca das listas e coleta dos membros
	
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################")

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
data_dir = "/home/amaury/coleta/lists_info/members_lists_collected/bin/" ############## Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/lists_info/members_lists_collected/error/" ########### Diretório para armazenamento dos arquivos de erro
formato = 'l'				####################################################### Long para o código ('l') e depois o array de chars de X posições:	
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
wait = 15
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)

#Autenticação
try:
	api = autentication(auths)
	print
	print("######################################################################")
	print
except tweepy.error.TweepError as e:
	print("[ERRRO] Não foi possível realizar autenticação. Erro: ",str(e),".\n")
	
	
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
i = 0
for file in os.listdir(data_dir):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
	
#Executa o método main
if __name__ == "__main__": main()