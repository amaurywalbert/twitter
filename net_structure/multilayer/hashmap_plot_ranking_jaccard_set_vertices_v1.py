# -*- coding: latin1 -*-
################################################################################################
#	
#
import sys, time, json, os, os.path
import numpy as np
from math import*
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib as mpl
import pylab
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import pandas_datareader
from pandas_datareader import data, wb
from pandas import Series, DataFrame
pd.__version__


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Plotar os dados de acordo com as métricas e propriedades calculadas nas redes Multilayer
##					Este ranking foi gerado pelo professor Thierson de acordo com o jaccard dos vértices par-a-par entre as camadas
##
## ID_ego a:amigos s:seguidores r:retuítes l:likes m:menções
##
## ID_ego as:data sr:data rl:data lm:data ma:data - TXT
## {ID_ego:{ as:data sr:data rl:data lm:data ma:data} - JSON
######################################################################################################################################################################


######################################################################################################################################################################
#
# Cria diretórios
#
######################################################################################################################################################################
def create_dirs(x):
	if not os.path.exists(x):
		os.makedirs(x)	

######################################################################################################################################################################
#
# Plotar o gráfico 
#
######################################################################################################################################################################

def make_plot(metric,df,output):
	f, ax = plt.subplots(1, figsize=(10,5))																# Create a figure with a single subplot
	bar_width = 1																									# Set bar width at 1
	bar_l = [i for i in range(len(df['rl']))]																# positions of the left bar-boundaries 
	tick_pos = [i+(bar_width/2) for i in bar_l]															# positions of the x-axis ticks (center of the bars as bar labels) 
	totals = [i+j+k+l+m+n+o+p+q+r for i,j,k,l,m,n,o,p,q,r in zip(df['rl'], df['as'], df['am'], df['al'], df['rm'], df['ar'], df['lm'], df['ls'], df['ms'], df['rs'])]	# Create the total score for each participant

	rl_rel = [i / j * 100 for  i,j in zip(df['rl'], totals)]								# Create the percentage of the total score the value for each participant was
	as_rel = [i / j * 100 for  i,j in zip(df['as'], totals)]								# Create the percentage of the total score the value for each participant was	
	am_rel = [i / j * 100 for  i,j in zip(df['am'], totals)]								# Create the percentage of the total score the value for each participant was
	al_rel = [i / j * 100 for  i,j in zip(df['al'], totals)]								# Create the percentage of the total score the value for each participant was
	rm_rel = [i / j * 100 for  i,j in zip(df['rm'], totals)]								# Create the percentage of the total score the value for each participant was
	ar_rel = [i / j * 100 for  i,j in zip(df['ar'], totals)]								# Create the percentage of the total score the value for each participant was
	lm_rel = [i / j * 100 for  i,j in zip(df['lm'], totals)]								# Create the percentage of the total score the value for each participant was
	ls_rel = [i / j * 100 for  i,j in zip(df['ls'], totals)]								# Create the percentage of the total score the value for each participant was
	ms_rel = [i / j * 100 for  i,j in zip(df['ms'], totals)]								# Create the percentage of the total score the value for each participant was
	rs_rel = [i / j * 100 for  i,j in zip(df['rs'], totals)]								# Create the percentage of the total score the value for each participant was
	
	# Create a bar charts
	ax.bar(bar_l, rl_rel, label='rl', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, as_rel, bottom=rl_rel, label='as', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, am_rel, bottom=[i+j for i,j in zip(rl_rel, as_rel)], label='am', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, al_rel, bottom=[i+j+k for i,j,k in zip(rl_rel, as_rel,am_rel)], label='al', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, rm_rel, bottom=[i+j+k+l for i,j,k,l in zip(rl_rel, as_rel, am_rel, al_rel)], label='rm', alpha=0.9, width=bar_width, edgecolor='white')
	
	ax.bar(bar_l, ar_rel, bottom=[i+j+k+l+m for i,j,k,l,m in zip(rl_rel, as_rel, am_rel, al_rel,rm_rel)], label='ar', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, lm_rel, bottom=[i+j+k+l+m+n for i,j,k,l,m,n in zip(rl_rel, as_rel, am_rel, al_rel,rm_rel,ar_rel)], label='lm', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, ls_rel, bottom=[i+j+k+l+m+n+o for i,j,k,l,m,n,o in zip(rl_rel, as_rel, am_rel, al_rel,rm_rel,ar_rel,lm_rel)], label='ls', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, ms_rel, bottom=[i+j+k+l+m+n+o+p for i,j,k,l,m,n,o,p in zip(rl_rel, as_rel, am_rel, al_rel,rm_rel,ar_rel,lm_rel,ls_rel)], label='ms', alpha=0.9, width=bar_width, edgecolor='white')
	ax.bar(bar_l, rs_rel, bottom=[i+j+k+l+m+n+o+p+q for i,j,k,l,m,n,o,p,q in zip(rl_rel, as_rel, am_rel, al_rel,rm_rel,ar_rel,lm_rel,ls_rel,ms_rel)], label='rs', alpha=0.9, width=bar_width, edgecolor='white')

	# Set the ticks to be ranking
	plt.xticks(tick_pos, df['Ranking'])
	ax.set_ylabel("Percentage")
	ax.set_xlabel("Ranking")

	# Let the borders of the graphic
	plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
	plt.ylim(-10, 110)

	# Now add the legend with some customizations.
	legend = ax.legend(shadow=True)

	# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
	frame = legend.get_frame()
	frame.set_facecolor('0.90')

	# Set the fontsize
	for label in legend.get_texts():
		label.set_fontsize('large')

	for label in legend.get_lines():
		label.set_linewidth(1.5)  # the legend line width

	# rotate axis labels
