# -*- coding: latin1 -*-
################################################################################################
#	
#
import calc
import sys, time, json, os, os.path
import numpy as np
from math import*
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib as mpl
import pylab
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import pandas_datareader
from pandas_datareader import data, wb
from pandas import Series, DataFrame
pd.__version__


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
def plotly_overlapping_vertices(data,output,name,pairs):
	print ("\nCriando histograma dinâmico...")
	print ("Salvando dados em: "+str(output)+"\n")

	trace = go.Histogram(x=data, name="vertices", marker=dict(color='green'))
	_data = [trace]
	layout = go.Layout(title="Overlapping Vertices - "+str(pairs), xaxis=dict(title='Overlapping Degree'),yaxis=dict(title="Egos"))    
	fig = go.Figure(data=_data, layout=layout)

	plotly.offline.plot(fig, filename=output+pairs+".html",auto_open=False)

	print (" - OK! Histograma salvo em: "+str(output))
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def plot_overlapping_vertices(data,output,name,pairs):
	print ("\nCriando histograma...")
	print ("Salvando dados em: "+str(output)+"\n")
	plt.hist(data,color='green')
	plt.xlabel ("Overlapping Degree")
	plt.ylabel ("Egos")
	plt.title ("Overlapping Vertices - "+str(pairs))
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
def print_data_overlapping_vertives(metric,file,output):
	with open(file,'r') as f:
		data = json.load(f)
		pairs = {}

		_aa = []
		_as = [] 
		_ar = []
		_al = [] 
		_am = []

		_sa = []
		_ss = []
		_sr = []
		_sl = []
		_sm = []
								
		_ra = []
		_rs = []
		_rr = []
		_rl = []
		_rm = []
								
		_la = []
		_ls = []
		_lr = []
		_ll = []						
		_lm = []

		_ma = []
		_ms = [] 
 		_mr = [] 
		_ml = [] 
		_mm = [] 
		
		for k,v in data.iteritems():
			for key,value in v.iteritems():
				if key == "aa":
					_aa.append(value)
				elif key == "as":	
					_as.append(value)
				elif key == "ar":
					_ar.append(value)
				elif key == "al":
					_al.append(value)
				elif key == "am":
					_am.append(value)
					
				elif key == "sa":
					_sa.append(value)
				elif key == "ss":
					_ss.append(value)
				elif key == "sr":
					_sr.append(value)
				elif key == "sl":
					_sl.append(value)
				elif key == "sm":
					_sm.append(value)
					
				elif key == "ra":
					_ra.append(value)
				elif key == "rs":
					_rs.append(value)
				elif key == "rr":
					_rr.append(value)
				elif key == "rl":
					_rl.append(value)
				elif key == "rm":
					_rm.append(value)

				elif key == "la":
					_la.append(value)
				elif key == "ls":
					_ls.append(value)
				elif key == "lr":
					_lr.append(value)
				elif key == "ll":
					_ll.append(value)
				elif key == "lm":
					_lm.append(value)

				elif key == "ma":
					_ma.append(value)
				elif key == "ms":
					_ms.append(value)
				elif key == "mr":
					_mr.append(value)
				elif key == "ml":
					_ml.append(value)
				elif key == "mm":
					_mm.append(value)
					
	plot_overlapping_vertices(_aa,output,metric,"Following and Following")
	plot_overlapping_vertices(_as,output,metric,"Following and Followers")
	plot_overlapping_vertices(_ar,output,metric,"Following and Retweets")
	plot_overlapping_vertices(_al,output,metric,"Following and Likes")
	plot_overlapping_vertices(_am,output,metric,"Following and Mentions")

	plot_overlapping_vertices(_sa,output,metric,"Followers and Following")
	plot_overlapping_vertices(_ss,output,metric,"Followers and Followers")
	plot_overlapping_vertices(_sr,output,metric,"Followers and Retweets")
	plot_overlapping_vertices(_sl,output,metric,"Followers and Likes")
	plot_overlapping_vertices(_sm,output,metric,"Followers and Mentions")
		
	plot_overlapping_vertices(_ra,output,metric,"Retweets and Following")
	plot_overlapping_vertices(_rs,output,metric,"Retweets and Followers")
	plot_overlapping_vertices(_rr,output,metric,"Retweets and Retweets")
	plot_overlapping_vertices(_rl,output,metric,"Retweets and Likes")
	plot_overlapping_vertices(_rm,output,metric,"Retweets and Mentions")
		
	plot_overlapping_vertices(_la,output,metric,"Likes and Following")
	plot_overlapping_vertices(_ls,output,metric,"Likes and Followers")
	plot_overlapping_vertices(_lr,output,metric,"Likes and Retweets")
	plot_overlapping_vertices(_ll,output,metric,"Likes and Likes")
	plot_overlapping_vertices(_lm,output,metric,"Likes and Mentions")
		
	plot_overlapping_vertices(_ma,output,metric,"Mentions and Following")
	plot_overlapping_vertices(_ms,output,metric,"Mentions and Followers")
	plot_overlapping_vertices(_mr,output,metric,"Mentions and Retweets")
	plot_overlapping_vertices(_ml,output,metric,"Mentions and Likes")
	plot_overlapping_vertices(_mm,output,metric,"Mentions and Mentions")
				
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
	metric = "overlapping_vertices"
	if not os.path.exists(str(data_dir)+str(metric)+".json"):																				# Verifica se diretório existe
		print ("Impossível localizar arquivo: "+str(data_dir)+str(metric)+".json")
	else:
		file = str(data_dir)+str(metric)+".json"
		output =str(output_dir)+str(metric)+"/"
		create_dirs(output)
		print_data_overlapping_vertives(metric,file,output)

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