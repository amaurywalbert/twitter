# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random, math
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import numpy as np
from math import*
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_bars_single(output,data_overview,metric,alg,title):
	print ("\n##################################################\n")
	print ("Gerando Gráficos Individuais - Algoritmo: "+str(alg)+" - Métrica: "+str(metric))
	name = str(alg)+"_"+str(metric)
	
	interaction = []
	value = []
	co_interaction = []
	co_value = []	
	for k, v in data_overview.iteritems():
		if k == 'n1':
			key = 'follow'
			interaction.append(key)
			value.append(round(v[metric], 3))			
		elif k == 'n2':
			key = 'retweets'			
			interaction.append(key)
			value.append(round(v[metric], 3))			
		elif k == 'n3':
			key = 'likes'
			interaction.append(key)
			value.append(round(v[metric], 3))			
		elif k == 'n4':
			key = 'mentions'
			interaction.append(key)
			value.append(round(v[metric], 3))			
		elif k == 'n9':
			key = 'followers'
			interaction.append(key)
			value.append(round(v[metric], 3))
						
		elif k == 'n5':
			key = 'co-follow'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))			
		elif k == 'n6':
			key = 'co-retweets'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))			
		elif k == 'n7':
			key = 'co-likes'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))			
		elif k == 'n8':
			key = 'co-mentions'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))			
		elif k == 'n10':
			key = 'co-followers'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))
			
			
		else:
			print ("Valor incorreto para nome da rede-ego")
			exit()																																						

	for item in co_value:
		value.append(item)
	for item in co_interaction:
		interaction.append(item)
	colors = ['lightblue', 'lightgreen', 'yellow', 'magenta', 'red', 'green', 'blue', 'cyan', 'magenta', 'black'] 	
	data = [value,colors,interaction]
	
	
	xPositions = np.arange(len(data[0]))
	barWidth = 0.50  # Largura da barra

	_ax = plt.axes()  # Cria axes
	_chartBars = plt.bar(xPositions, data[0], barWidth, color=data[1], align='center')  # Gera barras

	for bars in _chartBars:
		# text(x, y, s, fontdict=None, withdash=False, **kwargs)
		_ax.text(bars.get_x() + (bars.get_width() / 2.0), bars.get_height()+0.001, bars.get_height(), ha='center')  # Label acima das barras

	_ax.set_xticks(xPositions)
	_ax.set_xticklabels(data[2])
	
	plt.title(title)	
	plt.xlabel('Rede-ego')
	plt.ylabel(metric)
	plt.legend(_chartBars, data[2])

	output = output+alg+"/"+str(metric)+"/"
	if not os.path.exists(output):
		os.makedirs(output)
	
	plt.savefig(output+str(name)+".png")
	plt.close()

################################################################################################  MANTER -- Dá pra exportar a tabela depois...
	trace1 = go.Bar(x = data[2], y = data[0])

	data = [trace1]
	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='stack')
	fig = go.Figure(data=data, layout=layout)

		
	plotly.offline.plot(fig, filename=output+str(name)+".html",auto_open=False)

