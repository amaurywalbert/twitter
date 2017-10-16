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
import calc

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Gerar Resultados
##								
## # INPUT: Arquivos com os resultado obtidos em cada métricas 
## # OUTPUT:
##		- Arquivos com estatísticas dos resultados
######################################################################################################################################################################


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
	
	print data 
	
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

	output = output+alg+"/"
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

	output = output+alg+"/"
	if not os.path.exists(output):
		os.makedirs(output)
		
	plotly.offline.plot(fig, filename=output+str(metric)+".html")


######################################################################################################################################################################
#
# Salva os dados de cada algoritmo em formato JSON
#
######################################################################################################################################################################
def save_data(output,data,data_overview):
	if not os.path.exists(output):
		os.makedirs(output)
	print ("\n##################################################\n")
	print ("Salvando dados em: "+str(output))
	
	with open(output+"statistics.json", 'w') as f:
		for k, v in data.iteritems():
			network = k,v	 
			f.write(json.dumps(network)+"\n")	
	with open(output+"statistics_overview.json", 'w') as g:
		for k, v in data_overview.iteritems():	 
			network = k,v	 
			g.write(json.dumps(network)+"\n")
				
	print ("##################################################\n")
	
######################################################################################################################################################################
#
# Prepara apresentação dos resultados para o algoritmo - METRICA
#
######################################################################################################################################################################
def algorithm(comm_data_dir,metric):
	data = {}																				# Armazenar todos os valores da Metrica para cada threshold do algoritmo em cada rede - Formato {'n8': {1: {'soma': 6.059981138000007, 'media': 0.025787153778723433, 'desvio_padrao': 0.006377214443559922, 'variancia': 4.0668864059149294e-05}, 2: {'soma': 6.059981138000007...}}	
	data_overview = {}																	# Armazenar o nome da rede e o maior valor do trheshold do algoritmo para a MetricaI - Formato {{'N1':0.012},...}
	
	if os.path.isdir(comm_data_dir):
		for file in os.listdir(comm_data_dir):
			network = file.split(".json")														# pegar o nome do arquivo que indica o a rede analisada
			network = network[0]
			data_overview[network] = {'threshold':' ',metric:float(0)}
			print ("\n##################################################")
			print ("Recuperando dados da rede "+str(network))	

			if os.path.isfile(comm_data_dir+file):		
				with open(comm_data_dir+file, 'r') as f:
					partial = {}

					for line in f:
						comm_data = json.loads(line) 
						for k, v in comm_data.iteritems():
							values = []
							for item in v:
								if not math.isnan(item):											# exclui calculo de da METRICA que retorna valor NaN
									values.append(item)				

							result = calc.calcular_full(values)												# Calcula média e outros dados da METRICA recuperados para o conjunto de egos usando o threshold k				 				
							if result is not None:						
								if	float(result['media']) > data_overview[network][metric]:
									data_overview[network] = {'threshold':k,metric:float(result['media'])}
								partial[k] = result														# Adiciona os caclulos feitos num dicionário com indice k (ou seja, o threshold usado pelo algoritmo)
								data[network] = partial				
			else:
				print ("Arquivo não encontrado: "+str(comm_data_dir+file))
		
			print data_overview[network]														# Maior média para a rede [network]
	else:
		print ("Diretório não encontrado: "+str(comm_data_dir))					
	print
#	print
#	print data_overview
	print ("##################################################\n")
	return data,data_overview
	print ("##################################################")	

######################################################################################################################################################################
#
# Realiza as configurações necessárias para os dados do METRICA
#
######################################################################################################################################################################
def instructions(metric,alg):
################################################################################################	
	
	comm_data_dir = str(source)+"graphs_with_ego/"+alg+"/"+str(metric)+"/full/"
	output_dir = str(output)+"graphs_with_ego/"+alg+"/"+str(metric)+"/full/"
		
	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
	plot_single(output,data_overview,metric,alg,title='Graphs with ego - Communities with singletons')	
	data1 = data_overview
################################################################################################

	comm_data_dir = str(source)+"graphs_with_ego/"+alg+"/"+str(metric)+"/without_singletons/"
	output_dir = str(output)+"graphs_with_ego/"+alg+"/"+str(metric)+"/without_singletons/"

	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
	plot_single(output,data_overview,metric,alg,title='Graphs with ego - Communities without singletons')	
	data2 = data_overview
################################################################################################

	comm_data_dir = str(source)+"graphs_without_ego/"+alg+"/"+str(metric)+"/full/"
	output_dir = str(output)+"graphs_without_ego/"+alg+"/"+str(metric)+"/full/"

	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
	plot_single(output,data_overview,metric,alg,title='Graphs without ego - Communities with singletons')
	data3 = data_overview
################################################################################################

	comm_data_dir = str(source)+"graphs_without_ego/"+alg+"/"+str(metric)+"/without_singletons/"
	output_dir = str(output)+"graphs_without_ego/"+alg+"/"+str(metric)+"/without_singletons/"

	data,data_overview = algorithm(comm_data_dir,metric)
	save_data(output_dir,data,data_overview)		
	plot_single(output,data_overview,metric,alg,title='Graphs without ego - Communities without singletons')	
	data4 = data_overview

################################################################################################
	plot_full(output,data1,data2,data3,data4,metric,alg)		
		
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "\n#######################################################################\n"	
	print ("Métrica a ser aplicada na geração dos resultados:\n")
	print("01 - NMI - Normalized Mutual Infomation. ")
	print("02 - Ômega Index.")
	print("03 - Jaccard Similarity.")
	print	
	metric_op = int(raw_input("Escolha uma opção acima: "))
	print ("\n##################################################\n")
#######################################################################
	if metric_op == 01:
		metric = "nmi"
#######################################################################		
	elif metric_op == 02:
		metric = "omega"
#######################################################################
	elif metric_op == 03:
		metric = "jaccard"
#######################################################################
	else:
		metric = ""
		print("Opção inválida! Saindo...")
		exit()	
#######################################################################

	print "\n#######################################################################\n"	
	print ("Algoritmo usado na detecção das comunidades:\n")
	print("01 - COPRA ")
	print("02 - OSLOM")
	print	
	alg_op = int(raw_input("Escolha uma opção acima: "))
	print ("\n##################################################\n")
#######################################################################
	if alg_op == 01:
		alg = "copra"
#######################################################################		
	elif alg_op == 02:
		alg = "oslom"
#######################################################################
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		exit()	
#######################################################################

	instructions(metric,alg)
	
#######################################################################
	print
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
#####Alterar as linhas para Dropbox quando executado em ambiente de produção
source = "/home/amaury/Dropbox/evaluation/"
output = "/home/amaury/Dropbox/statistics/"
######################################################################################################################


if __name__ == "__main__": main()