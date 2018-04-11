# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
#Calculadora copiada da net...
import calc	
import plotly
import plotly.plotly as py
import plotly.graph_objs as go				


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular o métricas básicas como numero de vértices, arestas, densidade, etc. e armazenar em um arquivo texto.
##								- Considerar apenas redes-ego com a presença do ego.
##								- Calcula-se as métricas a partir da lista de arestas...
## 
##	INPUT: Redes-ego
##
## Output: arquivo texto. Formato:
##
##ID_ego a:amigos s:seguidores r:retuítes l:likes m:menções 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cria diretórios
#
######################################################################################################################################################################
def create_dir(x):
	if not os.path.exists(x):
		os.makedirs(x)

######################################################################################################################################################################
#
# Box Plot
#
######################################################################################################################################################################
def box_plot(_a,_s,_r,_l,_m, metric,title):
	output = str(output_dir)+"/"+str(metric)+"/"
	create_dir(output)	
	
	trace0 = go.Box(y=_a,name='Following',boxmean='sd')
	trace1 = go.Box(y=_s,name='Followers',boxmean='sd')
	trace2 = go.Box(y=_r,name='Retweets',boxmean='sd')
	trace3 = go.Box(y=_l,name='Likes',boxmean='sd')
	trace4 = go.Box(y=_m,name='Mentions',boxmean='sd')
	
	data = [trace0, trace1, trace2, trace3, trace4]

	title_plot = title
	layout = go.Layout(title=title_plot)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(metric)+"box_plot.html",auto_open=True)
	
	
	pass
	
######################################################################################################################################################################
#
# Prepara os dados
#
######################################################################################################################################################################
def prepare(dataset,metric,title):
	_a = []
	_s = [] 
	_r = [] 
	_l = []
	_m = [] 

	for k,v in dataset.iteritems():					# Para cada vértice...
		for key,value in v.iteritems():				# Para cada layer em cada vértice
			if key == "a":
				_a.append(value)
			elif key == "s":	
				_s.append(value)
			elif key == "r":
				_r.append(value)
			elif key == "l":
				_l.append(value)
			elif key == "m":
				_m.append(value)
	
	box_plot(_a,_s,_r,_l,_m, metric,title)
	
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
	print" Plot Basic Net Structure																	"
	print"																											"
	print"#################################################################################"
	print
	print"  1 - Nodes"
	print"  2 - Edges"
	print"  3 - Size"
	print"  4 - Average Degree"
	print"  5 - Diameter"
	print"  6 - Density"
	print"  7 - Closeness Centrality"				
	print"  8 - Betweenness Centrality Nodes"
	print"  9 - Betweenness Centrality Edges"
	print"  10 - Clustering Coefficient"
			
	print("\n")
	op = int(raw_input("Escolha uma opção acima: "))

	if op == 1:
		metric = "nodes"
		title = "Number of Nodes"
	elif op == 2:
		metric = "edges"
		title = "Number of Edges"
	elif op == 3:
		metric = "size"
		title = "Network Size"
	elif op == 4:
		metric = "avg_degree"
		title = "Average Degree of Nodes"
	elif op == 5:
		metric = "diameter"
		title = "Diamenter"
	elif op == 6:
		metric = "density"
		title = "Density"
	elif op == 7:
		metric = "closeness_centr"
		title = "Closeness Centrality"
	elif op == 8:
		metric = "betweenness_centr_nodes"
		title = "Nodes Betweenness Centrality"
	elif op == 9:
		metric = "betweenness_centr_edges"
		title = "Edges Betweenness Centrality"
	elif op == 10:
		metric = "clust_coef"
		title = "Clustering Coefficient"
	else:
		metric = 0
		print("Opção inválida! Saindo...")
		sys.exit()													
	
	if not os.path.exists(str(source_dir)+str(metric)+".json"):
		print ("Arquivo não encontrado! "+str(source_dir)+str(metric)+".json")
	else:
		create_dir(output_dir)																				# Cria diretótio para salvar arquivos.
		with open(str(source_dir)+str(metric)+".json",'r') as f:	
			dataset = json.load(f)			
		prepare(dataset,metric,title)
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/json/"
output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/"

#Executa o método main
if __name__ == "__main__": main()