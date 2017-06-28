# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
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
##		Status - Versão 1 - Seleciona egos que tenham um conjunto mínimo comum em todas as interações. Exemplo: 5 amigos, 5 seguidores, 5 retweets, 5 likes e 5 menções.
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
		friends_list = []
		while f.tell() < tamanho:
			buffer = f.read(user_struct.size)
			friend = user_struct.unpack(buffer)
			friends_list.append(friend[0])
	return friends_list
	
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():

	friends = set()										# Conjunto de egos acima do threshold de amigos
	followers = set()										# Conjunto de egos acima do threshold de seguidores
	retweets = set()										# Conjunto de egos acima do threshold de retuítes
	likes = set()											# Conjunto de egos acima do threshold de favoritos
	mentions = set()										# Conjunto de egos acima do threshold de menções

	print ("Preparando dados...")

	n_friends=[]

	for file in os.listdir(data_dir):
		friends_list = read_arq_bin(data_dir+file) # Função para converter o binário de volta em string em formato json.
		if friends_list:
			user_id = file.split(".dat")
			user_id = long(user_id[0])
			statistics[user_id] = {'n_of_friends':len(friends_list)}
			n_friends.append(statistics[user_id]['n_of_friends'])
		else:
			print ("Impossível recuperar dados de "+str(file))
	print ("Total de usuários ego: "+str(len(n_friends)))
	print ("OK!")
	print	
	histogram(n_friends)
	normalized_print(n_friends)

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
qtde_egos = 'full_with_prunned' 		#10, 50, 100, 500 ou full ou full_with_prunned
threshold = 10 							#Conjunto mínimo
######################################################################################################################
friends_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"
followers_dir = "/home/amaury/coleta/n9/egos_followers/"+str(qtde_egos)+"/bin/"
retweets_dir = "/home/amaury/coleta/n2/egos/"+str(qtde_egos)+"/bin/"
likes_dir = "/home/amaury/coleta/n3/egos/"+str(qtde_egos)+"/bin/"
mentions_dir = "/home/amaury/coleta/n4/egos/"+str(qtde_egos)+"/bin/"

output_dir =  "/home/amaury/coleta/subconjunto/"+str(qtde_egos)+"/"
formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

#Executa o método main
if __name__ == "__main__": main()