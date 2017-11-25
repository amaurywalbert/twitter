
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

	n_nodes = (G.GetNodes())														# Numero de vértices
	n_edges = (G.GetEdges())														# Numero de arestas

	_separability = []
	_density = []
	_cohesiveness = []
	_expansion = []
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
		

#		print total_edges_community,community_degree
		
		
		if internal_edges == n_edges or internal_nodes ==0 :													# Penalizar algoritmo que retorna apenas uma comunidade como sendo toda a rede-ego
			result_s = 0
			result_d = 0
			result_c = 0
			result_e = 0
		else:
########################################################################################################### Separability			
			if internal_edges != 0 and external_edges != 0:
				result_s = float(internal_edges)/float(external_edges)+float(internal_edges)				# Acrescentei internal edges no denominador... discutir isso. Como fazer com a divisão por zero??
			else:
				result_s = 0				
			
########################################################################################################### DENSITY

			if ud is False:
				if internal_nodes-1 != 0:
					result_d = float(internal_edges)/(float(internal_nodes)*(float(internal_nodes)-1))
				else:
					result_d = 0					
			else:
				result = (float(internal_nodes)*float(internal_nodes)-1)/2
				if result != 0:
					result_d = float(internal_edges)/float(result)
				else:
					result_d = 0	

########################################################################################################### COHESIVENESS = Conductância

			if internal_edges != 0 and external_edges != 0:
				result_c = float(external_edges)/(2*(float(internal_edges))+float(external_edges))			# Ver pq que tem um 2 no denominador nos artigos  "Metrics for community analisys"
			else:
				result_c = 0

########################################################################################################### EXPANSION

			result_e = float(external_edges)/float(internal_nodes)

			
########################################################################################################### 			 
		_separability.append(result_s)				
		_density.append(result_d)
		_cohesiveness.append(result_c)
		_expansion.append(result_e)
#		print ("community_degree: %d --- internal_nodes: %d --- internal_edges: %d --- external_edges: %d" % (community_degree, internal_nodes, internal_edges,external_edges))
#		print ("separability: %f --- density: %f --- cohesiveness: %f --- expansion: %f" % (result_s,result_d,result_c,result_e))		
#		print
######################################################################################################################################################################
######################################################################################################################################################################
	separability = calc.calcular(_separability)
	density = calc.calcular(_density)
	cohesiveness = calc.calcular(_cohesiveness)
	expansion = calc.calcular(_expansion)	

	return separability,density,cohesiveness,expansion
	