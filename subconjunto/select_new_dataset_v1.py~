# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##
##		28-07-2017 - NÃO RODAR NOVAMENTE.... RISCO DE MODIFICAR OS ALTERS A SEREM COLETADOS!!!!!
##
##
##		Status - Versão 1 - Recebe lista com 500 egos aleatórios e verifica quais deles extrapolam o número de 5mil alters.
##		Gera arquivo com o id do ego e o número de alters de cada um.
##						
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin_friends(file):
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

################################################################################################
# Imprime os arquivos binários com os ids dos followers
################################################################################################
def read_arq_bin_followers(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		followers_file = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			follower = user_struct.unpack(buffer)
			followers_file.append(follower[0])
	return followers_file

################################################################################################
# Seleciona aleatoriamente um número de alters
################################################################################################
def random_alters(user,alters_list,data_dir):
	vetor = random.sample(xrange(1,len(alters_list)), 5000)						# Gera números aleatórios para 5k alters do total de alters do user ego.
	print("Ordenando vetor de tamanho "+str(len(vetor))+"...")					# Ordenar o vetor
	vetor=sorted(vetor)

	print("Localizando alters...")														# Localizar os índices (números aleatórios) e armazenar a lista com os respectivos IDs dos alters
	random_alters=[]											
	for indice in vetor:
		random_alters.append(alters_list[indice-1])									# Seleciona os alters correspondentes aos índices aleatórios...
	print len(random_alters)		

	print("Salvando lista de alters aleatórios em arquivo...")
	with open(data_dir+str(user)+".dat", "w+b") as f:								# Salvando os IDS dos alters aleatórios em arquivos BINÁRIOS já no novo local
		for alter in random_alters:
			f.write(user_struct.pack(alter))										# Grava os ids dos alters no arquivo binário do usuário
	print ("Ego: "+str(user)+" - Alters selecionados aleatoriamente...")
################################################################################################
# Copia arquivo da origem para o destino...
################################################################################################
def copy(user,origem,destino):
	shutil.copy(origem+str(user)+".dat",destino)

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	i = 0
	j = 0
	k = 0
	with open(arq1, 'r') as f:
		file = json.load(f)
		for user in file:
			friends_list = read_arq_bin_friends(data_dir_n1+str(user)+".dat") 			#Verificando número de amigos
			followers_list = read_arq_bin_followers(data_dir_n9+str(user)+".dat")		#Verificando número de seguidores

#################################################################################### Testando número de AMIGOS			
			if len(friends_list) <= 5000:
				copy(user,data_dir_n1,new_data_dir_n1)				## Se menor ou igual que 5k, copia arquivo com amigos para o novo diretório
			else:
				alters_list = random_alters(user,friends_list,new_data_dir_n1)	## Se maior que 5k, chama função para selecionar 5k aleatoriamente
				i+=1

#################################################################################### Testando número de SEGUIDORES
			if len(followers_list) <= 5000:							## Se menor ou igual que 5k, copia arquivo com seguidores para o novo diretório
				copy(user,data_dir_n9,new_data_dir_n9)
			else:
				alters_list = random_alters(user,followers_list,new_data_dir_n9)## Se maior que 5k, chama função para selecionar 5k aleatoriamente
				j+=1

#################################################################################### Copiando arquivos para a rede de RETWEETS
			copy(user,data_dir_n2,new_data_dir_n2)
#################################################################################### Copiando arquivos para a rede de LIKES
			copy(user,data_dir_n3,new_data_dir_n3)
#################################################################################### Copiando arquivos para a rede de MENÇÕES
			copy(user,data_dir_n4,new_data_dir_n4)			
#################################################################################### Gerando estatísticas do algoritmo			
			if len(followers_list) > 5000 and len(friends_list) > 5000:
				k+=1	


		print ("Usuários com mais de 5k amigos: "+str(i))
		print ("Usuários com mais de 5k seguidores: "+str(j))
		print ("Usuários com mais de 5k amigos e seguidores: "+str(k))
					
######################################################################################################################################################################
	
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")


#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

arq1 = "/home/amaury/coleta/subconjunto/random_egos/k10/500.json"					#################### Arquivo com 500 egos aleatórios (de um total de 3980)

data_dir_n1 = "/home/amaury/coleta/n1/egos_friends/full_with_prunned/bin/" 	#################### Diretório contendo todos os egos da rede n1
data_dir_n2 = "/home/amaury/coleta/n2/egos/full_with_prunned/bin/" 				#################### Diretório contendo todos os egos da rede n2
data_dir_n3 = "/home/amaury/coleta/n3/egos/full_with_prunned/bin/" 				#################### Diretório contendo todos os egos da rede n3
data_dir_n4 = "/home/amaury/coleta/n4/egos/full_with_prunned/bin/" 				#################### Diretório contendo todos os egos da rede n4
data_dir_n9 = "/home/amaury/coleta/n9/egos_followers/full_with_prunned/bin/" 	#################### Diretório contendo todos os egos da rede n9

new_data_dir_n1 = "/home/amaury/dataset/n1/egos_limited_5k/bin/" 					#################### Diretório contendo 500 egos aleatórios da rede n1
new_data_dir_n2 = "/home/amaury/dataset/n2/egos/bin/" 								#################### Diretório contendo 500 egos aleatórios da rede n1
new_data_dir_n3 = "/home/amaury/dataset/n3/egos/bin/" 								#################### Diretório contendo 500 egos aleatórios da rede n1
new_data_dir_n4 = "/home/amaury/dataset/n4/egos/bin/" 								#################### Diretório contendo 500 egos aleatórios da rede n1
new_data_dir_n9 = "/home/amaury/dataset/n9/egos_limited_5k/bin/" 					#################### Diretório contendo 500 egos aleatórios da rede n1

formato = 'l'				####################################################### Long para o código ('l') - id dos amigos de cada user
user_struct = struct.Struct(formato) ########################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(new_data_dir_n1):
	os.makedirs(new_data_dir_n1)
if not os.path.exists(new_data_dir_n2):
	os.makedirs(new_data_dir_n2)
if not os.path.exists(new_data_dir_n3):
	os.makedirs(new_data_dir_n3)
if not os.path.exists(new_data_dir_n4):
	os.makedirs(new_data_dir_n4)
if not os.path.exists(new_data_dir_n9):
	os.makedirs(new_data_dir_n9)			

#Executa o método main
if __name__ == "__main__": main()