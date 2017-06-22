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
##		Status - Versão 1 - Gera gráficos para a rede N3 - Likes
## 
######################################################################################################################################################################

################################################################################################
# Converte binários para JSON retornando a lista de tweets favoritos para cada usuário
################################################################################################
def read_arq_bin(file):
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
	
######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def dynamic_histogram(n_tweets,n_authors):
	print ("Criando histograma dinâmico... Número de Favoritos por ego")
	histogram = [go.Histogram(x=n_tweets,marker=dict(color='green'))]
	plotly.offline.plot(histogram, filename=output_dir+"Favoritos.html")
	print ("OK")
	print
	
	print ("Criando histograma dinâmico... Número de Autores_tweets_favoritos por ego")
	histogram = [go.Histogram(x=n_authors,marker=dict(color='green'))]
	plotly.offline.plot(histogram, filename=output_dir+"Autores_Tweets_Favoritos.html")
	print ("OK")
	print
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram_full(n_tweets,n_authors):
	print ("Criando histograma... Número de Favoritos por ego")
	plt.hist(n_tweets,bins=bins,color='green')
	plt.xlabel ("Tweets Favoritos")
	plt.ylabel ("Egos")
	plt.title ("Rede de Favoritos - Número de favoritos por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"Favoritos_hist_full_bins.png")
	plt.close()
	print ("Criando histograma... Número de Autores_Tweets_Favoritos por ego")
	plt.hist(n_authors,bins=bins,color='green')
	plt.xlabel ("Autores de Tweets Favoritos")
	plt.ylabel ("Egos")
	plt.title ("Rede de Favoritos - Número de Autores_Tweets_Favoritos por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"Autores_Tweets_Favoritos_hist_full_bins.png")
	plt.close()

	print ("OK!")
	print
######################################################################################################################################################################
# Scatter Plot
######################################################################################################################################################################
def scatter_graph(n_tweets,n_authors):
	print ("Criando gráfico de dispersão...")	
	plt.scatter(x = n_tweets, y=n_authors,alpha=0.5,label=str(len(n_tweets))+" egos",color='green')
	plt.xlabel ("Tweets Favoritos")
	plt.ylabel ("Authors")
	plt.title ("Rede de Favoritos - Gráfico de Dispersão ")
	plt.legend(loc='best')

	plt.savefig(output_dir+"Scatter.png")		
	plt.close()
	print ("OK!")
	print	
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	n_tweets = []
	n_authors = []
	print ("Preparando dados...")
	for file in os.listdir(data_dir):
		tweets_list,authors_list = read_arq_bin(data_dir+file) # Função para converter o binário de volta em string em formato json.
		authors_set = set()
		authors_set.update(authors_list)
		n_tweets.append(len(tweets_list))
		n_authors.append(len(authors_set))

	print ("Total de usuários ego: "+str(len(n_tweets))) 
	print ("OK!")
	print	
	dynamic_histogram(n_tweets,n_authors)
	histogram_full(n_tweets,n_authors)
	scatter_graph(n_tweets,n_authors)

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
bins=50
######################################################################################################################
data_dir = "/home/amaury/coleta/n3/egos/"+str(qtde_egos)+"/bin/"
output_dir =  "/home/amaury/coleta/statistics/n3/"+str(qtde_egos)+"/"
formato = 'll'				################################################################### Long para o código ('l') e depois o array de chars de X posições:	
favorites_struct = struct.Struct(formato) ################################################# Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

#Executa o método main
if __name__ == "__main__": main()