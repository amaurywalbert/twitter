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
			tweet, user = timeline_struct.unpack(buffer)
			status = {'tweet':tweet, 'user':user}
			mentions_list.append(status)
	return mentions_list
	
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i 													# numero de usuários com arquivos já coletados / Número de arquivos no diretório
	for file in os.listdir(timeline_collected_dir):	# Verifica a lista de egos coletados 
		ego = file.split(".json")
		ego = long(ego[0])
		if not dictionary.has_key(ego):
			i+=1
			try:
				with open(data_dir+str(ego)+".dat", 'w+b') as f:
					with open(timeline_collected_dir+file,'r') as timeline:
						for line in timeline:
							tweet = json.loads(line)
							if not tweet.has_key('retweeted_status'):																	#Ignora retweets
								try:		
									for mention in tweet['entities']['user_mentions']:
										user_mentioned = long(mention['id'])
										f.write(timeline_struct.pack(tweet['id'], user_mentioned))		# Grava os ids dos tweet, o id do user mencionado
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
timeline_collected_dir = "/home/amaury/coleta/timeline_collect/full_with_prunned/json/"####### Arquivo contendo a timeline dos usuários ego já coletados em formato JSON
data_dir = "/home/amaury/coleta/n4/egos_with_prunned/full/bin/" ############## Diretório para armazenamento dos arquivos

formato = 'll'				#################################################### Long para id do tweet e outro long para autor
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