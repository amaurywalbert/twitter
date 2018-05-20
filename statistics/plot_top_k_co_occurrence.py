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
##		Status - Versão 1 - Plotar os dados da co-ocorrência dos dados entre as camadas
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
def color_bar(metric,_aa_avg,_as_avg,_ar_avg,_al_avg,_am_avg, _sa_avg,_ss_avg,_sr_avg,_sl_avg,_sm_avg, _ra_avg,_rs_avg,_rr_avg,_rl_avg,_rm_avg, _la_avg,_ls_avg,_lr_avg,_ll_avg,_lm_avg, _ma_avg,_ms_avg,_mr_avg,_ml_avg,_mm_avg):
	print ("\nCriando Matriz de Correlação...")
	print ("Salvando dados em: "+str(output_dir)+"\n")

	raw_data = {'Retweets': [_rr_avg['media'],_rl_avg['media'],_rm_avg['media']],
        'Likes': [_lr_avg['media'],_ll_avg['media'],_lm_avg['media']],
        'Mentions': [_mr_avg['media'],_ml_avg['media'],_mm_avg['media']]
        }
        
	df = pd.DataFrame(raw_data, columns = ['Retweets','Likes','Mentions'])
	print ("Média:")	
	print df
	
	raw_data_dp = {'Retweets': [_rr_avg['desvio_padrao'],_rl_avg['desvio_padrao'],_rm_avg['desvio_padrao']],
        'Likes': [_lr_avg['desvio_padrao'],_ll_avg['desvio_padrao'],_lm_avg['desvio_padrao']],
        'Mentions': [_mr_avg['desvio_padrao'],_ml_avg['desvio_padrao'],_mm_avg['desvio_padrao']]
        }
        
	df_dp = pd.DataFrame(raw_data_dp, columns = ['Retweets','Likes','Mentions'])
	print ("Desvio padrão:")
	print df_dp	
	
#	plt.matshow(df)
#	plt.matshow(df,cmap='gray')
#	plt.matshow(df,cmap=plt.cm.get_cmap('Blues', 20))
	plt.matshow(df,cmap=plt.cm.get_cmap('gray_r', 10))		#10 tonalidades
	
	plt.xticks(range(len(df.columns)), df.columns,rotation=30,size=9)
	plt.yticks(range(len(df.columns)), df.columns,rotation=30,size=9)

