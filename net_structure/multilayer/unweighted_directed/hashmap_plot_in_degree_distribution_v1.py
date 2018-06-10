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
import powerlaw
import matplotlib.pyplot as plt		


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para plotar os dados de in-degree distribution
##								- Considerar apenas redes-ego com a presença do ego.
## 
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
# histogram
#
######################################################################################################################################################################
def histogram_plot(_a,_s,_r,_l,_m, metric):
	output = str(output_dir)+"/"+str(metric)+"/"
	create_dir(output)	
	
	trace0 = go.Histogram(x=_a,name='Follow',opacity=0.75)
	trace1 = go.Histogram(x=_s,name='Followee',opacity=0.75)
	trace2 = go.Histogram(x=_r,name='Retweets',opacity=0.75)
	trace3 = go.Histogram(x=_l,name='Likes',opacity=0.75)
	trace4 = go.Histogram(x=_m,name='Mentions',opacity=0.75)
	
	data = [trace0, trace1, trace2, trace3, trace4]


	layout = go.Layout(barmode='overlay')
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(metric)+"_histogram.html",auto_open=True)
	
######################################################################################################################################################################
#
# CCDF Plot
#
######################################################################################################################################################################
def ccdf_plot(_a,_s,_r,_l,_m, metric):
	output = str(output_dir)+"/"+str(metric)+"/"
	create_dir(output)	
	
	fit_a = powerlaw.Fit(_a)
	fit_s = powerlaw.Fit(_s)
	fit_r = powerlaw.Fit(_r)
	fit_l = powerlaw.Fit(_l)
	fit_m = powerlaw.Fit(_m)

	fig = fit_a.plot_ccdf(linewidth=3, marker='+', label='Follow')
	fit_s.plot_ccdf(ax=fig, marker='^', label='Followers')
	fit_r.plot_ccdf(ax=fig, marker='*', label='Retweets')
	fit_l.plot_ccdf(ax=fig, marker='s', label='Likes')
	fit_m.plot_ccdf(ax=fig, marker='o', label='Mentions')
	####
	fig.set_ylabel(u"p(X>=x)")
	fig.set_xlabel("alpha")
	handles, labels = fig.get_legend_handles_labels()
	fig.legend(handles, labels, loc=3)
	figname = 'CCDF_alpha_Distribution'
	plt.savefig(str(output)+str(figname)+'.eps', bbox_inches='tight')
	plt.close()	

######################################################################################################################################################################
#
# Box Plot
#
######################################################################################################################################################################
def box_plot(_a,_s,_r,_l,_m, metric):
	output = str(output_dir)+"/"+str(metric)+"/"
	create_dir(output)	
	
	trace0 = go.Box(y=_a,name='Follow',boxmean='sd')
	trace1 = go.Box(y=_s,name='Followee',boxmean='sd')
	trace2 = go.Box(y=_r,name='Retweets',boxmean='sd')
	trace3 = go.Box(y=_l,name='Likes',boxmean='sd')
	trace4 = go.Box(y=_m,name='Mentions',boxmean='sd')
	
	data = [trace0, trace1, trace2, trace3, trace4]

	fig = go.Figure(data=data)

	plotly.offline.plot(fig, filename=output+str(metric)+"_box_plot.html",auto_open=True)
	
######################################################################################################################################################################
#
# Prepara os dados
#
######################################################################################################################################################################
def prepare(dataset,metric):
	_a = []
	_s = [] 
	_r = [] 
	_l = []
	_m = [] 

	for ego,data in dataset.iteritems():				# Para cada ego...
		for key,value in data.iteritems():				# Para cada layer em cada ego
			if key == "a":
				_a.append(value['alpha'])
			elif key == "s":	
				_s.append(value['alpha'])
			elif key == "r":
				_r.append(value['alpha'])
			elif key == "l":
				_l.append(value['alpha'])
			elif key == "m":
				_m.append(value['alpha'])
#				if value['alpha'] > 50:
#					print ego,value

	histogram_plot(_a,_s,_r,_l,_m, metric)		
	ccdf_plot(_a,_s,_r,_l,_m, metric)	
	box_plot(_a,_s,_r,_l,_m, metric)
	
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
	print" Plot In-Degree Distribution"
	print"																											"
	print"#################################################################################"
	print
	
	metric = "in_degree_distribution"
	if not os.path.exists(str(source_dir)+str(metric)+".json"):
		print ("Arquivo não encontrado! "+str(source_dir)+str(metric)+".json")
	else:
		create_dir(output_dir)																				# Cria diretótio para salvar arquivos.
		with open(str(source_dir)+str(metric)+".json",'r') as f:	
			dataset = json.load(f)			
		prepare(dataset,metric)
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/"
output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/unweighted_directed/"

#Executa o método main
if __name__ == "__main__": main()