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
##		Status - Versão 1 - Plotar os dados de acordo com as métricas e propriedades calculadas nas redes Multilayer - Number of Communities
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
def color_bar(_aa,_ar,_al,_am,_rr,_rl,_rm,_ll,_lm,_mm,output):
	print ("\nCriando Matriz de Correlação...")
	print ("Salvando dados em: "+str(output)+"\n")

	_ml=_lm
	_ma=_am
	_la=_al
	_ra=_ar
	_lr=_rl
	_mr=_rm

	raw_data = {'Follow': [_aa,_ar,_al,_am],
        'Retweet': [_ra,_rr,_rl,_rm],
        'Like': [_la,_lr,_ll,_lm],
        'Mention': [_ma,_mr,_ml,_mm]
        }
        
	df = pd.DataFrame(raw_data, columns = ['Follow','Retweet','Like','Mention'])	
	print df


	plt.matshow(df,cmap=plt.cm.get_cmap('Blues', 10))
#	plt.matshow(df,cmap=plt.cm.get_cmap('gray_r', 10))		#10 tonalidades
	
	plt.xticks(range(len(df.columns)), df.columns,rotation=30,size=9)
	plt.yticks(range(len(df.columns)), df.columns,rotation=30,size=9)

	plt.colorbar()
	for (i, j), z in np.ndenumerate(df):													#Show values in the grid
		plt.text(j, i, '{:0.2f}'.format(z), ha='center', va='center',bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.9'),size=8)	

	name = "n_comm_correlation"

	plt.savefig(output+name+".png",bbox_inches='tight',dpi=300)
	plt.show()
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
		print data
		color_bar(data['aa']['pearson'],data['ar']['pearson'],data['al']['pearson'],data['am']['pearson'],data['rr']['pearson'],data['rl']['pearson'],data['rm']['pearson'],data['ll']['pearson'],data['lm']['pearson'],data['mm']['pearson'],output_dir)
		
	
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
	metric = "n_comm_correlation"
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
print "################################################################################"
print"																											"
print" Plotar N Comm Correlation	"
print"																											"
print" Escolha o algoritmo usado na detecção das comunidades									"
print"																											"
print"#################################################################################"
print
print"  1 - COPRA - Without Weight - k = 10"
print"  2 - OSLOM - Without Weight - k = 50"
print"  3 - RAK - Without Weight"		
#
#print"  5 - INFOMAP - Partition"
print"  6 - INFOMAP - Partition - Without Weight"												
print
op1 = int(raw_input("Escolha uma opção acima: "))
#
if op1 == 1:
	alg = "copra_without_weight_k10"
	threshold = 10
elif op1 == 2:
	alg = "oslom_without_weight_k50"
	threshold = 50	
elif op1 == 3:
	alg = "rak_without_weight"
	threshold = 1
#elif op1 == 4:
#	alg = "infomap_without_weight"				
#if op1 == 5:
#	alg = "infomap_without_weight"
elif op1 == 6:
	alg = "infomap_without_weight"
	threshold = 10		
else:
	alg = ""
	print("Opção inválida! Saindo...")
	sys.exit()	
print ("\n")
data_dir = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/graphs_with_ego/"+str(alg)+"_without_weight/"	# Diretório com arquivos JSON com métricas e propriedades Calculadas
output_dir = "/home/amaury/Dropbox/evaluation_hashmap_statistics/communities_statistics/graphs_with_ego/"+str(alg)+"_without_weight/"	# Diretório para Salvar os gráficos...

#Executa o método main
if __name__ == "__main__": main()