######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_bars_full(output,data1,data2,data3,data4,metric,alg):
	title = "Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg)
	name =  str(metric)+"_"+str(alg)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo - Algoritmo: "+str(alg)+" - Métrica: "+str(metric))

	data_overview_full = [data1,data2,data3,data4]
	dataset = {}
	#i = 1										#armazenar dados de plotagem para dataset COM ego e comunidades COM singletons
	#i = 2										#armazenar dados de plotagem para dataset COM ego e comunidades SEM singletons
	#i = 3										#armazenar dados de plotagem para dataset SEM ego e comunidades COM singletons
	#i = 4										#armazenar dados de plotagem para dataset SEM ego e comunidades SEM singletons
	
	i=0

	for data_overview in data_overview_full:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in data_overview.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		 	
		data = [value,interaction,std]
		dataset[i] = data

	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego e comunidades COM singletons
	z = np.array(dataset[2][0])								# recebe os valores para COM ego e comunidades SEM singletons
	k = np.array(dataset[3][0])								# recebe os valores para SEM ego e comunidades COM singletons
	w = np.array(dataset[4][0])								# recebe os valores para SEM ego e comunidades SEM singletons

	y_std = np.array(dataset[1][2])								# recebe os valores para COM ego e comunidades COM singletons
	z_std = np.array(dataset[2][2])								# recebe os valores para COM ego e comunidades SEM singletons
	k_std = np.array(dataset[3][2])								# recebe os valores para SEM ego e comunidades COM singletons
	w_std = np.array(dataset[4][2])								# recebe os valores para SEM ego e comunidades SEM singletons
	
	print y, y_std
	print z, z_std
	print k, k_std
	print w, w_std
		
	ind=np.arange(n)
	width=0.35

	p1=plt.bar(ind-0.1,y,width,color="blue", label='Grafo COM ego')
	p3=plt.bar(ind,k,width,color="lightblue", label='Grafo SEM ego')														## Invertido pra ficar mais facil a visualização no grafo
	p2=plt.bar(ind+0.1,z,width,color="green", label='Grafo COM ego - Comunidade SEM singletons')					## Invertido pra ficar mais facil a visualização no grafo (lembrar de mudar o +0.1)
	p4=plt.bar(ind+0.2,w,width,color="lightgreen", label='Grafo SEM ego - Comunidade SEM singletons')

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()

	if not os.path.exists(output):
		os.makedirs(output)
		
#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="Grafo COM ego", marker=dict(color='blue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="Grafo COM ego - Comunidade SEM singletons", marker=dict(color='green'))
	trace3 = go.Bar(x = dataset[1][1], y = dataset[3][0], error_y=dict(type='data',array=dataset[3][2], color='#E6842A', visible=True), name="Grafo SEM ego", marker=dict(color='lightblue'))
	trace4 = go.Bar(x = dataset[1][1], y = dataset[4][0], error_y=dict(type='data',array=dataset[4][2], color='#E6842A', visible=True), name="Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightgreen'))
	
	data = [trace1, trace3,trace2,trace4]																						## Invertido pra ficar mais facil a visualização no grafo
	
	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(alg)+"_"+str(metric)+".html",auto_open=False)
	
	
	
	
	
##########################################################################################################################################
# Não considera without singletons
##########################################################################################################################################	
def plot_bars_full_without_singletons(output,data1,data2,metric,alg):
	title = "Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg)
	name =  str(metric)+"_"+str(alg)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo - Algoritmo: "+str(alg)+" - Métrica: "+str(metric))

	data_overview_full = [data1,data2,data3,data4]
	dataset = {}
	#i = 1										#armazenar dados de plotagem para dataset COM ego e comunidades COM singletons
	#i = 2										#armazenar dados de plotagem para dataset COM ego e comunidades SEM singletons
	#i = 3										#armazenar dados de plotagem para dataset SEM ego e comunidades COM singletons
	#i = 4										#armazenar dados de plotagem para dataset SEM ego e comunidades SEM singletons
	
	i=0

	for data_overview in data_overview_full:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in data_overview.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		 	
		data = [value,interaction,std]
		dataset[i] = data

	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego e comunidades COM singletons
	z = np.array(dataset[2][0])								# recebe os valores para COM ego e comunidades SEM singletons


	y_std = np.array(dataset[1][2])								# recebe os valores para COM ego e comunidades COM singletons
	z_std = np.array(dataset[2][2])								# recebe os valores para COM ego e comunidades SEM singletons

	
	print y, y_std
	print z, z_std

		
	ind=np.arange(n)
	width=0.35

	p1=plt.bar(ind,y,width,color="blue", label='Grafo COM ego')

	p2=plt.bar(ind+0.1,z,width,color="green", label='Grafo SEM ego')

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()

	if not os.path.exists(output):
		os.makedirs(output)
		
#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="Grafo COM ego", marker=dict(color='blue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="Grafo SEM ego", marker=dict(color='green'))
	
	data = [trace1,trace2]
	
	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(alg)+"_"+str(metric)+".html",auto_open=False)
	
	
	
	
	
		
