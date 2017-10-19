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
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Gera histogramas a partir de um dictionary {axis_X, axis_Y.
## 
######################################################################################################################################################################
def histogram(data,output_dir,title,xaxis,yaxis):
	if data:
		if data.__class__.__name__ == 'dict':
			_data = []
			for k,v in data.iteritems():
				_data.append(v)
			histogram_print(_data,output_dir,title,xaxis,yaxis)
			normalized_print(_data,ouput_dir,title,xaxis,yaxis)
		elif data.__class__.__name__ == 'list':
			histogram_print(data,output_dir,title,xaxis,yaxis)
			normalized_print(data,output_dir,title,xaxis,yaxis)
		else:
			print ("\nTipo de dados não reconhecido para gerar histograma\n")
	else:
		print ("\nVocê deve passar o argumento 'data'...\n")
		return 
######################################################################################################################################################################
# HTML
######################################################################################################################################################################
def normalized_print(data,output_dir,title,xaxis,yaxis):
	print ("\nCriando histograma dinâmico...")
	print ("Salvando dados em: "+str(output_dir)+"\n")
	normalized = [go.Histogram(x=data,marker=dict(color='green'))]
	plotly.offline.plot(normalized, filename=output_dir+title+".html",auto_open=False)
	print ("OK")
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def histogram_print(data,output_dir,title,xaxis,yaxis):
	print ("\nCriando histograma...")
	print ("Salvando dados em: "+str(output_dir)+"\n")
#	plt.hist(data,label=title,color='green')
	plt.hist(data,50,color='green')
	plt.xlabel (xaxis)
	plt.ylabel (yaxis)
	plt.title (title)
	plt.legend(loc='best')
	plt.savefig(output_dir+title+".png")
	plt.close()

	print ("OK!")
	print
