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
def plot_bars_full(output,data1,data2,metric):
	title = "Avaliação das redes usando a métrica "+str(metric)
	print ("\n##################################################\n")
	print ("Gerando Gráfico Completo - Métrica: "+str(metric))

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
				value.append(round(v['media'], 3))
				std.append(round(v['std'], 3))			
			elif k == 'n2':
				key = 'retweets'			
				interaction.append(key)
				value.append(round(v['media'], 3))	
				std.append(round(v['std'], 3))
			elif k == 'n3':
				key = 'likes'
				interaction.append(key)
				value.append(round(v['media'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n4':
				key = 'mentions'
				interaction.append(key)
				value.append(round(v['media'], 3))
				std.append(round(v['std'], 3))
			elif k == 'n9':
				key = 'followers'
				interaction.append(key)
				value.append(round(v['media'], 3))
				std.append(round(v['std'], 3))
						
			elif k == 'n5':
				key = 'co-follow'
				co_interaction.append(key)
				co_value.append(round(v['media'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n6':
				key = 'co-retweets'
				co_interaction.append(key)
				co_value.append(round(v['media'], 3))	
				co_std.append(round(v['std'], 3))
			elif k == 'n7':
				key = 'co-likes'
				co_interaction.append(key)
				co_value.append(round(v['media'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n8':
				key = 'co-mentions'
				co_interaction.append(key)
				co_value.append(round(v['media'], 3))
				co_std.append(round(v['std'], 3))
			elif k == 'n10':
				key = 'co-followers'
				co_interaction.append(key)
				co_value.append(round(v['media'], 3))
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
	
	y = np.array(dataset[1][0])								# recebe os valores para COM
	z = np.array(dataset[2][0])								# recebe os valores para SEM

	print x
	print y, dataset[1][2]
	print z, dataset[2][2]
		
	ind=np.arange(n)
	width=0.35

	p1=plt.bar(ind-0.1,y,width,color="blue", label='Grafo COM ego')
	p2=plt.bar(ind,z,width,color="lightblue", label='Grafo SEM ego')
	
	plt.ylabel(metric)
	plt.title("Avaliação das redes usando a métrica "+str(metric))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()

	if not os.path.exists(output):
		os.makedirs(output)
		
	plt.show()	
#	plt.savefig(output+str(metric)+".png")
	plt.close()
################################################################################################  MANTER -- Dá pra exportar a tabela depois...

	trace1 = go.Bar(x = dataset[1][1], y = dataset[1][0], error_y=dict(type='data',array=dataset[1][2], color='#E6842A', visible=True), name="Grafo COM ego", marker=dict(color='blue'))
	trace2 = go.Bar(x = dataset[1][1], y = dataset[2][0], error_y=dict(type='data',array=dataset[2][2], color='#E6842A', visible=True), name="Grafo SEM ego", marker=dict(color='lightblue'))
	
	data = [trace1,trace2]																						## Invertido pra ficar mais facil a visualização no grafo

	title_plot = title
	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
	fig = go.Figure(data=data, layout=layout)

		
	plotly.offline.plot(fig, filename=output+str(metric)+".html",auto_open=False)
	
