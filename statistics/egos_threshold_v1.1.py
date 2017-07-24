# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random, time
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
##		Status - Versão 1 - Seleciona egos que tenham um conjunto mínimo de alters em cada as interações.
##								Exemplo: 5 amigos, 5 seguidores, 5 autores diferentes de retweets, 5 autores diferentes de likes e 5 usuários distintos mencionados.
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
#		friends_list = []
		friends_set = set()
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
#			friends_list.append(friend[0])
			friends_set.add(friend[0])
#	return friends_list
	return friends_set

################################################################################################
# Imprime os arquivos binários com os ids dos seguidores
################################################################################################
def read_arq_bin_followers(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
#		followers_list = []
		followers_set = set()
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
#			followers_list.append(friend[0])
			followers_set.add(friend[0])
#	return followers_list
	return followers_set
	
################################################################################################
# Converte binários para JSON retornando a lista de retweets para cada usuário
################################################################################################
def read_arq_bin_retweets(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
#		retweets_list = []
#		retweets_authors_list = []
		retweets_authors_set = set()
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			retweet, user = timeline_struct.unpack(buffer)
#			retweets_list.append(retweet)
#			retweets_authors_list.append(user)
			retweets_authors_set.add(user)
#	return retweets_list,retweets_authors_list
	return retweets_authors_set
	
################################################################################################
# Converte binários para JSON retornando a lista de tweets favoritos para cada usuário
################################################################################################
def read_arq_bin_likes(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
#		likes_list = []
#		likes_authors_list = []
		likes_authors_set = set()
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			tweet, user = timeline_struct.unpack(buffer)
#			likes_list.append(tweet)
#			likes_authors_list.append(user)
			likes_authors_set.add(user)			# Considerando apenas autores distintos
#	return likes_list,likes_authors_list
	return likes_authors_set
	
################################################################################################
# Converte binários para JSON retornando a lista de menções para cada usuário
################################################################################################
def read_arq_bin_mentions(file):
	with open(file, 'r') as f:	 
		f.seek(0,2)
		tamanho = f.tell()
		f.seek(0)
#		tweets_list = []
#		mentions_list = []
		mentions_set = set()
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			tweet, user = timeline_struct.unpack(buffer)
#			tweets_list.append(tweet)
#			mentions_list.append(user)
			mentions_set.add(user)			# Considerando apenas mencionados distintos
#	return tweets_list,mentions_list
	return mentions_set
	

######################################################################################################################################################################
#
# Salvar intersecção em arquivo...
#
######################################################################################################################################################################
def save_intersection(intersection):
	with open(output_dir+"intersection_k_"+str(k)+".txt", 'w') as outfile:
		outfile.write(json.dumps(intersection))
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	ini = time.time()
	i=0														# Contador
	intersection = [] 

	print ("Preparando dados...")

	for file in os.listdir(friends_dir):
		i+=1
		ego_id = file.split(".dat")
		ego_id = long(ego_id[0])

		friends_set = read_arq_bin_friends(friends_dir+file) # Função para converter o binário de volta em string em formato json.
		if (len(friends_set) >= k):
			followers_set = read_arq_bin_followers(followers_dir+file)
			if (len(followers_set) >= k):
				retweets_set = read_arq_bin_retweets(retweets_dir+file)
				if (len(retweets_set) >= k):
					likes_set = read_arq_bin_likes(likes_dir+file)
					if (len(likes_set) >= k):
						mentions_set = read_arq_bin_mentions(mentions_dir+file)
						if (len(mentions_set) >= k):
							intersection.append(ego_id)
						else:
							print (str(i)+" - "+str(ego_id)+" - abaixo do threshold - MENTIONS: "+str(len(mentions_set)))
					else:
						print (str(i)+" - "+str(ego_id)+" - abaixo do threshold - LIKES: "+str(len(likes_set)))
				else:
					print (str(i)+" - "+str(ego_id)+" - abaixo do threshold - RETWEETS: "+str(len(retweets_set)))
			else:
				print (str(i)+" - "+str(ego_id)+" - abaixo do threshold - FOLLOWERS: "+str(len(followers_set)))		
		else:
			print (str(i)+" - "+str(ego_id)+" - abaixo do threshold - FRIENDS: "+str(len(friends_set)))
	print
	
	save_intersection(intersection)
	print ("Tamanho da intersecção com k="+str(k)+": "+str(len(intersection)))
	print
	fim = time.time()	
	print("######################################################################")
	print "Script V_1.1 finalizado! Tempo de Execução: ",fim-ini
	print("######################################################################\n")
#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full_with_prunned' 		#10, 50, 100, 500 ou full ou full_with_prunned
k = 10 										# threshold - Conjunto mínimo - 0,10,20,30,40,50,100,200
######################################################################################################################
friends_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"
followers_dir = "/home/amaury/coleta/n9/egos_followers/"+str(qtde_egos)+"/bin/"
retweets_dir = "/home/amaury/coleta/n2/egos/"+str(qtde_egos)+"/bin/"
likes_dir = "/home/amaury/coleta/n3/egos/"+str(qtde_egos)+"/bin/"
mentions_dir = "/home/amaury/coleta/n4/egos/"+str(qtde_egos)+"/bin/"

output_dir =  "/home/amaury/coleta/subconjunto/"+str(qtde_egos)+"/"

user_format = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(user_format) ##################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
timeline_format = 'll'				############################################# Long para o id do tweet ('l') e long para id do autor/mencionado 
timeline_struct = struct.Struct(timeline_format) ############################# Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

#Executa o método main
if __name__ == "__main__": main()