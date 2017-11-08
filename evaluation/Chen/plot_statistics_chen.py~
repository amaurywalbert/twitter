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
def plot_bars_single(output,data_overview,metric,alg,title):
	print ("\n##################################################\n")
	print ("Gerando Gráficos Individuais...")
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

	output = output+alg+"/bars_single/"
	if not os.path.exists(output):
		os.makedirs(output)
	
	plt.savefig(output+str(title)+"_"+str(alg)+"_"+str(metric)+".png")
	plt.close()

######################################################################################################################################################################
#
# Plota Gráficos dos dados...
#
######################################################################################################################################################################
def plot_bars_full(output,data1,data2,data3,data4,metric,alg):
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
#				co_interaction.append(key)
#				co_value.append(round(v[metric], 3))			
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
#				co_interaction.append(key)
#				co_value.append(round(v[metric], 3))
			
			else:
				print ("Valor incorreto para nome da rede-ego")
				exit()																																						

		for item in co_value:
			value.append(item)
		for item in co_interaction:
			interaction.append(item)
		 	
		data = [value,interaction]
		dataset[i] = data

	x = dataset[1][1]								# recebe os nomes das redes ego
	n=len(x)
	
	y = np.array(dataset[1][0])								# recebe os valores para COM ego e comunidades COM singletons
	z = np.array(dataset[2][0])								# recebe os valores para COM ego e comunidades SEM singletons
	k = np.array(dataset[3][0])								# recebe os valores para SEM ego e comunidades COM singletons
	w = np.array(dataset[4][0])								# recebe os valores para SEM ego e comunidades SEM singletons

	print y
	print z
	print k
	print w
		
	ind=np.arange(n)
	width=0.35

	p1=plt.bar(ind-0.1,y,width,color="blue", label='Grafo COM ego')
	p3=plt.bar(ind,k,width,color="lightblue", label='Grafo SEM ego')														## Invertido pra ficar mais facil a visualização no grafo
	p2=plt.bar(ind+0.1,z,width,color="green", label='Grafo COM ego - Comunidade SEM singletons')					## Invertido pra ficar mais facil a visualização no grafo (lembrar de mudar o +0.1)
	p4=plt.bar(ind+0.2,w,width,color="lightgreen", label='Grafo SEM ego - Comunidade SEM singletons')

	plt.ylabel(metric)
	plt.title("Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()

	output = output+alg+"/bars_full/"

	if not os.path.exists(output):
		os.makedirs(output)
		
	plt.show()	
#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], name="Grafo COM ego", marker=dict(color='blue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], name="Grafo COM ego - Comunidade SEM singletons", marker=dict(color='green'))
	trace3 = go.Bar(x = dataset[1][1], y = dataset[3][0], name="Grafo SEM ego", marker=dict(color='lightblue'))
	trace4 = go.Bar(x = dataset[1][1], y = dataset[4][0], name="Grafo SEM ego - Comunidade SEM singletons", marker=dict(color='lightgreen'))
	
	data = [trace1, trace3,trace2,trace4]																						## Invertido pra ficar mais facil a visualização no grafo

	layout = go.Layout(xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

		
	plotly.offline.plot(fig, filename=output+str(metric)+".html",auto_open=False)

	
