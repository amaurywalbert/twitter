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
def plot_full(output,data1,data2,data3,data4,metric,alg):
	title = "Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg)
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
def plot_without_singletons(output,data1,data2,metric,alg):
	title = "Avaliação das redes usando a métrica "+str(metric)+" e algoritmo "+str(alg)
	print ("Gerando Gráfico para o algoritmo: "+str(alg))

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
	p2=plt.bar(ind,z,width,color="green", label="Grafo SEM ego - Threshold - "+str(dataset[2][3]))

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()	


#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()
	
	
	
	




#########################################################################################################
#########################################################################################################
#######################################################################################################################################################################
## Plota Gráficos dos dados... Desconsiderando se hṕa ou não singletons
#######################################################################################################################################################################
#def plot_metrics.plot_full_without_singletons(output,data_full,metric)
#	title = "Avaliação das redes usando a métrica "+str(metric)
#	print ("Gerando Gráfico Completo...")
#	
#	
#	dataset = {}	
#	
#	for k,v in data.iteritems()
#		data1 = v['data1']
#		data2 = v['data2']
#
#		data_overview_full = [data1,data2]
#		#i = 1										#armazenar dados de plotagem para dataset COM ego
#		#i = 2										#armazenar dados de plotagem para dataset SEM ego
#	
#		i=0
#		data_alg = {}
#		for data_overview in data_overview_full:
#			i+=1
#			interaction = []
#			value = []
#			std = []
#			threshold = []
#			
#			co_interaction = []
#			co_value = []
#			co_std = []
#			co_threshold = []	
#			for k, v in data_overview.iteritems():
#				if k == 'n1':
#					key = 'follow'
#					interaction.append(key)
#					value.append(round(v[metric], 3))
#					std.append(round(v['std'], 3))
#					threshold.append(v['threshold'])						
#				elif k == 'n2':
#					key = 'retweets'			
#					interaction.append(key)
#					value.append(round(v[metric], 3))
#					std.append(round(v['std'], 3))
#					threshold.append(v['threshold'])
#				elif k == 'n3':
#					key = 'likes'
#					interaction.append(key)
#					value.append(round(v[metric], 3))
#					std.append(round(v['std'], 3))
#					threshold.append(v['threshold'])
#				elif k == 'n4':
#					key = 'mentions'
#					interaction.append(key)
#					value.append(round(v[metric], 3))
#					std.append(round(v['std'], 3))
#					threshold.append(v['threshold'])
#				elif k == 'n9':
#					key = 'followers'
#					interaction.append(key)
#					value.append(round(v[metric], 3))
#					std.append(round(v['std'], 3))
#					threshold.append(v['threshold'])
#							
#				elif k == 'n5':
#					key = 'co-follow'
#					co_interaction.append(key)
#					co_value.append(round(v[metric], 3))
#					co_std.append(round(v['std'], 3))
#					co_threshold.append(v['threshold'])
#				elif k == 'n6':
#					key = 'co-retweets'
#					co_interaction.append(key)
#					co_value.append(round(v[metric], 3))
#					co_std.append(round(v['std'], 3))
#					co_threshold.append(v['threshold'])
#				elif k == 'n7':
#					key = 'co-likes'
#					co_interaction.append(key)
#					co_value.append(round(v[metric], 3))
#					co_std.append(round(v['std'], 3))
#					co_threshold.append(v['threshold'])
#				elif k == 'n8':
#					key = 'co-mentions'
#					co_interaction.append(key)
#					co_value.append(round(v[metric], 3))
#					co_std.append(round(v['std'], 3))
#					co_threshold.append(v['threshold'])
#				elif k == 'n10':
#					key = 'co-followers'
#					co_interaction.append(key)
#					co_value.append(round(v[metric], 3))
#					co_std.append(round(v['std'], 3))
#					co_threshold.append(v['threshold'])
#			
#				else:
#					print ("Valor incorreto para nome da rede-ego")
#					exit()																																						
#
#			for item in co_value:
#				value.append(item)
#			for item in co_interaction:
#				interaction.append(item)
#			for item in co_std:
#				std.append(item)
#			for item in co_threshold:
#				threshold.append(item)
#			 	
#			data = [value,interaction,std,threshold]
#			data_alg[i] = data
#		dataset[k] = data_alg
#
#
#
#
#
#
#	x = dataset[0][1][1]								# recebe os nomes das redes ego
#	n=len(x)
#	
#				
#	y0 = np.array(dataset[0][1][0])								# recebe os valores para COM ego
#	z0 = np.array(dataset[0][2][0])								# recebe os valores para SEM ego
#	
#	y1 = np.array(dataset[1][1][0])								# recebe os valores para COM ego
#	z1 = np.array(dataset[1][2][0])								# recebe os valores para SEM ego
#
#	y2 = np.array(dataset[2][1][0])								# recebe os valores para COM ego
#	z2 = np.array(dataset[2][2][0])								# recebe os valores para SEM ego
#	
#	if len(dataset) > 3:
#	
#
#	ind=np.arange(n)
#	width=0.35
#
#	output = str(output)+"/"+str(metric)+"/"
#	
#	if not os.path.exists(output):
#		os.makedirs(output)
#################################################################################################  MANTER -- Dá pra exportar a tabela depois...
#	trace1 = go.Bar(x = dataset[0][1][1], y = dataset[0][1][0], error_y=dict(type='data',array=dataset[0][1][2], color='#E6842A', visible=True), name="Grafo COM ego - Threshold - "+str(dataset['copra'][1][3]), marker=dict(color='blue'))
#	trace2 = go.Bar(x = dataset[0][2][1], y = dataset[0][2][0], error_y=dict(type='data',array=dataset[0][2][2], color='#E6842A', visible=True), name="Grafo SEM ego - Threshold - "+str(dataset['copra'][2][3]), marker=dict(color='green'))
#
#	trace3 = go.Bar(x = dataset[1][1][1], y = dataset[1][1][0], error_y=dict(type='data',array=dataset[1][1][2], color='#E6842A', visible=True), name="Grafo COM ego - Threshold - "+str(dataset['oslom'][1][3]), marker=dict(color='blue'))
#	trace4 = go.Bar(x = dataset[1][2][1], y = dataset[1][2][0], error_y=dict(type='data',array=dataset[1][2][2], color='#E6842A', visible=True), name="Grafo SEM ego - Threshold - "+str(dataset['oslom'][2][3]), marker=dict(color='green'))
#
#	trace5 = go.Bar(x = dataset[2][1][1], y = dataset[2][1][0], error_y=dict(type='data',array=dataset[2][1][2], color='#E6842A', visible=True), name="Grafo COM ego - Threshold - "+str(dataset['rak'][1][3]), marker=dict(color='blue'))
#	trace6 = go.Bar(x = dataset[2][2][1], y = dataset[2][2][0], error_y=dict(type='data',array=dataset[2][2][2], color='#E6842A', visible=True), name="Grafo SEM ego - Threshold - "+str(dataset['rak'][2][3]), marker=dict(color='green'))
#
#	if len(dataset) > 3:
#	
#		y3 = np.array(dataset[3][1][0])								# recebe os valores para COM ego
#		z3 = np.array(dataset[3][2][0])								# recebe os valores para SEM ego	
#		trace7 = go.Bar(x = dataset[3][1][1], y = dataset[2][1][0], error_y=dict(type='data',array=dataset[3][1][2], color='#E6842A', visible=True), name="Grafo COM ego - Threshold - "+str(dataset[3][1][3]), marker=dict(color='blue'))
#		trace8 = go.Bar(x = dataset[3][2][1], y = dataset[3][2][0], error_y=dict(type='data',array=dataset[3][2][2], color='#E6842A', visible=True), name="Grafo SEM ego - Threshold - "+str(dataset[3][2][3]), marker=dict(color='green'))
#
#	
#		data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8]
#	else:
#		data = [trace1,trace2,trace3,trace4,trace5,trace6]
#
#	title_plot = title
#	layout = go.Layout(title=title_plot,xaxis=dict(tickangle=-45),barmode='group',)
#	fig = go.Figure(data=data, layout=layout)
#
#	plotly.offline.plot(fig, filename=output+str(metric)+"_"+str(alg)+".html",auto_open=False)

################################################################################################
	p1=plt.bar(ind-0.1,y,width,color="blue", label="Grafo COM ego - Threshold - "+str(dataset[1][3]))
	p2=plt.bar(ind,z,width,color="green", label="Grafo SEM ego - Threshold - "+str(dataset[2][3]))

	plt.ylabel(metric)
	plt.title(str(title))
	
	plt.xticks(ind+width/2,(x))
	plt.legend(loc='best')	
	plt.tight_layout()
	plt.show()	


#	plt.savefig(output+str(alg)+"_"+str(metric)+".png")
	plt.close()
		

