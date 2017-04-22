# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Pesquisa na timeline e extrai informações necessárias para formar o conjunto de egos da rede N4 - Conjunto de mencionados
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		mentions_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			tweet, user, is_retweet = timeline_struct.unpack(buffer)
			status = {'tweet':tweet, 'user':user, 'is_retweet':is_retweet}
			mentions_list.append(status)
	return mentions_list
	
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
	for file in os.listdir(timeline_collected_dir):	# Verifica a lista de egos coletados e para cada um, busca a timeline dos alters listados no arquivo do ego.
		ego = file.split(".json")
		ego = long(ego[0])
		if not dictionary.has_key(ego):
			i+=1
			try:
				with open(data_dir+str(ego)+".dat", 'w+b') as f:
					with open(timeline_collected_dir+file,'r') as timeline:
						for line in timeline:
							tweet = json.loads(line)
							is_retweet = 0
							if tweet.has_key('retweeted_status'):
								is_retweet = 1
			
							try:		
								mentions = tweet['entities']['user_mentions']
								if mentions:
									for mention in mentions:
										user_mentioned = long(mention['id'])
										f.write(timeline_struct.pack(tweet['id'], user_mentioned, is_retweet))		# Grava os ids dos tweet, o id do user mencionado e se foi um retweet ou não no arquivo binário do usuário
							except KeyError:
								pass
###
#				mentions_list = read_arq_bin(data_dir+str(ego)+".dat") # Função para converter o binário de volta em string em formato json.
#				print mentions_list
####	

				print (str(i)+" - ego convertido com sucesso!")
			except Exception as e:
				print e
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

timeline_collected_dir = "/home/amaury/coleta/timeline_collect/500/json/"####### Arquivo contendo a timeline dos usuários ego já coletados em formato JSON

data_dir = "/home/amaury/coleta/n4/mentions_collect/egos/500/bin/" ############## Diretório para armazenamento dos arquivos

formato = 'lli'				#################################################### Long para id do tweet e outro long para autor e uma flag (0 ou 1) indicando se é um tetweet
timeline_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

######################################################################################################################
######################################################################################################################
######################################################################################################################
#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)

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