# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import plotly
import plotly.plotly as py
import plotly.graph_objs as go				


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Plotar os dados de acordo com os dados calculados sobre a sobreposição entre listas e conjunto de vértices...
##
##		Para cada arquivo da sobreposição (jaccard, overlap_lists, overlap_alters): ID_ego a:amigos s:seguidores r:retuítes l:likes m:menções
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
	output = str(output_dir)+"/"
	create_dir(output)	
		
	if metric == "overlap_top_k":	
		#trace0 = go.Box(y=_a,name='Follow',boxmean='sd')
		#trace1 = go.Box(y=_s,name='Followee',boxmean='sd')
		trace2 = go.Box(y=_r,name='Retweets',boxmean='sd')
		trace3 = go.Box(y=_l,name='Likes',boxmean='sd')
		trace4 = go.Box(y=_m,name='Mentions',boxmean='sd')
		data = [trace2, trace3, trace4]
	else:
		trace0 = go.Box(y=_a,name='Follow',boxmean='sd')
		trace1 = go.Box(y=_s,name='Followee',boxmean='sd')
		trace2 = go.Box(y=_r,name='Retweets',boxmean='sd')
		trace3 = go.Box(y=_l,name='Likes',boxmean='sd')
		trace4 = go.Box(y=_m,name='Mentions',boxmean='sd')
		data = [trace0, trace1, trace2, trace3, trace4]

	title_plot = title
	layout = go.Layout(title=title_plot)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(metric)+"_box_plot.html",auto_open=True)
	
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
	print" Plot Overlap"
	print"																											"
	print"#################################################################################"
	print
	
	metrics = ["jaccard","overlap_lists","overlap_alters","overlap_top_k"]
	for metric in metrics:
		if metric == "jaccard":
			title = "Jaccard"
		elif metric == "overlap_lists":
			title = "Intersection over Lists Set"
		elif metric == "overlap_alters":
			title = "Intersection over Alters Set"
		elif metric == "overlap_top_k":
			title = "Intersection over Top-K Alters Set"	
				
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

type_graphs1 = "graphs_with_ego"
type_graphs2 = "graphs_without_ego"
singletons1 = "full"
singletons2 = "without_singletons"

source_dir = "/home/amaury/Dropbox/lists_properties/"+str(type_graphs1)+"_"+str(singletons1)+"/json/"
output_dir = "/home/amaury/Dropbox/lists_properties_statistics/"+str(type_graphs1)+"_"+str(singletons1)+"/"

#Executa o método main
if __name__ == "__main__": main()