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
##		Status - Versão 1 - Gera gráficos para a rede N2 - retweets
## 
######################################################################################################################################################################

################################################################################################
# Converte binários para JSON retornando a lista de retweets para cada usuário
################################################################################################
def read_arq_bin(file):
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
	
######################################################################################################################################################################
# HTML Normalized
######################################################################################################################################################################
def dynamic_histogram_normalized(n_retweets,n_authors):
	print ("Criando histograma dinâmico normalizado... Número de Retweets por ego")
	normalized = [go.Histogram(x=n_retweets,histnorm='probability',showlegend=True)]
	plotly.offline.plot(normalized, filename=output_dir_html+"retweets_histograma_k_"+str(k)+"_normalized.html")
	print ("OK")
	print
	
	print ("Criando histograma dinâmico normalizado... Número de Autores de Retweets por ego")
	normalized = [go.Histogram(x=n_authors,histnorm='probability')]
	plotly.offline.plot(normalized, filename=output_dir_html+"retweets_autores_histograma_k_"+str(k)+"_normalized.html")
	print ("OK")
	print
######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def dynamic_histogram(n_retweets,n_authors):
	print ("Criando histograma dinâmico... Número de Retweets por ego")
	histogram = [go.Histogram(x=n_retweets)]
	plotly.offline.plot(histogram, filename=output_dir_html+"retweets_hist_k_"+str(k)+".html")
	print ("OK")
	print
	
	print ("Criando histograma dinâmico... Número de Autores de Retweets por ego")
	histogram = [go.Histogram(x=n_authors)]
	plotly.offline.plot(histogram, filename=output_dir_html+"retweets_authors_hist_k_"+str(k)+".html")
	print ("OK")
	print
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram_full(n_retweets,n_authors):
	print ("Criando histograma... Número de Retweets por ego")
	plt.hist(n_retweets,bins=bins,label="k = "+str(k)+" - "+str(len(n_retweets))+" egos")
	plt.xlabel ("Retweets")
	plt.ylabel ("Egos")
	plt.title ("Rede de Retweets - Número de retweets por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"retweets_hist_k_"+str(k)+".png")
	plt.close()
	print ("Criando histograma... Número de Autores de Retweets por ego")
	plt.hist(n_authors,bins=bins,label="k = "+str(k)+" - "+str(len(n_retweets))+" egos")
	plt.xlabel ("Autores distintos de retweets feitos pelo ego")
	plt.ylabel ("Egos")
	plt.title ("Rede de Retweets - Número de Autores de Retweets por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"retweets_authors_hist_k_"+str(k)+".png")
	plt.close()

	print ("OK!")
	print

######################################################################################################################################################################
# Scatter Plot
######################################################################################################################################################################
def scatter_graph(n_retweets,n_authors):
	print ("Criando gráfico de dispersão...")	
	plt.scatter(x = n_retweets, y=n_authors,alpha=0.5,label=str(len(n_retweets))+" egos")
	plt.xlabel ("Retweets")
	plt.ylabel ("Authors")
	plt.title ("Rede de Retweets - Gráfico de Dispersão ")
	plt.legend(loc='best')

	plt.savefig(output_dir+"retweets_scatter_k_"+str(k)+".png")		
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
	n_retweets = []
	n_authors = []
	print ("Preparando dados...")
	with open(input_file, 'r') as infile:
		intersection = json.load(infile)
		for user in intersection:
			retweets_list,authors_list = read_arq_bin(data_dir+str(user)+".dat") # Função para converter o binário de volta em string em formato json.
			authors_set = set()
			authors_set.update(authors_list)
			n_retweets.append(len(retweets_list))
			n_authors.append(len(authors_set))
	print ("Total de usuários ego: "+str(len(n_retweets))) 
	print ("OK!")
	print	
	dynamic_histogram(n_retweets,n_authors)
	histogram_full(n_retweets,n_authors)
	scatter_graph(n_retweets,n_authors)

#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full_with_prunned'	########################################## 10, 50, 100, 500 ou full ou full_with_prunned
bins=50 ################################################################### Quantidade de barras no histograma
formato = 'll'				###################################################  Long para id do tweet e outro long para autor
timeline_struct = struct.Struct(formato) ################################## Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################
threshold = [0,10,20,30,40,50,100,200]
for i in range(len(threshold)):
	k = threshold[i]
	print ("Gerando gráficos com k = "+str(k)) 

	input_file = "/home/amaury/coleta/subconjunto/"+str(qtde_egos)+"/intersection_k_"+str(k)+".txt"
	data_dir = "/home/amaury/coleta/n2/egos/"+str(qtde_egos)+"/bin/"
	output_dir =  "/home/amaury/coleta/statistics/n2/"+str(qtde_egos)+"/"
	output_dir_zoom =  "/home/amaury/coleta/statistics/n2/"+str(qtde_egos)+"/zoom/"
	output_dir_html =  "/home/amaury/coleta/statistics/n2/"+str(qtde_egos)+"/html/"

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