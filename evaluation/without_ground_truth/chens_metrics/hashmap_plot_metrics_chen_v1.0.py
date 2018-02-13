# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import plot_metrics
import calc
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para plotar as métricas de avaliação sem ground_truth do Chen
##					Versão 2 - não considera without singletons
## 				Versão 3 - Filtra os dados salvos para impressão dos gráficos. Arquivos foram salvos com todos os calculos.
######################################################################################################################################################################
def prepare(dataset,metric):
	if not os.path.isdir(dataset):
		print ("Diretório com "+str(metric)+" não encontrado: "+str(dataset))
	else:	
		metric_plot = {}																	# Armazenar o nome da rede e o maior valor do métrica

		for directory in os.listdir(dataset):
			if os.path.isdir(dataset+directory):
				net = str(directory)
				metric_plot[net] = {'threshold':' ',metric:float(0),'std':float(0)}
				
				for file in os.listdir(dataset+directory):
					data_avg_values = []
					threshold = file.split(".json")
					threshold = threshold[0]
					with open(dataset+directory+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							for k,v in data.iteritems():
								data_avg_values.append(v)
							print len(data_avg_values)
												
							M = calc.calcular_full(data_avg_values)
							if M is not None:						
								if	float(M['media']) > metric_plot[net][metric]:
									metric_plot[net] = {'threshold': threshold, metric:float(M['media']),'std':float(M['desvio_padrao'])}
		return metric_plot

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
	print" 					Impressão de Gráficos - Métricas de Avaliação Sem Ground - Truth	"
	print"																											"
	print" Escolha o algoritmo usado na detecção das comunidades									"
	print"																											"
	print"#################################################################################"
	print
	print"  1 - COPRA"
	print"  2 - OSLOM"
	print"  3 - GN"		
	print"  4 - COPRA - Partition"
	print"  5 - INFOMAP - Partition"												
	print
	op1 = int(raw_input("Escolha uma opção acima: "))

	if op1 == 1:
		alg = "copra"
	elif op1 == 2:
		alg = "oslom"
	elif op1 == 3:
		alg = "gn"
	elif op1 == 4:
		alg = "copra_partition"
	elif op1 == 5:
		alg = "infomap"							
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print ("\n")
	print"#################################################################################"
	print
	print"  0 - All Metrics"
	print"  1 - Q - Modularidade"
	print"  2 - N - Modularidade"
	print"  3 - Qds - Modularidade Estendida"
	print"  4 - Intra Edges"
	print"  5 - Intra Density"	
	print"  6 - Contraction"
	print"  7 - Inter Edges"
	print"  8 - Expansion"
	print"  9 - Conductance"
	print"  10 - Modularity Degree"
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
	
	if op2 == 0:
		m = ["modularity","N_modularity","modularity_density","intra_edges","intra_density","contraction","inter_edges","expansion","conductance","modularity_degree"]
		for metric in m:
			data1 = {}
			data3 = {}
######################################################################		
######################################################################

			dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
			data1 = prepare(dataset1,metric)
			title = str(metric)+"_graphs_with_ego_"+str(alg)+"_full"	

######################################################################				
######################################################################

			dataset3 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"	
			data3 = prepare(dataset3,metric)
			title = str(metric)+"_graphs_without_ego_"+str(alg)+"_full"	
			
######################################################################				
######################################################################
			if data1 is not None and data3 is not None:
				if len(data1) == len(data3):
					plot_metrics.plot_full_without_singletons(output,data1,data3,metric,alg)
				else:
					print ("\nImpossível gerar gráfico para os 02 cenários... Data01: "+str(len(data1))+" - Data03: "+str(len(data3))+"\n")					
			else:
				print ("\nImpossível gerar gráfico para os 02 cenários...\n")
				print data1
				print data3	
	
	
		print("\n######################################################################\n")
		print("Script finalizado!")
		print("\n######################################################################\n")		
		sys.exit()
######################################################################				
######################################################################			 
	elif op2 == 1:
		metric = "modularity"
	elif op2 == 2:
		metric = "N_modularity"
	elif op2 == 3:
		metric = "modularity_density"
	elif op2 == 4:
		metric = "intra_edges"
	elif op2 == 5:
		metric = "intra_density"
	elif op2 == 6:
		metric = "contraction"
	elif op2 == 7:
		metric = "inter_edges"
	elif op2 == 8:
		metric = "expansion"		
	elif op2 == 9:
		metric = "conductance"		
	elif op2 == 10:
		metric = "modularity_degree"				
	else:
		print("Opção inválida! Saindo...")
		sys.exit()
	print ("\n")
				
######################################################################
	
	data1 = {}
	data2 = {}
	data3 = {}
	data4 = {}
######################################################################		
######################################################################

	dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
	data1 = prepare(dataset1,metric)
	title = str(metric)+"_graphs_with_ego_"+str(alg)+"_full"	
	if data1 is not None:
		plot_metrics.plot_single(output,data1,metric,alg,title)
	else:
		print ("Impossível gerar gráfico simples para: "+str(title))
######################################################################				
######################################################################

	dataset3 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"	
	data3 = prepare(dataset3,metric)
	title = str(metric)+"_graphs_without_ego_"+str(alg)+"_full"	
	if data3 is not None:				
		plot_metrics.plot_single(output,data3,metric,alg,title)
	else:
		print ("Impossível gerar gráfico simples para: "+str(title))
######################################################################		
######################################################################

	if data1 is not None and data3 is not None:
		if len(data1) == len(data3):
			plot_metrics.plot_full_without_singletons(output,data1,data3,metric,alg)
		else:
			print ("\nImpossível gerar gráfico para os 02 cenários... Data01: "+str(len(data1))+" - Data03: "+str(len(data3))+"\n")
	else:
		print ("\nImpossível gerar gráfico para os 02 cenários...\n")
		print data1
		print data3
######################################################################
######################################################################	
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/chen/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth/chen/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()