######################################################################################################################################################################	
######################################################################################################################################################################	
######################################################################################################################################################################	
###############################################################################################################################################################
#
# Plota Gráficos dos dados...
#
###############################################################################################################################################################
def plot_bars_gn(output,data1,data2,metric,alg):
	title = "Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg)
	name =  str(metric)+"_"+str(alg)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo - Algoritmo: "+str(alg)+" - Métrica: "+str(metric))

	data_overview_full = [data1,data2]
	dataset = {}
	#i = 1										#armazenar dados de plotagem para dataset COM ego
	#i = 2										#armazenar dados de plotagem para dataset SEM ego
	
	i=0

	for data_overview in data_overview_full:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in data_overview.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		 	
		data = [value,interaction,std]
		dataset[i] = data

	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego
	z = np.array(dataset[2][0])								# recebe os valores para SEM ego

	y_std = np.array(dataset[1][2])							# recebe os valores para COM ego
	z_std = np.array(dataset[2][2])							# recebe os valores para SEM ego
	
	print y, y_std
	print z, z_std
		
	ind=np.arange(n)
	width=0.35

	p1=plt.bar(ind-0.1,y,width,color="blue", label='Grafo COM ego')
	p2=plt.bar(ind,z,width,color="lightblue", label='Grafo SEM ego')


	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()

	if not os.path.exists(output):
		os.makedirs(output)
		
#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="Grafo COM ego", marker=dict(color='blue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="Grafo COM ego - Comunidade SEM singletons", marker=dict(color='green'))

	
	data = [trace1,trace2]
	
	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(alg)+"_"+str(metric)+".html",auto_open=False)




######################################################################################################################################################################
######################################################################################################################################################################	
######################################################################################################################################################################	
######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_full_algs(output,dataset1,dataset2,metric):
	title = "Avaliação das redes usando a métrica "+str(metric)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo...")

	dataset = {}
	#i = 1										#armazenar dados de plotagem para dataset COM ego e comunidades COM singletons
	#i = 2										#armazenar dados de plotagem para dataset COM ego e comunidades SEM singletons
	#i = 3										#armazenar dados de plotagem para dataset SEM ego e comunidades COM singletons
	#i = 4										#armazenar dados de plotagem para dataset SEM ego e comunidades SEM singletons
	
	i=0

	for array in dataset1:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in array.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		 	
		data1 = [value,interaction,std]
		dataset[i] = data1

	for array in dataset2:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in array.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		 	
		data2 = [value,interaction,std]
		dataset[i] = data2
		
	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego e comunidades COM singletons do primeiro algoritmo
	z = np.array(dataset[2][0])								# recebe os valores para COM ego e comunidades SEM singletons do primeiro algoritmo
	k = np.array(dataset[3][0])								# recebe os valores para SEM ego e comunidades COM singletons do primeiro algoritmo
	w = np.array(dataset[4][0])								# recebe os valores para SEM ego e comunidades SEM singletons do primeiro algoritmo

	y1 = np.array(dataset[5][0])								# recebe os valores para COM ego e comunidades COM singletons do segundo algoritmo
	z1 = np.array(dataset[6][0])								# recebe os valores para COM ego e comunidades SEM singletons do segundo algoritmo
	k1 = np.array(dataset[7][0])								# recebe os valores para SEM ego e comunidades COM singletons do segundo algoritmo
	w1 = np.array(dataset[8][0])								# recebe os valores para SEM ego e comunidades SEM singletons do segundo algoritmo


	ind=np.arange(n)
	width=0.15

	p1=plt.bar(ind-0.4,y,width,color="darkblue", label='COPRA - Grafo COM ego')
	p3=plt.bar(ind-0.3,k,width,color="blue", label='COPRA - Grafo SEM ego')													## Invertido pra ficar mais facil a visualização no grafo
	p2=plt.bar(ind-0.2,z,width,color="royalblue", label='COPRA - Grafo COM ego - Comunidade SEM singletons')					## Invertido pra ficar mais facil a visualização no grafo (lembrar de mudar o +0.1)
	p4=plt.bar(ind-0.1,w,width,color="lightblue", label='COPRA - Grafo SEM ego - Comunidade SEM singletons')
	

	p5=plt.bar(ind+0.1,y1,width,color="darkgreen", label='OSLOM - Grafo COM ego')
	p7=plt.bar(ind+0.2,k1,width,color="green", label='OSLOM - Grafo SEM ego')														## Invertido pra ficar mais facil a visualização no grafo
	p6=plt.bar(ind+0.3,z1,width,color="seagreen", label='OSLOM - Grafo COM ego - Comunidade SEM singletons')					## Invertido pra ficar mais facil a visualização no grafo (lembrar de mudar o +0.1)
	p8=plt.bar(ind+0.4,w1,width,color="lightgreen", label='OSLOM - Grafo SEM ego - Comunidade SEM singletons')

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()	

	if not os.path.exists(output):
		os.makedirs(output)

