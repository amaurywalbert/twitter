# -*- coding: latin1 -*-
################################################################################################
#	
#
import sys, os, os.path
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Gera histogramas a partir de um dictionary {axis_X, axis_Y.
## 
######################################################################################################################################################################
def histogram(data,output_dir,elements,net):

	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	if data.__class__.__name__ == 'dict':
		_data = []
		for k,v in data.iteritems():
			_data.append(v)
		histogram_print(_data,output_dir,elements,net)
		normalized_print(_data,output_dir,elements,net)

	elif data.__class__.__name__ == 'list':
		histogram_print(data,output_dir,elements,net)
		normalized_print(data,ouput_dir,elements,net)

	else:
		print ("\nTipo de dados não reconhecido para gerar histograma\n")
######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def normalized_print(data,output_dir,elements,net):
	print ("\nCriando histograma dinâmico...")
	print ("Salvando dados em: "+str(output_dir)+"\n")

	trace = go.Histogram(x=data, name="vértices = "+str(elements), marker=dict(color='green'))
	_data = [trace]
	layout = go.Layout(title='Distribuição de Graus', xaxis=dict(title='Graus'),yaxis=dict(title='Vértices'))    
	fig = go.Figure(data=_data, layout=layout)

	plotly.offline.plot(fig, filename=output_dir+str(net)+"_dist_degree.html")

	print (str(net)+" - OK! Histograma salvo em: "+str(output_dir))
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram_print(data,output_dir,elements,net):
	print ("\nCriando histograma...")
	print ("Salvando dados em: "+str(output_dir)+"\n")
	plt.hist(data,label="vértices = "+str(elements),color='green')
	plt.xlabel ("Graus")
	plt.ylabel ("Vértices")
	plt.title ("Distribuição de graus")
	plt.legend(loc='best')
	plt.savefig(output_dir+str(net)+"_dist_degree.png")
	plt.close()

	print (str(net)+" - OK! Histograma salvo em: "+str(output_dir))
	print
