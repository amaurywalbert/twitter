# -*- coding: latin1 -*-
################################################################################################
#	
#
import calc
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
# Color Bar - Correlation Matrix
######################################################################################################################################################################
def color_bar(_rs,_lm,_am,_al,_as,_ar,_ls,_ms,_rl,_rm,_aa,_ss,_rr,_ll,_mm,output):
	print ("\nCriando Matriz de Correlação...")
	print ("Salvando dados em: "+str(output)+"\n")

	_sr=_rs
	_ml=_lm
	_ma=_am
	_la=_al
	_sa=_as
	_ra=_ar
	_sl=_ls
	_sm=_ms
	_lr=_rl
	_mr=_rm

	raw_data = {'following': [_aa,_as,_ar,_al,_am],
        'followers': [_sa,_ss,_sr,_sl,_sm],
        'retweets': [_ra,_rs,_rr,_rl,_rm],
        'likes': [_la,_ls,_lr,_ll,_lm],
        'mentions': [_ma,_ms,_mr,_ml,_mm]
        }

	df = pd.DataFrame(raw_data, columns = ['following','followers','retweets','likes','mentions'])
	print df
	
#	plt.matshow(df)
#	plt.matshow(df,cmap='gray')
#	plt.matshow(df,cmap=plt.cm.get_cmap('Blues', 20))
	plt.matshow(df,cmap=plt.cm.get_cmap('gray_r', 40))
	plt.xticks(range(len(df.columns)), df.columns)
	plt.yticks(range(len(df.columns)), df.columns)

	plt.title('Jaccard over Vertices')
	plt.colorbar()
	for (i, j), z in np.ndenumerate(df):													#Show values in the grid
		plt.text(j, i, '{:0.2f}'.format(z), ha='center', va='center',bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))	

	plt.savefig(output+"Jaccard_over_Vertices.png")
	plt.show()

	plt.close()
	print (" - OK! Color Bar salvo em: "+str(output))
	print

######################################################################################################################################################################
# Histograma - HTML
######################################################################################################################################################################
def plotly_hist(data,output,name,pairs):
	print ("\nCriando histograma dinâmico...")
	print ("Salvando dados em: "+str(output)+"\n")

	trace = go.Histogram(x=data, name="vertices", marker=dict(color='green'))
	_data = [trace]
	layout = go.Layout(title="Jaccard over Vertices - "+str(pairs), xaxis=dict(title='Jaccard Coefficient'),yaxis=dict(title="Egos"))    
	fig = go.Figure(data=_data, layout=layout)

	plotly.offline.plot(fig, filename=output+pairs+".html",auto_open=False)

	print (" - OK! Histograma salvo em: "+str(output))
	print
	
######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def plot_hist(data,output,name,pairs):
	print ("\nCriando histograma...")
	print ("Salvando dados em: "+str(output)+"\n")
	plt.hist(data,color='green')
	plt.xlabel ("Jaccard Coefficient")
	plt.ylabel ("Egos")
	plt.title ("Jaccard over Vertices - "+str(pairs))
	plt.legend(loc='best')
	plt.savefig(output+pairs+".png")
	plt.close()

	print (" - OK! Histograma salvo em: "+str(output))
	print


######################################################################################################################################################################
# Histograma
######################################################################################################################################################################
def plot_hist_stacked(data,output,name,pairs):
	nBins = 10
	print ("\nCriando histograma...")
	print ("Salvando dados em: "+str(output)+"\n")
	plt.hist(data, nBins, normed=1, histtype='bar', stacked=True)
	plt.xlabel ("Jaccard Coefficient")
	plt.ylabel ("Egos")
	plt.title ("Jaccard over Vertices - "+str(pairs))
	plt.legend(loc='best')
	plt.show()
	plt.savefig(output+pairs+".png")
	plt.close()

	print (" - OK! Histograma salvo em: "+str(output))
	print

######################################################################################################################################################################
#
# Plotar Gŕaficos relacionados aos dados
#
######################################################################################################################################################################
def prepare(metric,file,output):
	with open(file,'r') as f:	
		data = json.load(f)
	pairs = {}
	_rs = []
	_lm = [] 
	_am = [] 
	_al = []
	_as = [] 
	_ar = [] 
	_ls = [] 
	_ms = [] 
	_rl = [] 
	_rm = [] 

	for k,v in data.iteritems():
		for key,value in v.iteritems():
			if key == "rs":
				_rs.append(value)
			elif key == "lm":	
				_lm.append(value)
			elif key == "am":
				_am.append(value)
			elif key == "al":
				_al.append(value)
			elif key == "as":
				_as.append(value)
			elif key == "ar":
				_ar.append(value)
			elif key == "ls":
				_ls.append(value)
			elif key == "ms":
				_ms.append(value)
			elif key == "rl":
				_rl.append(value)
			elif key == "rm":
				_rm.append(value)
	plot_hist(_rs,output,metric,"Retweets and Followers")
	plot_hist(_lm,output,metric,"Likes and Mentions")
	plot_hist(_am,output,metric,"Following and Mentions")
	plot_hist(_al,output,metric,"Following and Likes")
	plot_hist(_as,output,metric,"Following and Followers")
	plot_hist(_ar,output,metric,"Following and Retweets")
	plot_hist(_ls,output,metric,"Likes and Followers")
	plot_hist(_ms,output,metric,"Mentions and Followers")
	plot_hist(_rl,output,metric,"Retweets and Likes")
	plot_hist(_rm,output,metric,"Retweets and Mentions")
		
	_rs_avg = calc.calcular_full(_rs)
	_rs_avg = _rs_avg['media'] 

	_lm_avg = calc.calcular_full(_lm)
	_lm_avg = _lm_avg['media']
		
	_am_avg = calc.calcular_full(_am)
	_am_avg = _am_avg['media']

	_al_avg = calc.calcular_full(_al)
	_al_avg = _al_avg['media']
		
	_as_avg = calc.calcular_full(_as)
	_as_avg = _as_avg['media']
		
	_ar_avg = calc.calcular_full(_ar)
	_ar_avg = _ar_avg['media']
		
	_ls_avg = calc.calcular_full(_ls)
	_ls_avg = _ls_avg['media']
		
	_ms_avg = calc.calcular_full(_ms)
	_ms_avg = _ms_avg['media']

	_rl_avg = calc.calcular_full(_rl)
	_rl_avg = _rl_avg['media']
		
	_rm_avg = calc.calcular_full(_rm)
	_rm_avg = _rm_avg['media']
		
	_aa_avg = 1.0
	_ss_avg = 1.0
	_rr_avg = 1.0
	_ll_avg = 1.0
	_mm_avg = 1.0
		
	color_bar(_rs_avg,_lm_avg,_am_avg,_al_avg,_as_avg,_ar_avg,_ls_avg,_ms_avg,_rl_avg,_rm_avg,_aa_avg,_ss_avg,_rr_avg,_ll_avg,_mm_avg,output_dir)
		
					
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
	print
	metric = "jaccard_set_vertices"
	if not os.path.exists(str(data_dir)+str(metric)+".json"):													# Verifica se diretório existe
		print ("Impossível localizar arquivo: "+str(data_dir)+str(metric)+".json")
	else:
		file = str(data_dir)+str(metric)+".json"
		output =str(output_dir)+str(metric)+"/"
		create_dirs(output)
		prepare(metric,file,output)

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

data_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/json/"	# Diretório com arquivos JSON com métricas e propriedades Calculadas
output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/"	# Diretório para Salvar os gráficos...

#Executa o método main
if __name__ == "__main__": main()