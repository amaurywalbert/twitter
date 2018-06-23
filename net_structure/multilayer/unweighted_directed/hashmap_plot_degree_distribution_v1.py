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
#Grouped Box Plot
#
######################################################################################################################################################################
def grouped_box_plot(_a,_s,_r,_l,_m, metric):		#Separar por conjuntos alpha<2, 2<alpha<3, 3<alpha
	output = str(output_dir)+"/"+str(metric)+"/"
	create_dir(output)	
	
	data = {"a":_a, "r":_r,"l":_l,"m":_m}
	dataset = {}
	for key,value in data.iteritems():
		normal = []
		heavy_tailed = []
		scale_free = []
		ultra_small_world = []
			
		for item in value:		
			if item < 0:
				normal.append(item)	
			elif item < 2 and item >= 0:
				heavy_tailed.append(item)
			elif item >=2 and item <=3:
				scale_free.append(item)
			else:	
				ultra_small_world.append(item)
		dataset[key] = {"normal":normal, "heavy_tailed":heavy_tailed, "scale_free":scale_free,"ultra_small_world":ultra_small_world}
	 
	x1 = []
	y1 = []
	frequence = []
	for key,values in dataset.iteritems():
		if key == 'a':
			layer = "Follow"
		elif key == 'r':
			layer = "Retweets"
		elif key == 'l':
			layer = "Likes"
		elif key == 'm':
			layer = "Mentions"
		else:
			layer = ""
			print "Error"
			sys.exit()											
		for alpha in values['heavy_tailed']:
			x1.append(layer)			
			y1.append(alpha)

	x2 = []
	y2 = []
	for key,values in dataset.iteritems():
		if key == 'a':
			layer = "Follow"
		elif key == 'r':
			layer = "Retweets"
		elif key == 'l':
			layer = "Likes"
		elif key == 'm':
			layer = "Mentions"
		else:
			layer = ""
			print "Error"
			sys.exit()											
		for alpha in values['scale_free']:
			x2.append(layer)			
			y2.append(alpha)

	x3 = []
	y3 = []
	for key,values in dataset.iteritems():
		if key == 'a':
			layer = "Follow"
		elif key == 'r':
			layer = "Retweets"
		elif key == 'l':
			layer = "Likes"
		elif key == 'm':
			layer = "Mentions"
		else:
			layer = ""
			print "Error"
			sys.exit()											
		for alpha in values['ultra_small_world']:
			x3.append(layer)			
			y3.append(alpha)

	trace1 = go.Box(x=x1,y=y1,name='$0<\gamma<2$',boxmean='sd')
	trace2 = go.Box(x=x2,y=y2,name='$2\leq\gamma\leq3$',boxmean='sd')
	trace3 = go.Box(x=x2,y=y3,name='$3<\gamma$',boxmean='sd')

	data = [trace3, trace2, trace1]

	layout = go.Layout(boxmode='group')
	fig = go.Figure(data=data, layout=layout)

#	plotly.offline.plot(fig, filename=output+str(metric)+"_grouped_box_plot.html",auto_open=True)

######################################################################################################################################################################
######################################################################################################################################################################
	x = ["Follow","Retweets","Likes","Mentions"]
	f1 = []
	f2 = []
	f3 = []
	
	f1.append(len(dataset['a']["heavy_tailed"]))
	f1.append(len(dataset['r']["heavy_tailed"]))
	f1.append(len(dataset['l']["heavy_tailed"]))
	f1.append(len(dataset['m']["heavy_tailed"]))
	
	f2.append(len(dataset['a']["scale_free"]))
	f2.append(len(dataset['r']["scale_free"]))
	f2.append(len(dataset['l']["scale_free"]))
	f2.append(len(dataset['m']["scale_free"]))
	
	f3.append(len(dataset['a']["ultra_small_world"]))
	f3.append(len(dataset['r']["ultra_small_world"]))
	f3.append(len(dataset['l']["ultra_small_world"]))
	f3.append(len(dataset['m']["ultra_small_world"]))
	
#	trace1 = go.Bar(x=x,y=f1,name='$0<\gamma<2$')
#	trace2 = go.Bar(x=x,y=f2,name='$2\leq\gamma\leq3$')
#	trace3 = go.Bar(x=x,y=f3,name='$3<\gamma$')

	trace1 = go.Bar(x=x,y=f1,name='0 < '+u'\u03B3'+' < 2')
	trace2 = go.Bar(x=x,y=f2,name='2 ≤ '+u'\u03B3'+' ≤ 3')
	trace3 = go.Bar(x=x,y=f3,name='3 < '+u'\u03B3')

	data = [trace1, trace2, trace3]

	layout = go.Layout(barmode='group')
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(metric)+"_grouped_bar_plot.html",auto_open=True)

	
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

		
#	ccdf_plot(_a,_s,_r,_l,_m, metric)	
	grouped_box_plot(_a,_s,_r,_l,_m, metric)
	
	
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
	print" Plot Degree Distribution"
	print"																											"
	print"#################################################################################"
	print
	
	#metrics = ["in_degree_distribution","out_degree_distribution","total_degree_distribution"]
	metrics = ["in_degree_distribution"]
	for metric in metrics:
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