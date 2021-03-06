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


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_single(output,data_overview,metric,alg,title):
	print ("\n##################################################\n")
	print ("Gerando Gráficos Individuais...")
	interaction = []
	value = []
	co_interaction = []
	co_value = []
	threshold = []
	co_threshold = []
	for k, v in data_overview.iteritems():
		if k == 'n1':
			key = 'follow'
			interaction.append(key)
			value.append(round(v[metric], 3))
			threshold.append(v['threshold'])			
		elif k == 'n2':
			key = 'retweets'			
			interaction.append(key)
			value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
		elif k == 'n3':
			key = 'likes'
			interaction.append(key)
			value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
		elif k == 'n4':
			key = 'mentions'
			interaction.append(key)
			value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
		elif k == 'n9':
			key = 'followers'
			interaction.append(key)
			value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
												
		elif k == 'n5':
			key = 'co-follow'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
		elif k == 'n6':
			key = 'co-retweets'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
		elif k == 'n7':
			key = 'co-likes'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
		elif k == 'n8':
			key = 'co-mentions'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))
			threshold.append(v['threshold'])

		elif k == 'n10':
			key = 'co-followers'
			co_interaction.append(key)
			co_value.append(round(v[metric], 3))
			threshold.append(v['threshold'])
			
		else:
			print ("Valor incorreto para nome da rede-ego")
			exit()																																						

	for item in co_value:
		value.append(item)
	for item in co_interaction:
		interaction.append(item)
	for item in co_threshold:
		threshold.append(item)
	colors = ['lightblue', 'lightgreen', 'yellow', 'magenta', 'red', 'green', 'blue', 'cyan', 'magenta', 'black'] 	
	data = [value,colors,interaction,threshold]
	
	
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
	plt.legend(_chartBars, str(data[2])+" - "+str(data[3]))

	output = str(output)+"/"+str(metric)+"/bars_single/"
	if not os.path.exists(output):
		os.makedirs(output)
	
	plt.savefig(output+str(title)+"_"+str(alg)+"_"+str(metric)+".png")
	plt.close()

######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_full(output,data1,data2,data3,data4,metric,alg):
	title = "Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo...")

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
		threshold = []
			
		co_interaction = []
		co_value = []
		co_std = []
		co_threshold = []	
		for k, v in data_overview.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])						
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		for item in co_threshold:
			threshold.append(item)
			 	
		data = [value,interaction,std,threshold]
		dataset[i] = data

	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego e comunidades COM singletons
	z = np.array(dataset[2][0])								# recebe os valores para COM ego e comunidades SEM singletons
	k = np.array(dataset[3][0])								# recebe os valores para SEM ego e comunidades COM singletons
	w = np.array(dataset[4][0])								# recebe os valores para SEM ego e comunidades SEM singletons

	ind=np.arange(n)
	width=0.35

	output = str(output)+"/"+str(metric)+"/"
	
	if not os.path.exists(output):
		os.makedirs(output)
################################################################################################  MANTER -- Dá pra exportar a tabela depois...
	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="Grafo COM ego - "+str(dataset[1][3]), marker=dict(color='blue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="Grafo COM ego - Comunidade SEM singletons - "+str(dataset[2][3]), marker=dict(color='green'))
	trace3 = go.Bar(x = dataset[1][1], y = dataset[3][0], error_y=dict(type='data',array=dataset[3][2], color='#E6842A', visible=True), name="Grafo SEM ego - "+str(dataset[3][3]), marker=dict(color='lightblue'))
	trace4 = go.Bar(x = dataset[1][1], y = dataset[4][0], error_y=dict(type='data',array=dataset[4][2], color='#E6842A', visible=True), name="Grafo SEM ego - Comunidade SEM singletons - "+str(dataset[4][3]), marker=dict(color='lightgreen'))
	
	data = [trace1, trace3,trace2,trace4]																						## Invertido pra ficar mais facil a visualização no grafo

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(metric)+"_"+str(alg)+".html",auto_open=False)

################################################################################################
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


#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()




