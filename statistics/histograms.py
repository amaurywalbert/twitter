# -*- coding: latin1 -*-
################################################################################################
#	
#
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
def histogram(data=None,output_dir):
	if data:
		if data.__class__.__name__ == 'dict':
			_data = []
			for k,v in data.iteritems():
				_data.append(v)
			histogram_print(_data,output_dir)
			normalized_print(_data,ouput_dir)
		elif data.__class__.__name__ == 'list':
			histogram_print(data,output_dir)
			normalized_print(data,ouput_dir)
		else:
			print ("\nTipo de dados não reconhecido para gerar histograma\n")
	else:
		print ("\nVocê deve passar o argumento 'data'...\n")
		return 
######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def normalized_print(data,output_dir):
	print ("\nCriando histograma dinâmico...")
	print ("Salvando dados em: "+str(output)+"\n")
	normalized = [go.Histogram(x=data,marker=dict(color='green'))]
	plotly.offline.plot(normalized, filename=output_dir+"histogram_dist_degree.html")
	print ("OK")
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram_print(data,output_dir):
	print ("\nCriando histograma...")
	print ("Salvando dados em: "+str(output)+"\n")
	plt.hist(data,label="Distribuição de graus",color='green')
	plt.xlabel ("Graus")
	plt.ylabel ("Vértices")
	plt.title ("Distribuição de graus")
	plt.legend(loc='best')
	plt.savefig(output_dir+"histogram_dist_degree.png")
	plt.close()

	print ("OK!")
	print
