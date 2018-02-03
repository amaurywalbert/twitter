
# -*- coding: latin1 -*-
################################################################################################
import sys, time, os, os.path, math, calc
import networkx as nx

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script com funções para cálculo de métricas de avaliação sem                                                truth com a biblioteca NETWORKx
## 
######################################################################################################################################################################
def calc_metrics(communities,G,uw,ud):
######################################################################################################################################################################



	average_degree = [] 
	conductance = []		
	cut_ratio = []
	density = []
	expansion = []
	normal_cut_ratio = []
	separability = []
	clustering = []

	if ud is False:													#Para grafos direcionados...
		for k,community in communities.iteritems():
			_average_degree = 0 
			_conductance = 0		
			_cut_ratio = 0
			_density = 0
			_expansion = 0
			_normal_cut_ratio = 0
			_separability = 0
			
			average_degree.append(_average_degree)														#Armazena os resultados para cada partição para depois fazer a média do ego. 		
			conductance.append(_conductance)																#Armazena os resultados para cada partição para depois fazer a média do ego.
			cut_ratio.append(_cut_ratio)																	#Armazena os resultados para cada partição para depois fazer a média do ego.		
			density.append(_density)																		#Armazena os resultados para cada partição para depois fazer a média do ego.
			expansion.append(_expansion)																	#Armazena os resultados para cada partição para depois fazer a média do ego.
			normal_cut_ratio.append(_normal_cut_ratio)												#Armazena os resultados para cada partição para depois fazer a média do ego.		
			separability.append(_separability)															#Armazena os resultados para cada partição para depois fazer a média do ego.
	
	else:																			#Para grafos não direcionados...
		clustering_of_G = nx.clustering(G,weight='weight')			#Calcula o coeficiente de Clustering para o Grafo.
		
		for k,community in communities.iteritems():
			_average_degree = 0 
			_conductance = 0		
			_cut_ratio = 0
			_density = 0
			_expansion = 0
			_normal_cut_ratio = 0
			_separability = 0
############################################################################################################ 	CLUSTERING COEFFICIENT	 
			_cc = []										#Anexar os coeficientes de clustering de cada Nó na comunidade
			for Node in community:
				try:
					_cc.append(clustering_of_G[Node])
				except Exception as e:
					print ("Error - "+str(e))
			if _cc is not None:
				_clustering = calc.calcular(_cc)		#Trazer a média do coeficiente de clustering da comunidade
				clustering.append(_clustering['media'])												#Armazena os resultados para cada partição para depois fazer a média do ego.
			else:
				_clustering = 0
				clustering.append(_clustering)															#Armazena os resultados para cada partição para depois fazer a média do ego.
#############################################################################################################				
				
			average_degree.append(_average_degree)														#Armazena os resultados para cada partição para depois fazer a média do ego. 		
			conductance.append(_conductance)																#Armazena os resultados para cada partição para depois fazer a média do ego.
			cut_ratio.append(_cut_ratio)																	#Armazena os resultados para cada partição para depois fazer a média do ego.		
			density.append(_density)																		#Armazena os resultados para cada partição para depois fazer a média do ego.
			expansion.append(_expansion)																	#Armazena os resultados para cada partição para depois fazer a média do ego.
			normal_cut_ratio.append(_normal_cut_ratio)												#Armazena os resultados para cada partição para depois fazer a média do ego.		
			separability.append(_separability)															
				
	
	avg_ad = calc.calcular_full(average_degree)	
	avg_c = calc.calcular_full(conductance)
	avg_cut_r = calc.calcular_full(cut_ratio)
	avg_d = calc.calcular_full(density)
	avg_e = calc.calcular_full(expansion)
	avg_normal_cut = calc.calcular_full(normal_cut_ratio)
	avg_s = calc.calcular_full(separability)
	avg_cc = calc.calcular_full(clustering)		

	return avg_ad, avg_c, avg_cut_r, avg_d, avg_e, avg_normal_cut, avg_s, avg_cc
	