######################################################################################################################################################################
# Plota Gráficos dos dados... Desconsiderando se hṕa ou não singletons
######################################################################################################################################################################
def plot_full_without_singletons(output,data1,data2,metric,alg):
	title = "Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo...")

	data_overview_full = [data1,data2]
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
		threshold = []
			
		co_interaction = []
		co_value = []
		co_std = []
		co_threshold = []	
		for k, v in data_overview.iteritems():
			if k == 'n1':
				key = 'follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])						
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
				threshold.append(v['threshold'])
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v[metric], 3))
				co_std.append(round(v['std'], 3))
				co_threshold.append(v['threshold'])
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		for item in co_std:
			std.append(item)
		for item in co_threshold:
			threshold.append(item)
			 	
		data = [value,interaction,std,threshold]
		dataset[i] = data

	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego
	z = np.array(dataset[2][0])								# recebe os valores para SEM ego


	ind=np.arange(n)
	width=0.35

	output = str(output)+"/"+str(metric)+"/"
	
	if not os.path.exists(output):
		os.makedirs(output)
################################################################################################  MANTER -- Dá pra exportar a tabela depois...
	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="Grafo COM ego - Threshold - "+str(dataset[1][3]), marker=dict(color='blue'))
	trace2 = go.Bar(x = dataset[2][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="Grafo SEM ego - Threshold - "+str(dataset[2][3]), marker=dict(color='green'))

	
	data = [trace1,trace2]

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+str(metric)+"_"+str(alg)+".html",auto_open=False)

################################################################################################
	p1=plt.bar(ind-0.1,y,width,color="blue", label="Grafo COM ego - Threshold - "+str(dataset[1][3]))
	p2=plt.bar(ind,z,width,color="green", label="Grafo COM ego - Threshold - "+str(dataset[2][3]))

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()	


#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()


