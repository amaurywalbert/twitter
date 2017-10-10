	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import networkx as nx
import matplotlib.pyplot as plt
from math import*

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Gerar Resultados
##								
## # INPUT: Arquivos com os resultado obtidos em cada métricas 
## # OUTPUT:
##		- Arquivos com estatísticas dos resultados
######################################################################################################################################################################

######################################################################################################################################################################
#
# Prepara apresentação dos resultados para o algoritmo COPRA 
#
######################################################################################################################################################################

def copra(graph_type,metric,algorithm):
	for i in range(10):
		i+=1
		communities = str(source_dir)+str(graph_type)+"/"+str(metric)+"/n"+str(i)+"/"+algorithm+"/"
		values = []
		try:		
			for file in os.listdir(communities):										# Para cada arquivo no diretório
				with open(communities+file, 'r') as f:
					print communities+file
					for line in f:
						a = line.split('\t')
						b = float(a[1])
						try:
							values.append(b)
						except Exception as e:
							pass	
			print values				
			print ("#########################")

		except IOError as io:
			print ("Arquivo não encontrado. Continuando.")
		except OSError as os1:
			print ("Diretório não encontrado. Continuando.")
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	print
	print
	print("01 - Communidades extraídas de grafos SEM o ego. (default)")
	print("02 - Communidades extraídas de grafos COM o ego.")
	print
	graph_type_op = int(raw_input("Escolha uma opção acima: "))
	if graph_type_op == 01:
		graph_type = "graphs_without_ego"
	elif graph_type_op == 02:
		graph_type = "graphs_with_ego"
	else:
		graph_type = "graphs_without_ego"
#######################################################################	
	print
	print
	print("01 - NMI - Normalized Mutual Infomation. ")
	print("02 - Ômega Index.")
	print("03 - Jaccard Similarity.")
	print
	print
	metric_op = int(raw_input("Escolha uma opção acima: "))
	if metric_op == 01:
		metric = "nmi"
	elif metric_op == 02:
		metric = "omega"
	elif metric_op == 03:
		metric = "jaccard"
	else:
		metric = ""
		print("Opção inválida! Saindo...")
		exit()
	#######################################################################	
	print
	print
	print("01 - COPRA. ")
	print("02 - ")
	print("03 - ")
	print
	algorithm_op = int(raw_input("Escolha uma opção acima: "))
	if algorithm_op == 01:
		algorithm = "copra"
		copra(graph_type,metric,algorithm)			# Chama função e passa o parâmetros para cálcular as estatísticas para os resultados obtidos pelo algoritmo em questão
	else:
		algorithm = ""
		print("Opção inválida! Saindo...")
		exit()
	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
#####Alterar as linhas para Dropbox quando executado em ambiente de produção
#source_dir = "/home/amaury/Dropbox/evaluation/"
#output_dir = "/home/amaury/Dropbox/statistics/"
source_dir = "/home/amaury/evaluation/"
output_dir = "/home/amaury/statistics/"
######################################################################################################################


if __name__ == "__main__": main()