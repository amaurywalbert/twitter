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
##					Versão 2 - Imprime na tela o desvio padrão entre os pares de layers
##
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

#####################################################################################################################################################################
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

	raw_data = {'Follow': [_aa,_ar['media'],_al['media'],_am['media']],
        'Retweet': [_ra['media'],_rr,_rl['media'],_rm['media']],
        'Like': [_la['media'],_lr['media'],_ll,_lm['media']],
        'Mention': [_ma['media'],_mr['media'],_ml['media'],_mm]
        }
        
	df = pd.DataFrame(raw_data, columns = ['Follow','Retweet','Like','Mention'])
	print ("Média:")	
	print df
	
	raw_data_dp = {'Follow': [_aa,_ar['desvio_padrao'],_al['desvio_padrao'],_am['desvio_padrao']],
        'Retweet': [_ra['desvio_padrao'],_rr,_rl['desvio_padrao'],_rm['desvio_padrao']],
        'Like': [_la['desvio_padrao'],_lr['desvio_padrao'],_ll,_lm['desvio_padrao']],
        'Mention': [_ma['desvio_padrao'],_mr['desvio_padrao'],_ml['desvio_padrao'],_mm]
        }
        
	df_dp = pd.DataFrame(raw_data_dp, columns = ['Follow','Retweet','Like','Mention'])
	print ("Desvio padrão:")
	print df_dp	
	
#	plt.matshow(df)
#	plt.matshow(df,cmap='gray')
	plt.matshow(df,cmap=plt.cm.get_cmap('Blues', 10))
#	plt.matshow(df,cmap=plt.cm.get_cmap('gray_r', 10))		#10 tonalidades
	
	plt.xticks(range(len(df.columns)), df.columns,rotation=30,size=9)
	plt.yticks(range(len(df.columns)), df.columns,rotation=30,size=9)

#	plt.title('Rank-Biased Overlap (Extended) - In-Degree Rank',y=-0.08)
	plt.colorbar()
	for (i, j), z in np.ndenumerate(df):													#Show values in the grid
		plt.text(j, i, '{:0.2f}'.format(z), ha='center', va='center',bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.9'),size=8)	

	name = "rbo_in_degree_rank"

	plt.savefig(output+name+".png",bbox_inches='tight',dpi=300)
	plt.close()
	print (" - OK! Color Bar salvo em: "+str(output))
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
			if key == "rs" or key == "sr":
				_rs.append(value)
			elif key == "lm" or key == "ml":	
				_lm.append(value)
			elif key == "am" or key == "ma":
				_am.append(value)
			elif key == "al" or key == "la":
				_al.append(value)
			elif key == "as" or key == "sa":
				_as.append(value)
			elif key == "ar" or key == "ra":
				_ar.append(value)
			elif key == "ls" or key == "sl":
				_ls.append(value)
			elif key == "ms" or key == "sm":
				_ms.append(value)
			elif key == "rl" or key == "lr":
				_rl.append(value)
			elif key == "rm" or key == "mr":
				_rm.append(value)
		
	_rs_avg = calc.calcular_full(_rs)
	_lm_avg = calc.calcular_full(_lm)	
	_am_avg = calc.calcular_full(_am)
	_al_avg = calc.calcular_full(_al)
	_as_avg = calc.calcular_full(_as)
	_ar_avg = calc.calcular_full(_ar)
	_ls_avg = calc.calcular_full(_ls)
	_ms_avg = calc.calcular_full(_ms)
	_rl_avg = calc.calcular_full(_rl)
	_rm_avg = calc.calcular_full(_rm)
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
	metric = "rbo_extended_in_degree_rank"
	if not os.path.exists(str(data_dir)+str(metric)+".json"):												# Verifica se diretório existe
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

data_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/"	# Diretório com arquivos JSON com métricas e propriedades Calculadas
output_dir = "/home/amaury/Dropbox/net_structure_hashmap_statistics/multilayer/graphs_with_ego/unweighted_directed/"	# Diretório para Salvar os gráficos...

#Executa o método main
if __name__ == "__main__": main()