#	plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
	
	plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
	plt.title('Ranking of Jaccard over Vertices')
	
	plt.savefig(output+"Ranking_of_Jaccard_Vertices.png")

	# shot plot
	plt.show()
	
	plt.close()
	print (" - OK! Color Bar salvo em: "+str(output))
	print
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" Plotar gráficos sobre as métricas e propriedades calculadas - Multilayer			"
	print"																											"
	print"#################################################################################"

	metric = "ranking_jaccard_set_vertices"
	raw_data = {'Ranking': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'rl': [34.47,29.06,14.83,8.62,4.81,4.21,2.40,1.00,0.40,0.20],
        'as': [30.06,13.43,5.21,8.02,7.01,7.62,18.44,7.21,1.60,1.40],
        'am': [15.43,14.23,8.62,10.82,13.03,9.62,10.22,5.81,10.42,1.80],
        'al': [11.22,18.64,25.05,13.63,16.63,5.61,4.61,1.60,2.81,0.20],
        'rm': [3.41,10.22,15.43,16.23,17.64,14.83,10.62,7.01,3.41,1.20],
        'ar': [3.21,5.81,14.83,23.45,15.23,16.43,11.62,3.61,5.81,0.00],
        'lm': [2.20,8.02,13.23,12.83,14.83,22.85,13.63,8.62,2.81,1.00],
        'ls': [0.00,0.20,1.40,3.01,7.62,10.22,18.64,36.27,13.63,9.02],
        'ms': [0.00,0.20,1.40,2.61,2.40,4.61,6.61,12.42,25.45,44.29],
        'rs': [0.00,0.20,0.00,0.80,0.80,4.01,3.21,16.43,33.67,40.88]
        }
	df = pd.DataFrame(raw_data, columns = ['Ranking','rl','as','am','al','rm','ar','lm','ls','ms','rs'])
	print df
	
	output =str(output_dir)+str(metric)+"/"
	create_dirs(output)
	make_plot(metric,df,output)

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")


output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/"	# Diretório para Salvar os gráficos...
#Executa o método main
if __name__ == "__main__": main()