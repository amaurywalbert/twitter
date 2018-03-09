# -*- coding: latin1 -*-
################################################################################################
#	
#
import sys, time, json, os, os.path
import numpy as np
from math import*
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Plotar os dados de acordo com as métricas e propriedades calculadas nas redes Multilayer
##
## ID_ego a:amigos s:seguidores r:retuítes l:likes m:menções
##
## ID_ego as:data sr:data rl:data lm:data ma:data - TXT
## {ID_ego:{ as:data sr:data rl:data lm:data ma:data} - JSON
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cria diretórios
#
######################################################################################################################################################################
def create_dirs(x):
	if not os.path.exists(x):
		os.makedirs(x)	


######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def plotly_jaccard_over_edges(data,output,name,pairs):
	print ("\nCriando histograma dinâmico...")
	print ("Salvando dados em: "+str(output)+"\n")

	trace = go.Histogram(x=data, name="edges", marker=dict(color='green'))
	_data = [trace]
	layout = go.Layout(title="Jaccard over Edges - "+str(pairs), xaxis=dict(title='Jaccard'),yaxis=dict(title="Egos"))    
	fig = go.Figure(data=_data, layout=layout)

	plotly.offline.plot(fig, filename=output+pairs+".html",auto_open=False)

	print (" - OK! Histograma salvo em: "+str(output))
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def plot_jaccard_over_edges(data,output,name,pairs):
	print ("\nCriando histograma...")
	print ("Salvando dados em: "+str(output)+"\n")
	plt.hist(data,color='green')
	plt.xlabel ("Jaccard")
	plt.ylabel ("Egos")
	plt.title ("Jaccard over Edges - "+str(pairs))
	plt.legend(loc='best')
	plt.savefig(output+pairs+".png")
	plt.close()

	print (" - OK! Histograma salvo em: "+str(output))
	print		

######################################################################################################################################################################
#
# Plotar Gŕaficos relacionados aos dados
#
######################################################################################################################################################################
def print_data_jaccard_over_vertives(metric,file,output):
	with open(file,'r') as f:
		data = json.load(f)
		pairs = {}
		_rs = []
		_lm = [] 
		_am = [] 
		_al = []
		_as = [] 
		_ar = [] 
		_ls = [] 
		_ms = [] 
		_rl = [] 
		_rm = [] 

		for k,v in data.iteritems():
			for key,value in v.iteritems():
				if key == "rs":
					_rs.append(value)
				elif key == "lm":	
					_lm.append(value)
				elif key == "am":
					_am.append(value)
				elif key == "al":
					_al.append(value)
				elif key == "as":
					_as.append(value)
				elif key == "ar":
					_ar.append(value)
				elif key == "ls":
					_ls.append(value)
				elif key == "ms":
					_ms.append(value)
				elif key == "rl":
					_rl.append(value)
				elif key == "rm":
					_rm.append(value)
		plot_jaccard_over_edges(_rs,output,metric,"Retweets and Followers")
		plot_jaccard_over_edges(_lm,output,metric,"Likes and Mentions")
		plot_jaccard_over_edges(_am,output,metric,"Following and Mentions")
		plot_jaccard_over_edges(_al,output,metric,"Following and Likes")
		plot_jaccard_over_edges(_as,output,metric,"Following and Followers")
		plot_jaccard_over_edges(_ar,output,metric,"Following and Retweets")
		plot_jaccard_over_edges(_ls,output,metric,"Likes and Followers")
		plot_jaccard_over_edges(_ms,output,metric,"Mentions and Followers")
		plot_jaccard_over_edges(_rl,output,metric,"Retweets and Likes")
		plot_jaccard_over_edges(_rm,output,metric,"Retweets and Mentions")
					
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" Plotar gráficos sobre as métricas e propriedades calculadas - Multilayer			"
	print"																											"
	print"#################################################################################"
	print
	metric = "jaccard_set_edges"
	if not os.path.exists(str(data_dir)+str(metric)+".json"):																				# Verifica se diretório existe
		print ("Impossível localizar arquivo: "+str(data_dir)+str(metric)+".json")
	else:
		file = str(data_dir)+str(metric)+".json"
		output =str(output_dir)+str(metric)+"/"
		create_dirs(output)
		print_data_jaccard_over_vertives(metric,file,output)

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

data_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/json/"	# Diretório com arquivos JSON com métricas e propriedades Calculadas
output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/"	# Diretório para Salvar os gráficos...

#Executa o método main
if __name__ == "__main__": main()