# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import scipy.stats as stats
import numpy.random as rnd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import numpy as np
import powerlaw
import seaborn as sns
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Two-Sided Kolmogorov-Smirnov Tests - Testar se dois grupos de amostras foram tirados de conjuntos com a mesma distribuição.
##									Compara de dois em dois.EX: 03 folds - A,B,C - compara AeB, AeC, e BeC.  
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin_n1(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		friends_list = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_list.append(friend[0])
	return friends_list

################################################################################################
# Converte binários para JSON retornando a lista de retweets para cada usuário
################################################################################################
def read_arq_bin_n2(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		retweets_list = []
		authors_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)
			retweets_list.append(retweet)
			authors_list.append(user)
	return retweets_list,authors_list

################################################################################################
# Converte binários para JSON retornando a lista de tweets favoritos para cada usuário
################################################################################################
def read_arq_bin_n3(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		tweets_list = []
		authors_list = []
		while f.tell() < tamanho:
			buffer = f.read(favorites_struct.size)
			tweet, user = favorites_struct.unpack(buffer)
			tweets_list.append(tweet)
			authors_list.append(user)
	return tweets_list,authors_list

################################################################################################
# Converte binários para JSON retornando a lista de tweets favoritos para cada usuário
################################################################################################
def read_arq_bin_n4(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		mentions_list = []
		tweets_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			tweet, user = timeline_struct.unpack(buffer)
			tweets_list.append(tweet)
			mentions_list.append(user)
	return tweets_list,mentions_list	

################################################################################################
# Imprime os arquivos binários com os ids dos seguidores
################################################################################################
def read_arq_bin_n9(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
		followers_list = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			followers_list.append(friend[0])
	return followers_list
		


######################################################################################################################################################################
#
#Two-Sided Kolmogorov-Smirnov Tests
#
######################################################################################################################################################################
def ks_test(data1,data2):
	statistical, p_value = stats.ks_2samp(data1, data2)
	print statistical, p_value

######################################################################################################################################################################
#
# Calculo para a rede n1
#
######################################################################################################################################################################
def n1():	
	f1=[]
	f2=[]
	f3=[]
	print ("Preparando dados para a REDE N1 - Avaliando a Quantidade de Amigos...\n")

	for ego in fold1:
		friends_list = read_arq_bin_n1(data_dir_n1+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f1.append(len(friends_list))															# Salva a quantidade de amigos para cada ego.

	for ego in fold2:
		friends_list = read_arq_bin_n1(data_dir_n1+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f2.append(len(friends_list))															# Salva a quantidade de amigos para cada ego.
	
	for ego in fold3:
		friends_list = read_arq_bin_n1(data_dir_n1+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f3.append(len(friends_list))															# Salva a quantidade de amigos para cada ego.
		
	print ("Executando KS-TEST entre Fold1 e Fold2...")
	ks_test(f1,f2)
	print
	print ("Executando KS-TEST entre Fold1 e Fold3...")
	ks_test(f1,f3)
	print
	print ("Executando KS-TEST entre Fold2 e Fold3...")
	ks_test(f2,f3)


######################################################################################################################################################################
#
# Calculo para a rede n2
#
######################################################################################################################################################################
def n2():	
	f1=[]
	f2=[]
	f3=[]
	print ("Preparando dados para a REDE N2 - Avaliando a Quantidade de Retweets...\n")

	for ego in fold1:
		retweets_list,authors_list = read_arq_bin_n2(data_dir_n2+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f1.append(len(retweets_list))																	# Salva a quantidade de retweets para cada ego.

	for ego in fold2:
		retweets_list,authors_list = read_arq_bin_n2(data_dir_n2+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f2.append(len(retweets_list))

	for ego in fold3:
		retweets_list,authors_list = read_arq_bin_n2(data_dir_n2+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f3.append(len(retweets_list))		

	print ("Executando KS-TEST entre Fold1 e Fold2...")
	ks_test(f1,f2)
	print
	print ("Executando KS-TEST entre Fold1 e Fold3...")
	ks_test(f1,f3)
	print
	print ("Executando KS-TEST entre Fold2 e Fold3...")
	ks_test(f2,f3)

######################################################################################################################################################################
#
# Calculo para a rede n3
#
######################################################################################################################################################################
def n3():	
	f1=[]
	f2=[]
	f3=[]
	print ("Preparando dados para a REDE N3 - Avaliando a Quantidade de Likes...\n")

	for ego in fold1:
		tweets_list,authors_list = read_arq_bin_n3(data_dir_n3+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f1.append(len(tweets_list))													# Salva a quantidade de likes para cada ego.

	for ego in fold2:
		tweets_list,authors_list = read_arq_bin_n3(data_dir_n3+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f2.append(len(tweets_list))

	for ego in fold3:
		tweets_list,authors_list = read_arq_bin_n3(data_dir_n3+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f3.append(len(tweets_list))		

	print ("Executando KS-TEST entre Fold1 e Fold2...")
	ks_test(f1,f2)
	print
	print ("Executando KS-TEST entre Fold1 e Fold3...")
	ks_test(f1,f3)
	print
	print ("Executando KS-TEST entre Fold2 e Fold3...")
	ks_test(f2,f3)

######################################################################################################################################################################
#
# Calculo para a rede n4
#
######################################################################################################################################################################
def n4():	
	f1=[]
	f2=[]
	f3=[]
	print ("Preparando dados para a REDE N4 - Avaliando a Quantidade de Menções...\n")

	for ego in fold1:
		tweets_list,mentions_list = read_arq_bin_n4(data_dir_n4+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f1.append(len(mentions_list))														# Salva a quantidade de menções para cada ego.

	for ego in fold2:
		tweets_list,mentions_list = read_arq_bin_n4(data_dir_n4+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f2.append(len(mentions_list))

	for ego in fold3:
		tweets_list,mentions_list = read_arq_bin_n4(data_dir_n4+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f3.append(len(mentions_list))		

	print ("Executando KS-TEST entre Fold1 e Fold2...")
	ks_test(f1,f2)
	print
	print ("Executando KS-TEST entre Fold1 e Fold3...")
	ks_test(f1,f3)
	print
	print ("Executando KS-TEST entre Fold2 e Fold3...")
	ks_test(f2,f3)

######################################################################################################################################################################
#
# Calculo para a rede n9
#
######################################################################################################################################################################
def n9():	
	f1=[]
	f2=[]
	f3=[]
	print ("Preparando dados para a REDE N9 - Avaliando a Quantidade de Seguidores...\n")

	for ego in fold1:
		followers_list = read_arq_bin_n9(data_dir_n9+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f1.append(len(followers_list))									# Salva a quantidade de seguidores para cada ego.

	for ego in fold2:
		followers_list = read_arq_bin_n9(data_dir_n9+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f2.append(len(followers_list))

	for ego in fold3:
		followers_list = read_arq_bin_n9(data_dir_n9+str(ego)+".dat")		 			# Função para converter o binário de volta em string em formato json.
		f3.append(len(followers_list))		

	print ("Executando KS-TEST entre Fold1 e Fold2...")
	ks_test(f1,f2)
	print
	print ("Executando KS-TEST entre Fold1 e Fold3...")
	ks_test(f1,f3)
	print
	print ("Executando KS-TEST entre Fold2 e Fold3...")
	ks_test(f2,f3)
		
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	print																				
	print("######################################################################")
	n1()
	print																				
	print("######################################################################")
	n2()
	print																				
	print("######################################################################")
	n3()
	print																				
	print("######################################################################")
	n4()
	print																				
	print("######################################################################")
	n9()
	print																				
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
arq_fold1 = "/home/amaury/twitter/create_folds/egos_fold1.json"						#################### Arquivo JSON contendo a lista de usuários egos aleatórios FOLD 1
arq_fold2 = "/home/amaury/twitter/create_folds/egos_fold2.json"						#################### Arquivo JSON contendo a lista de usuários egos aleatórios FOLD 2
arq_fold3 = "/home/amaury/twitter/create_folds/egos_fold3.json"						#################### Arquivo JSON contendo a lista de usuários egos aleatórios FOLD 3

data_dir_n1 = "/home/amaury/coleta/n1/egos_friends/full_with_prunned/bin/" 		#################### Diretório contendo todos os egos da rede n1
data_dir_n2 = "/home/amaury/coleta/n2/egos/full_with_prunned/bin/" 					#################### Diretório contendo todos os egos da rede n2
data_dir_n3 = "/home/amaury/coleta/n3/egos/full_with_prunned/bin/" 					#################### Diretório contendo todos os egos da rede n3
data_dir_n4 = "/home/amaury/coleta/n4/egos/full_with_prunned/bin/" 					#################### Diretório contendo todos os egos da rede n4
data_dir_n9 = "/home/amaury/coleta/n9/egos_followers/full_with_prunned/bin/" 		#################### Diretório contendo todos os egos da rede n9

formato_user = 'l'				########################### Long para id do amigo
user_struct = struct.Struct(formato_user) ############### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

formato_timeline = 'll'				######################## Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato_timeline) ####### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

formato_favorites = 'll'				##################### Long para id do tweet e outro long para autor	
favorites_struct = struct.Struct(formato_favorites) ##### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################
######################################################################################################################

																	# Carregando as listas com os egos aleatórios... 
with open(arq_fold1, 'r') as f:
	fold1 = json.load(f)
with open(arq_fold2, 'r') as f:
	fold2 = json.load(f)
with open(arq_fold3, 'r') as f:
	fold3 = json.load(f)

######################################################################################################################
#Executa o método main
if __name__ == "__main__": main()