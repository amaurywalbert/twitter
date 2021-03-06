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
def box_plot(n1,n2,n3,n4):
	metrics = ["coef_clust_G","avg_spl_G_paths_exists"]
	for metric in metrics:
		if metric == "coef_clust_G":
			rnd_metric = "coef_clust_Gnm"
		elif metric == "avg_spl_G_paths_exists":
			rnd_metric = "avg_spl_Gnm_paths_exists"
		x = []
		y1 = []						# G
		y2 = []						# Random G	

		for i in range(len(n1)):
			x.append("Follow")
		for i in range(len(n2)):
			x.append("Retweet")
		for i in range(len(n3)):
			x.append("Like")
		for i in range(len(n4)):
			x.append("Mention")

		for line in n1:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y1.append(v[metric])
		for line in n2:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y1.append(v[metric])
		for line in n3:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y1.append(v[metric])
		for line in n4:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y1.append(v[metric])

		for line in n1:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y2.append(v[rnd_metric])
		for line in n2:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y2.append(v[rnd_metric])
		for line in n3:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y2.append(v[rnd_metric])
		for line in n4:
			data = json.loads(line)
			for k,v in data.iteritems():			
				y2.append(v[rnd_metric])


		trace1 = go.Box(y=y1,x=x,name='Graph G',boxmean='sd')
		trace2 = go.Box(y=y2,x=x,name='Random Graph G',boxmean='sd')

		data = [trace1, trace2]
		layout = go.Layout(boxmode='group')

		fig = go.Figure(data=data, layout=layout)

		fig = go.Figure(data=data, layout=layout)
		plotly.offline.plot(fig, filename=output_dir+str(metric)+"_box_plot.html",auto_open=True)

######################################################################################################################################################################
#
#Grouped Bar Plot
#
######################################################################################################################################################################
def grouped_bar_plot(_a,_r,_l,_m, metric):		#Separar por conjuntos S<1 1<=S

	dataset = {}
######################### Follow
	smaller_a = []
	bigger_a = []
	for item in _a:		
		if item < 1:
			smaller_a.append(item)
		else:	
			bigger_a.append(item)
	dataset["a"] = {"not_small_world":smaller_a, "small_world":bigger_a}
	 
######################### Retweet
	smaller_r = []
	bigger_r = []
	for item in _r:		
		if item < 1:
			smaller_r.append(item)
		else:	
			bigger_r.append(item)
	dataset["r"] = {"not_small_world":smaller_r, "small_world":bigger_r}
	
######################### Like
	smaller_l = []
	bigger_l = []
	for item in _l:		
		if item < 1:
			smaller_l.append(item)
		else:	
			bigger_l.append(item)
	dataset["l"] = {"not_small_world":smaller_l, "small_world":bigger_l}
	
######################### Mention
	smaller_m = []
	bigger_m = []
	for item in _m:		
		if item < 1:
			smaller_m.append(item)
		else:	
			bigger_m.append(item)
	dataset["m"] = {"not_small_world":smaller_m, "small_world":bigger_m}	

#################################################################################
	x = ["Follow","Retweet","Like","Mention"]
	f1 = []
	f2 = []
	
	f1.append(len(dataset['a']["not_small_world"]))
	f1.append(len(dataset['r']["not_small_world"]))
	f1.append(len(dataset['l']["not_small_world"]))
	f1.append(len(dataset['m']["not_small_world"]))
	
	f2.append(len(dataset['a']["small_world"]))
	f2.append(len(dataset['r']["small_world"]))
	f2.append(len(dataset['l']["small_world"]))
	f2.append(len(dataset['m']["small_world"]))


	trace1 = go.Bar(x=x,y=f1,name='S < 1')
	trace2 = go.Bar(x=x,y=f2,name='1 ≤ S')

	data = [trace1, trace2]

	layout = go.Layout(barmode='group')
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output_dir+"small_world.html",auto_open=True)


######################################################################################################################################################################
#
# Prepara os dados
#
######################################################################################################################################################################
def prepare(n1,n2,n3,n4):

	if op == 1:
		metrics = ["transitivity_G","transitivity_Gnm","avg_spl_Gnm","S","avg_spl_G"]
	else:
		metrics = ["coef_clust_G","coef_clust_Gnm","avg_spl_G_paths_exists","avg_spl_Gnm_paths_exists","avg_spl_G_all_paths","avg_spl_Gnm_all_paths","S_all_paths","S_path_exists"]
	for metric in metrics:
		_a = []
		_r = [] 
		_l = []
		_m = [] 
		for line in n1:
			data = json.loads(line)
			for k,v in data.iteritems():
				_a.append(v[metric])					# Vetor da camada Mentions
#		print metric, _a

		for line in n2:
			data = json.loads(line)
			for k,v in data.iteritems():
				_r.append(v[metric])					# Vetor da camada Mentions
#		print metric, _r

		for line in n3:
			data = json.loads(line)
			for k,v in data.iteritems():
				_l.append(v[metric])					# Vetor da camada Mentions
#		print metric, _l

		for line in n4:
			data = json.loads(line)
			for k,v in data.iteritems():
				_m.append(v[metric])					# Vetor da camada Mentions
#		print metric,_m
#		print
#		if metric == "S" or metric == "S_all_paths" or metric == "S_path_exists":
		if metric == "S" or metric == "S_path_exists":
			grouped_bar_plot(_a,_r,_l,_m, metric)
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
	print"																										"
	print" Plot Values of Small World																	"
	print"																										"
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
			print ("Quantidade de redes-egos em cada camada: n1 / n2 / n3 / n4")
			print len(n1),len(n2),len(n3),len(n4)
		
			prepare(n1,n2,n3,n4)
			box_plot(n1,n2,n3,n4)

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
os.system('clear')
print "################################################################################"
print"																											"
print" Merge Results of S metric for five egos sets in one file								"
print" 			ONLY FOLLOW LAYER								"
print"																											"
print"#################################################################################"
print
print
print"  1 - NetworkX - Directed"
print"  2 - SNAP - Directed"
print			
print
op = int(raw_input("Escolha a biblioteca utilizada para calcular a métrica S : "))
	
if op == 1:
	print ("Não utilizado... usando apenas SNAP.")
	sys.exit()	
#	source_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world/"
#	output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/unweighted_directed/small_world/"
elif op == 2: 
	source_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world_snap/"
	output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/unweighted_directed/small_world_snap/"
else:
	print ("Opção inválida...")
	source_dir = " "
	output_dir = source_dir
	sys.exit()
			
#Executa o método main
if __name__ == "__main__": main()




