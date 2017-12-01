
# -*- coding: latin1 -*-
################################################################################################
import snap, sys, time, os, os.path, math, calc

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script com funções para cálculo de métricas de avaliação sem ground truth
## 
######################################################################################################################################################################
def calc_metrics(communities,G,ud):
######################################################################################################################################################################
######################################################################################################################################################################	
	def calc_average_degree(n_edges,internal_edges,internal_nodes):
		if ud is False:
			result = float(internal_edges)/float(internal_nodes)
		else:
			result = (2*float(internal_edges))/float(internal_nodes)
		return result
######################################################################################################################################################################
######################################################################################################################################################################	
	def calc_conductance(n_edges,internal_edges,external_edges,internal_nodes,external_nodes):			
		if ud is False:
			if internal_edges != 0 and external_edges != 0:															# Provavelmente vamos excluir esse cálculo
				result = float(external_edges)/(2*(float(internal_edges))+float(external_edges))			# Ver pq que tem um 2 no denominador nos artigos  "Metrics for community analisys"
			else:																													# Cálculo tá confuso... parece que o calculo correto cresce exponencialmente no numero de vértices da comunidade...
				result = 0
		else:
			if internal_edges != 0 and external_edges != 0:															# Provavelmente vamos excluir esse cálculo
				result = float(external_edges)/(float(internal_edges)+float(external_edges))				# Ver pq que tem um 2 no denominador nos artigos  "Metrics for community analisys"
			else:																													# Cálculo tá confuso... parece que o calculo correto cresce exponencialmente no numero de vértices da comunidade...
				result = 0						
		return result
######################################################################################################################################################################
######################################################################################################################################################################	
	def calc_cut_r(n_edges,internal_edges,external_edges,n_nodes,internal_nodes):
		result = float(external_edges)/(float(internal_nodes)*(float(n_nodes)-float(internal_nodes)))				
		return result
######################################################################################################################################################################
######################################################################################################################################################################	
	def calc_density(n_edges,internal_edges,internal_nodes):
		if ud is False:
			if internal_nodes-1 != 0:
				result = float(internal_edges)/(float(internal_nodes)*(float(internal_nodes)-1))
			else:
				result = 0					
		else:
			_result = (float(internal_nodes)*float(internal_nodes)-1)/2
			if _result != 0:
				result = float(internal_edges)/float(_result)
			else:
				result = 0				
		return result
######################################################################################################################################################################
######################################################################################################################################################################			
	def calc_expansion(n_edges,internal_edges,external_edges,internal_nodes):			
		result = float(external_edges)/float(internal_nodes)
		return result	
######################################################################################################################################################################
######################################################################################################################################################################	
	def calc_normal_cut(n_edges,internal_edges,external_edges):
		if ud is False:
			operator1 = float(external_edges)/(2*float(internal_edges)+float(external_edges))
			operator2 = float(external_edges)/(2*(n_edges-float(internal_edges))+float(external_edges))
			result = operator1+operator2					
		else:
			operator1 = float(external_edges)/(float(internal_edges)+float(external_edges))
			operator2 = float(external_edges)/((n_edges-float(internal_edges))+float(external_edges))
			result = operator1+operator2									
		return result		
######################################################################################################################################################################
######################################################################################################################################################################
	def calc_separability(n_edges,internal_edges,external_edges,internal_nodes): 
		if internal_edges != 0 and external_edges != 0:
			result = float(internal_edges)/float(external_edges)					# FALTA VERIFICAR A DIVISÃO POR ZERO!
		else:
			result = 0				
		return result
######################################################################################################################################################################
######################################################################################################################################################################
	
	n_nodes = (G.GetNodes())														# Numero de vértices
	n_edges = (G.GetEdges())														# Numero de arestas

	_metric_ad = []																	#AverageDegree by community
	_metric_c = []																		#Conductance by community
	_metric_cut_r = []																#Cut Ratio by community
	_metric_d = []																		#Density by community
	_metric_e = []																		#Expansion by community
	_metric_normal_cut = []															#Normalized Cut by community	
	_metric_s = []																		#Separability by community
