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
##		Status - Versão 1 - Plotar as medidas usadas no cálculo de Small World
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
def box_plot(_a,_r,_l,_m, metric):	

	if metric == "avg_spl_G":
		name_yaxis = "Average Shortest Path Length"
	elif metric == "S":
		name_yaxis = "S"
	elif metric == "transitivity_G":
		name_yaxis = "Transitivity"		
	else:
		name_yaxis = " "
	trace1 = go.Box(y=_a,name='Follow',boxmean='sd')
	trace2 = go.Box(y=_r,name='Retweet',boxmean='sd')
	trace3 = go.Box(y=_l,name='Like',boxmean='sd')
	trace4 = go.Box(y=_m,name='Mention',boxmean='sd')

	data = [trace1, trace2, trace3, trace4]

	layout = go.Layout(showlegend=False)
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig, filename=output_dir+str(metric)+"_box_plot.html",auto_open=True)


######################################################################################################################################################################
#
# Prepara os dados
#
######################################################################################################################################################################
def prepare(n1,n2,n3,n4):
	print len(n1),len(n2),len(n3),len(n4)
	print
	metrics = ["avg_spl_G","S","transitivity_G"]
	for metric in metrics:
		_a = []
		_r = [] 
		_l = []
		_m = [] 
		for line in n1:
			data = json.loads(line)
			for k,v in data.iteritems():
				_a.append(v[metric])					# Vetor da camada Mentions
		print metric, _a

		for line in n2:
			data = json.loads(line)
			for k,v in data.iteritems():
				_r.append(v[metric])					# Vetor da camada Mentions
		print metric, _r

		for line in n3:
			data = json.loads(line)
			for k,v in data.iteritems():
				_l.append(v[metric])					# Vetor da camada Mentions
		print metric, _l

		for line in n4:
			data = json.loads(line)
			for k,v in data.iteritems():
				_m.append(v[metric])					# Vetor da camada Mentions
		print metric,_m
		print
	
		box_plot(_a,_r,_l,_m, metric)
	
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
	print" Plot Values of Small World																	"
	print"																											"
	print"#################################################################################"
	print
	if not os.path.exists(str(source_dir)+"n1.json") or not os.path.exists(str(source_dir)+"n2.json") or not os.path.exists(str(source_dir)+"n3.json") or not os.path.exists(str(source_dir)+"n4.json"):
		print ("Arquivos não encontrados em: "+str(source_dir))
	else:
		create_dir(output_dir)																				# Cria diretótio para salvar arquivos.
		f1 = open(str(source_dir)+"n1.json",'r')
		f2 = open(str(source_dir)+"n2.json",'r')
		f3 = open(str(source_dir)+"n3.json",'r')
		f4 = open(str(source_dir)+"n4.json",'r')
		
		n1 = f1.readlines()
		n2 = f2.readlines()
		n3 = f3.readlines()
		n4 = f4.readlines()

		if len(n1) != len(n2) and len(n1) != len(n3) and len(n1) != len(n4):
			print ("Diferentes números de egos entre as camadas... Saindo")
			sys.exit()
		else:  	
			prepare(n1,n2,n3,n4)	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world/"
output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/unweighted_directed/small_world/"

#Executa o método main
if __name__ == "__main__": main()