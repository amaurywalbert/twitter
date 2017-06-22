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
# Seaborn
######################################################################################################################################################################
#def seaborn_print(data):
#	print ("Seaborn\n")
#	sns.distplot(data, bins=bins, kde=False, rug=False,label=str(len(data))+" egos")
#	plt.xlim([0, axis_x_limit])
#	sns.plt.savefig(output_dir+"seaborn_full_bins.png")
#	
#	sns.distplot(data, bins=bins, kde=False, rug=False,label=str(len(data))+" egos")
#	plt.xlim([0, axis_x_limit])
#	sns.plt.savefig(output_dir+"seaborn.png")	

	
######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def normalized_print(data):
	print ("Criando histograma dinâmico...")
	normalized = [go.Histogram(x=data,histnorm='probability')]
	plotly.offline.plot(normalized, filename=output_dir+"normalized.html")
	
#	cumulative = [go.Histogram(x=data,cumulative=True,histnorm='probability')]
#	plotly.offline.plot(cumulative, filename=output_dir+"cumulative.html")

	print ("OK")
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram(data,i):
	print ("Criando histograma...")
	
	plt.hist(data,bins=bins,label=str(len(data))+" egos")
	plt.xlabel ("Friends")
	plt.ylabel ("Egos")
	plt.title ("Número de amigos por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"hist_full_bins.png")
	plt.close()
	plt.hist(data,bins=bins,label=str(len(data))+" egos")
	plt.xlabel ("Friends")
	plt.xlim([0, axis_x_limit])
	plt.ylabel ("Egos")
	plt.title ("Número de amigos por ego")
	plt.legend(loc='best')
	plt.savefig(output_dir+"histograma.png")	
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
	statistics={}
	n_friends=[]
	print ("Preparando dados...")
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
bins=50
axis_x_limit = 10000 							#Limite para eixo x (zoom)
######################################################################################################################
data_dir = "/home/amaury/coleta/n1/egos_friends/"+str(qtde_egos)+"/bin/"
output_dir =  "/home/amaury/coleta/statistics/n1/"+str(qtde_egos)+"/"
formato = 'l'				################################################### Long para id do amigo
user_struct = struct.Struct(formato) ###################################### Inicializa o objeto do tipo struct para poder armazenar o formato específico no arquivo binário

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

#Executa o método main
if __name__ == "__main__": main()