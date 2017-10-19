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
##		Status - Versão 1 - Gera gráficos para a rede N4 - Menções
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
		mentions_list = []
		tweets_list = []
		while f.tell() < tamanho:
			buffer = f.read(timeline_struct.size)
			tweet, user = timeline_struct.unpack(buffer)
			tweets_list.append(tweet)
			mentions_list.append(user)
	return tweets_list,mentions_list

######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def dynamic_histogram(n_tweets,n_mentions):
	print ("Criando histograma dinâmico... Tweets com menções por ego")
	histogram = [go.Histogram(x=n_tweets,marker=dict(color='red'))]
	plotly.offline.plot(histogram, filename=output_dir_html+"mentions_tweets_with_mentions_hist_k_"+str(k)+".html")
	print ("OK")
	print
	
	print ("Criando histograma dinâmico... Conjunto de Mencionados por ego")
	histogram = [go.Histogram(x=n_mentions,marker=dict(color='red'))]
	plotly.offline.plot(histogram, filename=output_dir_html+"mentions_users_mentioned_hist_k_"+str(k)+".html")
	print ("OK")
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram_full(n_tweets,n_mentions):
	print ("Criando histograma... Tweets com menções por ego")
	plt.hist(n_tweets,bins=bins,label="k = "+str(k)+" - "+str(len(n_tweets))+" egos",color='red')
	plt.xlabel ("Tweets com menções")
	plt.ylabel ("Egos")
	plt.title ("Rede de Menções - Tweets com Menções por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"mentions_tweets_with_mentions_hist_k_"+str(k)+".png")
	plt.close()
	print ("Criando histograma... Conjunto de Mencionados por ego")
	plt.hist(n_mentions,bins=bins,label="k = "+str(k)+" - "+str(len(n_tweets))+" egos",color='red')
	plt.xlabel ("Usuários distintos mencionados pelo ego")
	plt.ylabel ("Egos")
	plt.title ("Rede de Menções - Conjunto de Mencionados por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"mentions_users_mentioned_hist_k_"+str(k)+".png")
	plt.close()

	print ("OK!")
	print
######################################################################################################################################################################
# Scatter Plot
######################################################################################################################################################################
def scatter_graph(n_tweets,n_mentions):
	print ("Criando gráfico de dispersão...")	
	plt.scatter(x = n_tweets, y=n_mentions,alpha=0.5,label="k = "+str(k)+" - "+str(len(n_tweets))+" egos",color='red')
	plt.xlabel ("Tweets com Menções")
	plt.ylabel ("Usuários Mencionados")
	plt.title ("Rede de Menções - Gráfico de Dispersão ")
	plt.legend(loc='best')

	plt.savefig(output_dir+"mentions_scatter_k_"+str(k)+".png")		
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
	n_mentions = []
	print ("Preparando dados...")
	with open(input_file, 'r') as infile:
		intersection = json.load(infile)
		for user in intersection:
			tweets_list,mentions_list = read_arq_bin(data_dir+str(user)+".dat") # Função para converter o binário de volta em string em formato json.
			tweets_set = set()
			mentions_set = set()		
			tweets_set.update(tweets_list)
			mentions_set.update(mentions_list)
			n_tweets.append(len(tweets_set))
			n_mentions.append(len(mentions_set))
	
	print ("Total de usuários ego: "+str(len(n_tweets))) 
	print ("OK!")
	print	
	dynamic_histogram(n_tweets,n_mentions)
	histogram_full(n_tweets,n_mentions)
	scatter_graph(n_tweets,n_mentions)

#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full_with_prunned'	########################################## 10, 50, 100, 500 ou full ou full_with_prunned
bins=50 ################################################################### Quantidade de barras no histograma
formato = 'll'				################################################### Long para id do tweet e outro long para autor e uma flag (0 ou 1) indicando se é um tetweet
timeline_struct = struct.Struct(formato) ################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

######################################################################################################################
threshold = [0,10,20,30,40,50,100,200]
for i in range(len(threshold)):
	k = threshold[i]
	print ("Gerando gráficos com k = "+str(k)) 

	input_file = "/home/amaury/coleta/subconjunto/"+str(qtde_egos)+"/intersection_k_"+str(k)+".txt"
	data_dir = "/home/amaury/coleta/n4/egos/"+str(qtde_egos)+"/bin/"
	output_dir =  "/home/amaury/coleta/statistics/n4/"+str(qtde_egos)+"/"
	output_dir_zoom =  "/home/amaury/coleta/statistics/n4/"+str(qtde_egos)+"/zoom/"
	output_dir_html =  "/home/amaury/coleta/statistics/n4/"+str(qtde_egos)+"/html/"

	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	if not os.path.exists(output_dir_zoom):
		os.makedirs(output_dir_zoom)
	if not os.path.exists(output_dir_html):
		os.makedirs(output_dir_html)

	#Executa o método main
	if __name__ == "__main__": main()
print("######################################################################")
print("Script finalizado!")
print("######################################################################\n")