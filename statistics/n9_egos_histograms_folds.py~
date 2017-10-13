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
##		Status - Versão 1 - Gera histogramas para a rede N9 - seguidores do ego
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos seguidores
################################################################################################
def read_arq_bin(file):
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
# HTML
######################################################################################################################################################################
def dynamic_histogram(data):
	print ("Criando histograma dinâmico...")
	normalized = [go.Histogram(x=data,marker=dict(color='black'))]
	plotly.offline.plot(normalized, filename=output_dir_html+"followers_hist_k_"+str(k)+".html")
	print ("OK")
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram(data):
	print ("Criando histograma...")
	
	plt.hist(data,bins=bins,label="k = "+str(k)+" - "+str(len(data))+" egos",color='black')
	plt.xlabel ("Followers")
	plt.ylabel ("Egos")
	plt.title ("Rede de Seguidores - Número de seguidores por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"followers_hist_k_"+str(k)+".png")	
	plt.close()
	
	plt.hist(data,bins=bins,label="k = "+str(k)+" - "+str(len(data))+" egos",color='black')
	plt.xlabel ("Followers")
	plt.xlim([0, axis_x_limit])
	plt.ylabel ("Egos")
	plt.title ("Rede de Seguidores - Número de seguidores por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir_zoom+"followers_hist_k_"+str(k)+".png")	
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
	n_followers=[]
	print ("Preparando dados...")
	with open(input_file, 'r') as infile:
		intersection = json.load(infile)
		for user in intersection:
			followers_list = read_arq_bin(data_dir+str(user)+".dat") # Função para converter o binário de volta em string em formato json.
			n_followers.append(len(followers_list))
	print ("Total de usuários ego: "+str(len(n_followers)))
	print ("OK!")
	print	
	histogram(n_followers)
	dynamic_histogram(n_followers)

#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
bins=1500 ################################################################# Quantidade de barras no histograma
axis_x_limit = 100000	################################################### Limite para eixo x (zoom)
formato = 'l'				################################################### Long para id do seguidor
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################
#threshold = [0,10,20,30,40,50,100,200]
threshold = [0,5]
for i in range(len(threshold)):
	k = threshold[i]
	print ("Gerando gráficos com k = "+str(k)) 

	input_file = "/home/amaury/folds/histograms/intersection_k_"+str(k)+".txt"
	data_dir = "/home/amaury/folds/n9/egos/bin/"
	output_dir =  "/home/amaury/folds/histograms/n9/"
	output_dir_zoom =  "/home/amaury/folds/histograms/n9/zoom/"
	output_dir_html =  "/home/amaury/folds/histograms/n9/html/"
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