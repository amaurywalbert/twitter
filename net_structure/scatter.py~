# -*- coding: latin1 -*-
################################################################################################
#	
#
import sys, os, os.path
import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
import plotly

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Gera gráfico de dispersão a partir de dois vetores
## 
######################################################################################################################################################################
def prepare(data_nodes,data_edges,output,net):

	if not os.path.exists(output):
		os.makedirs(output)
	
	if net == 'n1':
		network = 'Follow'
	elif net == 'n9':
		network = 'Followers'			
			
	elif net == 'n2':
		network = 'Retweets'			

	elif net == 'n3':
		network = 'Likes'
			
	elif net == 'n4':
		network = 'Mentions'
						
	elif net == 'n5':
		network = 'Co-Follow'

	elif net == 'n6':
		network = 'Co-Retweets'

	elif net == 'n7':
		network = 'Co-Likes'

	elif net == 'n8':
		network = 'Co-Mentions'

	elif net == 'n10':
		network = 'Co-Followers'

	else:
		print ("Valor incorreto para nome da rede-ego")
		exit()						

	scatter_print_single(data_nodes,data_edges,output,net,network)



######################################################################################################################################################################
# Scatter Plot Single
######################################################################################################################################################################
def scatter_print_single(data_nodes,data_edges,output,net,network):
	title = str(network)
	print ("\nCriando gráfico de dispersão...")
	print ("Salvando dados em: "+str(output)+"\n")
	
	trace = go.Scatter(x = data_nodes,y = data_edges, mode = 'markers')
	data = [trace]
	layout= go.Layout(title = title,hovermode= 'closest',xaxis= dict(title= 'Vértices',ticklen= 5,zeroline= False,gridwidth=2,),yaxis=dict(title= 'Arestas',ticklen= 5,gridwidth= 2,),showlegend= False)
	fig = dict(data=data, layout=layout)	
	
	plotly.offline.plot(fig, filename=str(output)+str(net)+"_scatter_nodes_edges.html",auto_open=False)

	print (str(net)+" - OK! Gráfico salvo em: "+str(output))
	print