#	plt.title('Rank-Biased Overlap (Extended) - Closeness Centrality Rank',y=-0.08)
#	plt.colorbar(orientation='horizontal')
	plt.colorbar()
	for (i, j), z in np.ndenumerate(df):													#Show values in the grid
		plt.text(j, i, '{:0.2f}'.format(z), ha='center', va='center',bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.9'),size=8)	

	plt.savefig(output_dir+metric+".png",bbox_inches='tight',dpi=300)
	plt.close()
	print (" - OK! Color Bar salvo em: "+str(output_dir))
	print

######################################################################################################################################################################
#
# Plotar Gŕaficos relacionados aos dados
#
######################################################################################################################################################################
def prepare(metric,file):
	with open(file,'r') as f:
		data = json.load(f)
	pairs = {}
 
 	_aa = []
	_as = []
	_ar = []	
	_al = []
	_am = [] 

 	_sa = []
	_ss = []
	_sr = []	
	_sl = []
	_sm = [] 

 	_ra = []
	_rs = []
	_rr = []	
	_rl = []
	_rm = [] 

 	_la = []
	_ls = []
	_lr = []	
	_ll = []
	_lm = [] 

 	_ma = []
	_ms = []
	_mr = []	
	_ml = []
	_mm = [] 

	
	
	for k,v in data.iteritems():
		for key,value in v.iteritems():
			if key == "aa":
				_aa.append(value)
			elif key == "as":
				_as.append(value)
			elif key == "ar":
				_ar.append(value)
			elif key == "al":
				_al.append(value)
			elif key == "am":
				_am.append(value)

			elif key == "sa":
				_sa.append(value)
			elif key == "ss":
				_ss.append(value)
			elif key == "sr":
				_sr.append(value)
			elif key == "sl":
				_sl.append(value)
			elif key == "sm":
				_sm.append(value)

			elif key == "ra":
				_ra.append(value)
			elif key == "rs":
				_rs.append(value)
			elif key == "rr":
				_rr.append(value)
			elif key == "rl":
				_rl.append(value)
			elif key == "rm":
				_rm.append(value)
				
			elif key == "la":
				_la.append(value)
			elif key == "ls":
				_ls.append(value)
			elif key == "lr":
				_lr.append(value)
			elif key == "ll":
				_ll.append(value)
			elif key == "lm":
				_lm.append(value)
				
				
			elif key == "ma":
				_ma.append(value)
			elif key == "ms":
				_ms.append(value)
			elif key == "mr":
				_mr.append(value)
			elif key == "ml":
				_ml.append(value)
			elif key == "mm":
				_mm.append(value)												

			else:
				print ("Rede inválida")
				sys.exit()	
						
	_aa_avg = calc.calcular_full(_aa)
	_as_avg = calc.calcular_full(_as)	
	_ar_avg = calc.calcular_full(_ar)
	_al_avg = calc.calcular_full(_al)
	_am_avg = calc.calcular_full(_am)

	_sa_avg = calc.calcular_full(_sa)
	_ss_avg = calc.calcular_full(_ss)	
	_sr_avg = calc.calcular_full(_sr)
	_sl_avg = calc.calcular_full(_sl)
	_sm_avg = calc.calcular_full(_sm)

	_ra_avg = calc.calcular_full(_ra)
	_rs_avg = calc.calcular_full(_rs)	
	_rr_avg = calc.calcular_full(_rr)
	_rl_avg = calc.calcular_full(_rl)
	_rm_avg = calc.calcular_full(_rm)

	_la_avg = calc.calcular_full(_la)
	_ls_avg = calc.calcular_full(_ls)	
	_lr_avg = calc.calcular_full(_lr)
	_ll_avg = calc.calcular_full(_ll)
	_lm_avg = calc.calcular_full(_lm)

	_ma_avg = calc.calcular_full(_ma)
	_ms_avg = calc.calcular_full(_ms)	
	_mr_avg = calc.calcular_full(_mr)
	_ml_avg = calc.calcular_full(_ml)
	_mm_avg = calc.calcular_full(_mm)		

	color_bar(metric,_aa_avg,_as_avg,_ar_avg,_al_avg,_am_avg, _sa_avg,_ss_avg,_sr_avg,_sl_avg,_sm_avg, _ra_avg,_rs_avg,_rr_avg,_rl_avg,_rm_avg, _la_avg,_ls_avg,_lr_avg,_ll_avg,_lm_avg, _ma_avg,_ms_avg,_mr_avg,_ml_avg,_mm_avg)
		
	
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
	metric = "top_k_co_occurrence"
	if not os.path.exists(str(data_dir)+str(metric)+".json"):												# Verifica se diretório existe
		print ("Impossível localizar arquivo: "+str(data_dir)+str(metric)+".json")
	else:
		file = str(data_dir)+str(metric)+".json"
		prepare(metric,file)

	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
print "\n#######################################################################\n"	
type_graphs1 = "graphs_with_ego"
type_graphs2 = "graphs_without_ego"
singletons1 = "full"
singletons2 = "without_singletons"
#######################################################################
	
data_dir = "/home/amaury/Dropbox/lists_properties/"+str(type_graphs1)+"_"+str(singletons1)+"/"
output_dir = "/home/amaury/Dropbox/lists_properties_statistics/"+str(type_graphs1)+"_"+str(singletons1)+"/"

#Executa o método main
if __name__ == "__main__": main()