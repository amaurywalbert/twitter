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
##		Status - Versão 1 - Gera histogramas para a rede N1 - amigos do ego
## 
######################################################################################################################################################################

################################################################################################
# Imprime os arquivos binários com os ids dos amigos
################################################################################################
def read_arq_bin(file):
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
# HTML
######################################################################################################################################################################
def normalized_print(data):
	print ("Criando histograma dinâmico...")
	normalized = [go.Histogram(x=data,marker=dict(color='yellow'))]
	plotly.offline.plot(normalized, filename=output_dir_html+"following_hist_k_"+str(k)+".html")
	
	print ("OK")
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram(data):
	print ("Criando histograma...")
	
	plt.hist(data,bins=bins,label="k = "+str(k)+" - "+str(len(data))+" egos",color='yellow')
	plt.xlabel ("Friends")
	plt.ylabel ("Egos")
	plt.title ("Rede de Amizade - Número de amigos por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"following_hist_k_"+str(k)+".png")
	plt.close()
	
	plt.hist(data,bins=bins,label="k = "+str(k)+" - "+str(len(data))+" egos",color='yellow')
	plt.xlabel ("Friends")
	plt.xlim([0, axis_x_limit])
	plt.ylabel ("Egos")
	plt.title ("Rede de Amizade - Número de amigos por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir_zoom+"following_hist_k_"+str(k)+".png")	
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
	n_friends=[]
	print ("Preparando dados...")
	with open(input_file, 'r') as infile:
		intersection = json.load(infile)
		for user in intersection:
			friends_list = read_arq_bin(data_dir+str(user)+".dat") # Função para converter o binário de volta em string em formato json.
			n_friends.append(len(friends_list))
	print ("Total de usuários ego: "+str(len(n_friends)))
	print ("OK!")
	print	
	histogram(n_friends)
	normalized_print(n_friends)
	
#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
qtde_egos = 'full_with_prunned'	########################################## 10, 50, 100, 500 ou full ou full_with_prunned
bins=50 ################################################################### Quantidade de barras no histograma
axis_x_limit = 10000	###################################################### Limite para eixo x (zoom)
formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário
######################################################################################################################
threshold = [0,10,20,30,40,50,100,200]
for i in range(len(threshold)):
	k = threshold[i]
	print ("Gerando gráficos com k = "+str(k)) 

	input_file = "/home/amaury/coleta/subconjunto/"+str(qtde_egos)+"/intersection_k_"+str(k)+".txt"
	data_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"
	output_dir =  "/home/amaury/coleta/statistics/n1/"+str(qtde_egos)+"/"
	output_dir_zoom =  "/home/amaury/coleta/statistics/n1/"+str(qtde_egos)+"/zoom/"
	output_dir_html =  "/home/amaury/coleta/statistics/n1/"+str(qtde_egos)+"/html/"
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