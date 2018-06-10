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
##		Status - Versão 1 - Plotar os dados da co-ocorrência dos dados entre as camadas usando grouped Boxplot
##
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

#####################################################################################################################################################################
# Grouped Box Plot
######################################################################################################################################################################
def box_plot(metric,_aa,_as,_ar,_al,_am,_sa,_ss,_sr,_sl,_sm,_ra,_rs,_rr,_rl,_rm,_la,_ls,_lr,_ll,_lm,_ma,_ms,_mr,_ml,_mm,title):
	print ("\nCriando Box Plot...")
	print ("Salvando dados em: "+str(output_dir)+"\n")
	x = []
	y0 = []						#Follow
	y1 = []						#Retweets
	y2 = []						#Likes
	y3 = []						#Mentions
	
#	for i in range(len(_aa)):
#		x.append("Follow")
	for i in range(len(_ar)):
		x.append("Retweets")
	for i in range(len(_al)):
		x.append("Likes")
	for i in range(len(_am)):
		x.append("Mentions")

#	for i in _aa:
#		y0.append(i)
	for i in _ar:
		y0.append(i)
	for i in _al:
		y0.append(i)
	for i in _am:
		y0.append(i)

#	for i in _ra:
#		y1.append(i)
	for i in _rr:
		y1.append(i)
	for i in _rl:
		y1.append(i)
	for i in _rm:
		y1.append(i)
				

#	for i in _la:
#		y2.append(i)
	for i in _lr:
		y2.append(i)
	for i in _ll:
		y2.append(i)
	for i in _lm:
		y2.append(i)
	
#	for i in _ma:
#		y3.append(i)
	for i in _mr:
		y3.append(i)
	for i in _ml:
		y3.append(i)
	for i in _mm:
		y3.append(i)		
							
	trace0 = go.Box(y=y0,x=x,name='Follow',boxmean='sd')
	trace1 = go.Box(y=y1,x=x,name='Retweets',boxmean='sd')
	trace2 = go.Box(y=y2,x=x,name='Likes',boxmean='sd')
	trace3 = go.Box(y=y3,x=x,name='Mentions',boxmean='sd')

	title_plot = title
	data = [trace0, trace1, trace2,trace3]
	layout = go.Layout(title=title_plot,yaxis=dict(title='Top-K Alters',zeroline=False),boxmode='group')

	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output_dir+str(metric)+"_box_plot.html",auto_open=True)
	print (" - OK! Imagem salva em: "+str(output_dir))
	print

######################################################################################################################################################################
#
# Plotar Gŕaficos relacionados aos dados
#
######################################################################################################################################################################
def prepare(metric,file,title):
	with open(file,'r') as f:
		data = json.load(f)
 
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

			else:
				print ("Rede inválida")
				sys.exit()		

	box_plot(metric,_aa,_as,_ar,_al,_am,_sa,_ss,_sr,_sl,_sm,_ra,_rs,_rr,_rl,_rm,_la,_ls,_lr,_ll,_lm,_ma,_ms,_mr,_ml,_mm,title)	
		
	
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
	metric = "top_k_co_occurrence"
	title = "Top-K Intersection over Alters Set"	
	if not os.path.exists(str(data_dir)+str(metric)+".json"):												# Verifica se diretório existe
		print ("Impossível localizar arquivo: "+str(data_dir)+str(metric)+".json")
	else:
		file = str(data_dir)+str(metric)+".json"
		prepare(metric,file,title)

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
print "\n#######################################################################\n"	
type_graphs1 = "graphs_with_ego"
type_graphs2 = "graphs_without_ego"
singletons1 = "full"
singletons2 = "without_singletons"
#######################################################################
	
data_dir = "/home/amaury/Dropbox/lists_properties/"+str(type_graphs1)+"_"+str(singletons1)+"/"
output_dir = "/home/amaury/Dropbox/lists_properties_statistics/"+str(type_graphs1)+"_"+str(singletons1)+"/"

#Executa o método main
if __name__ == "__main__": main()