#	print ("Número de vértices: "+str(n_nodes)+" - Número de Arestas: "+str(n_edges))			

	for k,community in communities.iteritems():
		internal_edges = 0												# Arestar que entram na comunidade
		external_edges = 0												# Arestas que saem da comunidade
		internal_nodes = 0												# Vértices da comunidades
		external_nodes = 0

		in_degree = 0														# Só pra confirmar que estamos verificando todas as arestas que entram na comunidade		
		out_degree = 0														# Só pra confirmar que estamos verificando todas as arestas que saem na comunidade
		community_degree = 0
				
		if ud is False:										#PARA GRAFOS DIRECIONADOS	
			for NI in G.Nodes():									# Para os nós da rede-ego:
				if NI.GetId() in community:						# Se o nó está na comunidade:
					internal_nodes+=1								# internal_nodes recebe + 1												
					in_degree+=NI.GetInDeg()					# in_degree	acrescenta o grau de entrada do nó						
					out_degree+=NI.GetOutDeg()					# out_degree acrescenta o grau de saída do nó
					
					for edge in NI.GetOutEdges():				# Para arestas de saída do nó:
						if edge in community:						# se o destino da aresta está na comunidade
							internal_edges+=1								#internal edge recebe +1					
						else:												# senao
							external_edges+=1								# external_edge recebe +1			

					for edge in NI.GetInEdges():				# Para arestas de entrada no nó:
						if edge in community:						# se o destino da aresta está na comunidade
							internal_edges+=1								#internal edge recebe +1					
						else:												# senao
							external_edges+=1								# external_edge recebe +1		

			internal_edges = float(internal_edges)/2
			external_edges = float(external_edges)/2
			total_edges_community = float(internal_edges)+float(external_edges)						#Essas duas linhas devem retornar os mesmos resultados, embora os operandos sejam diferentes...			
			community_degree = (float(in_degree)+float(out_degree))/2									#Essas duas linhas devem retornar os mesmos resultados, embora os operandos sejam diferentes...
			
			
				
		else:														#PARA GRAFOS NÃO DIRECIONADOS
			for NI in G.Nodes():									# Para os nós da rede-ego:
				if NI.GetId() in community:						# Se o nó NÃO está na comunidade:
					internal_nodes+=1								# internal_nodes recebe + 1
					in_degree+=NI.GetInDeg()					# in_degree	acrescenta o grau de entrada do nó
					#Não precisa do outdegree pq as arestas sao contadas tanto pra entrada quanto pra saida						
					for edge in NI.GetOutEdges():				# Para arestas de saída do nó:
						if edge in community:						# se o destino da aresta está na comunidade
							internal_edges+=1								#internal edge recebe +1					
						else:												# senao
							external_edges+=1								# external_edge recebe +1			
		
			internal_edges = float(internal_edges)/2
			external_edges = float(external_edges)/2
			total_edges_community = float(internal_edges)+float(external_edges)						#Essas duas linhas devem retornar os mesmos resultados, embora os operandos sejam diferentes...			
			community_degree = float(in_degree)/2																#Essas duas linhas devem retornar os mesmos resultados, embora os operandos sejam diferentes...

######################################################################################################################################################################
######################################################################################################################################################################
		if internal_edges == n_edges or internal_nodes == 0 :												# Penalizar algoritmo que retorna apenas uma comunidade como sendo toda a rede-ego ou retorna valor para id que não corresponde a um vértice da rede
			_result_ad = 0 
 			_result_c = 0		
 			_result_cut_r = 0
 			_result_d = 0
 			_result_e = 0
 			_result_normal_cut = 0
			_result_s = 0
		else:	
			_result_ad = calc_average_degree(n_edges,internal_edges,internal_nodes) 
 			_result_c = calc_conductance(n_edges,internal_edges,external_edges,internal_nodes,external_nodes)		
 			_result_cut_r = calc_cut_r(n_edges,internal_edges,external_edges,n_nodes,internal_nodes)
 			_result_d = calc_density(n_edges,internal_edges,internal_nodes)
 			_result_e = calc_expansion(n_edges,internal_edges,external_edges,internal_nodes)
 			_result_normal_cut = calc_normal_cut(n_edges,internal_edges,external_edges)
			_result_s = calc_separability(n_edges,internal_edges,external_edges,internal_nodes)

		_metric_ad.append(_result_ad)																			#Armazena os resultados para cada partição para depois fazer a média do ego. 		
		_metric_c.append(_result_c)																			#Armazena os resultados para cada partição para depois fazer a média do ego.
		_metric_cut_r.append(_result_cut_r)																	#Armazena os resultados para cada partição para depois fazer a média do ego.		
		_metric_d.append(_result_d)																			#Armazena os resultados para cada partição para depois fazer a média do ego.
		_metric_e.append(_result_e)																			#Armazena os resultados para cada partição para depois fazer a média do ego.
		_metric_normal_cut.append(_result_normal_cut)													#Armazena os resultados para cada partição para depois fazer a média do ego.		
		_metric_s.append(_result_s)																			#Armazena os resultados para cada partição para depois fazer a média do ego.
	
	avg_ad = calc.calcular(_metric_ad)	
	avg_c = calc.calcular(_metric_c)
	avg_cut_r = calc.calcular(_metric_cut_r)
	avg_d = calc.calcular(_metric_d)
	avg_e = calc.calcular(_metric_e)
	avg_normal_cut = calc.calcular(_metric_normal_cut)
	avg_s = calc.calcular(_metric_s)		

	return avg_ad, avg_c, avg_cut_r, avg_d, avg_e, avg_normal_cut, avg_s
	