#	plt.savefig(output+"full_algs_"+str(metric)+".png")
	plt.close()
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="COPRA - Grafo COM ego", marker=dict(color='darkblue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="COPRA - Grafo COM ego - Comunidade SEM singletons", marker=dict(color='royalblue'))
	trace3 = go.Bar(x = dataset[1][1], y = dataset[3][0], error_y=dict(type='data',array=dataset[3][2], color='#E6842A', visible=True), name="COPRA - Grafo SEM ego", marker=dict(color='blue'))
	trace4 = go.Bar(x = dataset[1][1], y = dataset[4][0], error_y=dict(type='data',array=dataset[4][2], color='#E6842A', visible=True), name="COPRA - Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightblue'))

	trace5 = go.Bar(x = dataset[1][1], y = dataset[5][0], error_y=dict(type='data',array=dataset[5][2], color='#E6842A', visible=True), name="OSLOM - Grafo COM ego", marker=dict(color='darkgreen'))
	trace6 = go.Bar(x = dataset[1][1], y = dataset[6][0], error_y=dict(type='data',array=dataset[6][2], color='#E6842A', visible=True), name="OSLOM - Grafo COM ego - Comunidade SEM singletons", marker=dict(color='seagreen'))
	trace7 = go.Bar(x = dataset[1][1], y = dataset[7][0], error_y=dict(type='data',array=dataset[7][2], color='#E6842A', visible=True), name="OSLOM - Grafo SEM ego", marker=dict(color='green'))
	trace8 = go.Bar(x = dataset[1][1], y = dataset[8][0], error_y=dict(type='data',array=dataset[8][2], color='#E6842A', visible=True), name="OSLOM - Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightgreen'))
		
#1f77b4 or rgb(31, 119, 180)
#ff7f0e or rgb(255, 127, 14)
#2ca02c or rgb(44, 160, 44)
#d62728 or rgb(214, 39, 40)
#9467bd or rgb(148, 103, 189)
#8c564b or rgb(140, 86, 75)	
	
	data = [trace1,trace3,trace2,trace4,trace5,trace7,trace6,trace8]																						## Invertido pra ficar mais facil a visualização no grafo

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+"full_algs_"+str(metric)+".html",auto_open=False)
	
######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_full_metrics(output,dataset1,dataset2,alg):
	title = "Avaliação das redes usando o algoritmo "+str(alg)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo...")

	dataset = {}
	#i = 1										#armazenar dados de plotagem para dataset COM ego e comunidades COM singletons
	#i = 2										#armazenar dados de plotagem para dataset COM ego e comunidades SEM singletons
	#i = 3										#armazenar dados de plotagem para dataset SEM ego e comunidades COM singletons
	#i = 4										#armazenar dados de plotagem para dataset SEM ego e comunidades SEM singletons
	
	i=0

	for array in dataset1:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in array.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v['nmi'], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v['nmi'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v['nmi'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v['nmi'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v['nmi'], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v['nmi'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v['nmi'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v['nmi'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v['nmi'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v['nmi'], 3))
				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		 	
		data1 = [value,interaction,std]
		dataset[i] = data1

	for array in dataset2:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in array.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v['jaccard'], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v['jaccard'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v['jaccard'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v['jaccard'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v['jaccard'], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v['jaccard'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v['jaccard'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v['jaccard'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v['jaccard'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v['jaccard'], 3))
				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		 	
		data2 = [value,interaction,std]
		dataset[i] = data2
		
	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego e comunidades COM singletons do primeira métrica
	z = np.array(dataset[2][0])								# recebe os valores para COM ego e comunidades SEM singletons do primeira métrica
	k = np.array(dataset[3][0])								# recebe os valores para SEM ego e comunidades COM singletons do primeiro métrica
	w = np.array(dataset[4][0])								# recebe os valores para SEM ego e comunidades SEM singletons do primeiro métrica

	y1 = np.array(dataset[5][0])								# recebe os valores para COM ego e comunidades COM singletons do segundo métrica
	z1 = np.array(dataset[6][0])								# recebe os valores para COM ego e comunidades SEM singletons do segundo métrica
	k1 = np.array(dataset[7][0])								# recebe os valores para SEM ego e comunidades COM singletons do segundo métrica
	w1 = np.array(dataset[8][0])								# recebe os valores para SEM ego e comunidades SEM singletons do segundo métrica


	ind=np.arange(n)
	width=0.15

	p1=plt.bar(ind-0.4,y,width,color="darkblue", label='NMI - Grafo COM ego')
	p3=plt.bar(ind-0.3,k,width,color="blue", label='NMI - Grafo SEM ego')													## Invertido pra ficar mais facil a visualização no grafo
	p2=plt.bar(ind-0.2,z,width,color="royalblue", label='NMI - Grafo COM ego - Comunidade SEM singletons')					## Invertido pra ficar mais facil a visualização no grafo (lembrar de mudar o +0.1)
	p4=plt.bar(ind-0.1,w,width,color="lightblue", label='NMI - Grafo SEM ego - Comunidade SEM singletons')
	

	p5=plt.bar(ind+0.1,y1,width,color="darkgreen", label='JACCARD - Grafo COM ego')
	p7=plt.bar(ind+0.2,k1,width,color="green", label='JACCARD - Grafo SEM ego')														## Invertido pra ficar mais facil a visualização no grafo
	p6=plt.bar(ind+0.3,z1,width,color="seagreen", label='JACCARD - Grafo COM ego - Comunidade SEM singletons')					## Invertido pra ficar mais facil a visualização no grafo (lembrar de mudar o +0.1)
	p8=plt.bar(ind+0.4,w1,width,color="lightgreen", label='JACCARD - Grafo SEM ego - Comunidade SEM singletons')

	plt.ylabel(alg)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()	

	if not os.path.exists(output):
		os.makedirs(output)

#	plt.savefig(output+"full_metrics_"+str(alg)+".png")
	plt.close()
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="NMI - Grafo COM ego", marker=dict(color='darkblue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="NMI - Grafo COM ego - Comunidade SEM singletons", marker=dict(color='royalblue'))
	trace3 = go.Bar(x = dataset[1][1], y = dataset[3][0], error_y=dict(type='data',array=dataset[3][2], color='#E6842A', visible=True), name="NMI - Grafo SEM ego", marker=dict(color='blue'))
	trace4 = go.Bar(x = dataset[1][1], y = dataset[4][0], error_y=dict(type='data',array=dataset[4][2], color='#E6842A', visible=True), name="NMI - Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightblue'))

	trace5 = go.Bar(x = dataset[1][1], y = dataset[5][0], error_y=dict(type='data',array=dataset[5][2], color='#E6842A', visible=True), name="JACCARD - Grafo COM ego", marker=dict(color='darkgreen'))
	trace6 = go.Bar(x = dataset[1][1], y = dataset[6][0], error_y=dict(type='data',array=dataset[6][2], color='#E6842A', visible=True), name="JACCARD - Grafo COM ego - Comunidade SEM singletons", marker=dict(color='seagreen'))
	trace7 = go.Bar(x = dataset[1][1], y = dataset[7][0], error_y=dict(type='data',array=dataset[7][2], color='#E6842A', visible=True), name="JACCARD - Grafo SEM ego", marker=dict(color='green'))
	trace8 = go.Bar(x = dataset[1][1], y = dataset[8][0], error_y=dict(type='data',array=dataset[8][2], color='#E6842A', visible=True), name="JACCARD - Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightgreen'))
		
	
	data = [trace1,trace3,trace2,trace4,trace5,trace7,trace6,trace8]																						## Invertido pra ficar mais facil a visualização no grafo

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+"full_metrics_"+str(alg)+".html",auto_open=False)	
		
