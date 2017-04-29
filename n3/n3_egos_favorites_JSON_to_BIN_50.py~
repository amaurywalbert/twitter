# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - Versão 1 - Pesquisa na lista de favoritos e extrai informações necessárias para formar o conjunto de egos da rede N2 - Conjunto de autores de likes.
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		tweets_list = []
		while f.tell() < tamanho:
			buffer = f.read(favorites_struct.size)
			tweet, user = favorites_struct.unpack(buffer)
			status = {'tweet':tweet, 'user':user}
			tweets_list.append(status)
	return tweets_list
	
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
	for file in os.listdir(favorites_collected_dir):					# Verifica a lista de egos coletados e para cada um, busca a timeline dos alters listados no arquivo do ego.
		ego = file.split(".json")
		ego = long(ego[0])
		if not dictionary.has_key(ego):
			i+=1
			try:
				with open(data_dir+str(ego)+".dat", 'w+b') as f:
					with open(favorites_collected_dir+file,'r') as favorites:
						for line in favorites:
							favorite = json.loads(line)
							like = favorite['id']
							like = long(like)									
							user = favorite['user']['id']
							user = long(user)
							f.write(favorites_struct.pack(like, user))						# Grava os ids dos tweet  e o id do autor n
				print (str(i)+" - ego convertido com sucesso!")
###
#				tweets_list = read_arq_bin(data_dir+str(ego)+".dat") # Função para converter o binário de volta em string em formato json.
#				print tweets_list
####
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
qtde_egos = 10 #10, 50, 100, 500, full

favorites_collected_dir = "/home/amaury/coleta/favorites_collect/"+str(qtde_egos)+"/json/"####### Arquivo contendo a lista dos usuários ego já coletados em formato JSON
data_dir = "/home/amaury/coleta/n3/egos/"+str(qtde_egos)+"/bin/" ############# Diretório para armazenamento dos arquivos

formato = 'll'				####################################################### Long para id do tweet e outro long para autor
favorites_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

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