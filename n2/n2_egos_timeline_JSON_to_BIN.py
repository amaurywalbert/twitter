# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Pesquisa na timeline e extrai informações necessárias para formar o conjunto de egos da rede N2 - Conjunto de autores de retweets.
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		retweets_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)
			status = {'retweet':retweet, 'user':user}
			retweets_list.append(status)
	return retweets_list
	
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos favoritos do user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i 													# numero de usuários com arquivos já coletados / Número de arquivos no diretório
	j = 0															# Exibe o número ordinal do ego que está sendo usado para a busca da timeline
	for file in os.listdir(timeline_collected_dir):					# Verifica a lista de egos coletados e para cada um, busca a timeline dos alters listados no arquivo do ego.
		ego = file.split(".json")
		ego = long(ego[0])
		if not dictionary.has_key(ego):
			print ("Buscando retweets do ego: "+str(ego))
			j+=1
			try:
				with open(data_dir+str(ego)+".dat", 'w+b') as f:
					with open(timeline_collected_dir+file,'r') as timeline:
						for line in timeline:
							retweet = json.loads(line)
							try:
								tweet = retweet['retweeted_status']['id']
								tweet = long(tweet)									
								user =  retweet['retweeted_status']['user']['id']
								user = long(user)
								f.write(timeline_struct.pack(tweet, user))						# Grava os ids dos tweet  e o id do autor n
							except KeyError:
								print ("Não é retweet!")
			except Exception as e:
				print e		
			print
			print("######################################################################")
	
	print
	print("######################################################################")
	print("Conversão finalizada!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

timeline_collected_dir = "/home/amaury/coleta/timeline_collect/100/json/"####### Arquivo contendo a lista dos usuários ego já coletados em formato JSON

data_dir = "/home/amaury/coleta/n2/timeline_collect/egos/100/bin/" ############# Diretório para armazenamento dos arquivos
error_dir = "/home/amaury/coleta/n2/timeline_collect/egos/100/error/" ########## Diretório para armazenamento dos arquivos de erro

formato = 'll'				####################################################### Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

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
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
i = 0	#Conta quantos usuários já foram coletados (todos arquivos no diretório)
for file in os.listdir(data_dir):
	user_id = file.split(".dat")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
	
#Executa o método main
if __name__ == "__main__": main()