######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_full_algs(output,dataset1,dataset2,dataset3,dataset4,metric):
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

	if not os.path.exists(output):
		os.makedirs(output)
		
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="COPRA - Grafo COM ego", marker=dict(color='darkblue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="COPRA - Grafo COM ego - Comunidade SEM singletons", marker=dict(color='royalblue'))
	trace3 = go.Bar(x = dataset[1][1], y = dataset[3][0], error_y=dict(type='data',array=dataset[3][2], color='#E6842A', visible=True), name="COPRA - Grafo SEM ego", marker=dict(color='blue'))
	trace4 = go.Bar(x = dataset[1][1], y = dataset[4][0], error_y=dict(type='data',array=dataset[4][2], color='#E6842A', visible=True), name="COPRA - Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightblue'))

	trace5 = go.Bar(x = dataset[1][1], y = dataset[5][0], error_y=dict(type='data',array=dataset[5][2], color='#E6842A', visible=True), name="OSLOM - Grafo COM ego", marker=dict(color='darkgreen'))
	trace6 = go.Bar(x = dataset[1][1], y = dataset[6][0], error_y=dict(type='data',array=dataset[6][2], color='#E6842A', visible=True), name="OSLOM - Grafo COM ego - Comunidade SEM singletons", marker=dict(color='seagreen'))
	trace7 = go.Bar(x = dataset[1][1], y = dataset[7][0], error_y=dict(type='data',array=dataset[7][2], color='#E6842A', visible=True), name="OSLOM - Grafo SEM ego", marker=dict(color='green'))
	trace8 = go.Bar(x = dataset[1][1], y = dataset[8][0], error_y=dict(type='data',array=dataset[8][2], color='#E6842A', visible=True), name="OSLOM - Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightgreen'))
	
	
	data = [trace1,trace3,trace2,trace4,trace5,trace7,trace6,trace8]																						## Invertido pra ficar mais facil a visualização no grafo

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=output+"full_algs_"+str(metric)+".html",auto_open=False)

################################################################################################
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

#	plt.savefig(output+"full_algs_"+str(metric)+".png")
	plt.close()
	
	
	
	
	
	
	
	
	
######################################################################################################################################################################
# Plota Gráficos dos dados... Apenas com dados das redes with ego - with singletons
######################################################################################################################################################################
def plot_full_only_with_ego(output,data,metric,alg):
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo..."+str(metric))

	data_overview = data
	dataset = {}
	
	interaction = []
	value = []
	std = []
	threshold = []
			
	co_interaction = []
	co_value = []
	co_std = []
	co_threshold = []	
	for k, v in data_overview.iteritems():
		if k == 'n1':
			key = 'Follow'
			interaction.append(key)
			value.append(round(v[metric], 3))
			std.append(round(v['std'], 3))
			threshold.append(v['threshold'])						
		elif k == 'n2':
			key = 'Retweets'			
			interaction.append(key)
			value.append(round(v[metric], 3))
			std.append(round(v['std'], 3))
			threshold.append(v['threshold'])
		elif k == 'n3':
			key = 'Likes'
			interaction.append(key)
			value.append(round(v[metric], 3))
			std.append(round(v['std'], 3))
			threshold.append(v['threshold'])
		elif k == 'n4':
			key = 'Mentions'
			interaction.append(key)
			value.append(round(v[metric], 3))
			std.append(round(v['std'], 3))
			threshold.append(v['threshold'])
#		elif k == 'n9':
#			key = 'Followers'
#			interaction.append(key)
#			value.append(round(v[metric], 3))
#			std.append(round(v['std'], 3))
#			threshold.append(v['threshold'])
#					
#		elif k == 'n5':
#			key = 'Co-Follow'
#			co_interaction.append(key)
#			co_value.append(round(v[metric], 3))
#			co_std.append(round(v['std'], 3))
#			co_threshold.append(v['threshold'])
#		elif k == 'n6':
#			key = 'Co-Retweets'
#			co_interaction.append(key)
#			co_value.append(round(v[metric], 3))
#			co_std.append(round(v['std'], 3))
#			co_threshold.append(v['threshold'])
#		elif k == 'n7':
#			key = 'Co-Likes'
#			co_interaction.append(key)
#			co_value.append(round(v[metric], 3))
#			co_std.append(round(v['std'], 3))
#			co_threshold.append(v['threshold'])
#		elif k == 'n8':
#			key = 'Co-Mentions'
#			co_interaction.append(key)
#			co_value.append(round(v[metric], 3))
#			co_std.append(round(v['std'], 3))
#			co_threshold.append(v['threshold'])
#		elif k == 'n10':
#			key = 'Co-Followers'
#			co_interaction.append(key)
#			co_value.append(round(v[metric], 3))
#			co_std.append(round(v['std'], 3))
#			co_threshold.append(v['threshold'])
			
		else:
			print ("Valor incorreto para nome da rede-ego")
#			exit()																																						

	for item in co_value:
		value.append(item)
	for item in co_interaction:
		interaction.append(item)
	for item in co_std:
		std.append(item)
	for item in co_threshold:
		threshold.append(item)
		 	
	dataset = [value,interaction,std,threshold]

	x = dataset[1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[0])								# recebe os valores para COM ego


	ind=np.arange(n)
	width=0.5

	output = str(output)+"/"+str(metric)+"/"
	
	if not os.path.exists(output):
		os.makedirs(output)
################################################################################################
	_filename = output+str(metric)+"_"+str(alg)
	
	if metric == "modularity_density":
		metric = "Modularity Density"
	elif metric == "modularity":
		metric = "Modularity"
	elif metric == "intra_edges":
		metric = "Intra Edges"
	elif metric == "intra_density":
		metric = "Intra Density"
	elif metric == "contraction":
		metric = "Contraction"
	elif metric == "inter_edges":
		metric = "Inter Edges"
	elif metric == "expansion":
		metric = "Expansion"
	elif metric == "conductance":
		metric = "Conductance"
																
	title = "Communities Evaluation - "+str(metric)

################################################################################################  MANTER -- Dá pra exportar a tabela depois...
	trace1 = go.Bar(x = dataset[1], y = dataset[0], error_y=dict(type='data',array=dataset[2], color='#E6842A', visible=True), name="Threshold - "+str(dataset[3]), marker=dict(color='blue'))
	data = [trace1]

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=_filename+".html",auto_open=False)

################################################################################################
	p1=plt.bar(ind,y,width,color="blue", label="Threshold - "+str(dataset[3]))

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()

#	plt.savefig(_filename+".png")
	plt.close()



######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_full_algs_only_with_ego(output,algorithms_data,metric):

	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo...")

	dataset = {}
	#i = 1										#COPRA
	#i = 2										#OSLOM
	#i = 3										#RAK
	#i = 4										#INFOMAP
	#i = 5										#INFOMAP - Without Weight
	
	i=0

	for algorithm in algorithms_data:
		i+=1
		interaction = []
		value = []
		std = []
		
		co_interaction = []
		co_value = []
		co_std = []	
		for k, v in algorithm.iteritems():
			if k == 'n1':
				key = 'Follow'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'Retweets'			
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'Likes'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'Mentions'
				interaction.append(key)
				value.append(round(v[metric], 3))
				std.append(round(v['std'], 3))
#			elif k == 'n9':
#				key = 'Followers'
#				interaction.append(key)
#				value.append(round(v[metric], 3))
#				std.append(round(v['std'], 3))
#						
#			elif k == 'n5':
#				key = 'Co-Follow'
#				co_interaction.append(key)
#				co_value.append(round(v[metric], 3))
#				co_std.append(round(v['std'], 3))
#			elif k == 'n6':
#				key = 'Co-Retweets'
#				co_interaction.append(key)
#				co_value.append(round(v[metric], 3))
#				co_std.append(round(v['std'], 3))
#			elif k == 'n7':
#				key = 'Co-Likes'
#				co_interaction.append(key)
#				co_value.append(round(v[metric], 3))
#				co_std.append(round(v['std'], 3))
#			elif k == 'n8':
#				key = 'Co-Mentions'
#				co_interaction.append(key)
#				co_value.append(round(v[metric], 3))
#				co_std.append(round(v['std'], 3))
#			elif k == 'n10':
#				key = 'Co-Followers'
#				co_interaction.append(key)
#				co_value.append(round(v[metric], 3))
#				co_std.append(round(v['std'], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
#				exit()																																						

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
	
	y = np.array(dataset[1][0])								# COPRA
	z = np.array(dataset[2][0])								# OSLOM
	k = np.array(dataset[3][0])								# RAK
	w = np.array(dataset[4][0])								# INFOMAP
	q = np.array(dataset[5][0])								# INFOMAP - Without Weight


	ind=np.arange(n)
	width=0.25			 # Largura da barra

	if not os.path.exists(output):
		os.makedirs(output)
		
################################################################################################
	_filename = output+"full_algs_"+str(metric)
	
	if metric == "coef_clust":
		metric = "Clustering Coefficient"
		
	title = "Communities Evaluation - "+str(metric)

################################################################################################  MANTER -- Dá pra exportar a tabela depois...	
	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="COPRA - Overlapping", marker=dict(color='darkblue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="OSLOM - Overlapping", marker=dict(color='royalblue'))
	trace3 = go.Bar(x = dataset[1][1], y = dataset[3][0], error_y=dict(type='data',array=dataset[3][2], color='#E6842A', visible=True), name="RAK - Partition", marker=dict(color='blue'))
	trace4 = go.Bar(x = dataset[1][1], y = dataset[4][0], error_y=dict(type='data',array=dataset[4][2], color='#E6842A', visible=True), name="INFOMAP - Partition", marker=dict(color='lightblue'))
	trace5 = go.Bar(x = dataset[1][1], y = dataset[5][0], error_y=dict(type='data',array=dataset[5][2], color='#E6842A', visible=True), name="INFOMAP - Partition - Without Weight", marker=dict(color='yellow'))	

	data = [trace1,trace2,trace3,trace4,trace5]

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
#	layout = go.Layout(xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename=_filename+".html",auto_open=False)

################################################################################################
	
	p1=plt.bar(ind-0.2,y,width,color="darkblue", label='COPRA - Overlapping')
	p2=plt.bar(ind,z,width,color="blue", label='OSLOM - Overlapping')
	p3=plt.bar(ind+0.2,k,width,color="royalblue", label='COPRA - Partition')
	p4=plt.bar(ind+0.4,w,width,color="lightblue", label='INFOMAP - Partition')
	p5=plt.bar(ind+0.6,q,width,color="yellow", label='INFOMAP - Partition - Without Weight')
	

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
#	plt.show()	
#	plt.savefig(_filename+".png")
	plt.close()			
