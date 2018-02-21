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
## 				Versão 4 - Filtra os resultados das outras métricas com o threshold que retorna a maior Modularity Density
######################################################################################################################################################################

######################################################################################################################################################################
#
# Calcular Modularity Density
#
######################################################################################################################################################################
def modularity_density_calc(dataset,metric,graph_type,alg): # Verifica pelo melhor threshold - aquele com maior Qds. Em caso de empate pega o último threshold verificado.
	if not os.path.isdir(dataset):
		print ("Diretório com "+str(metric)+" não encontrado: "+str(dataset))
	else:	
		qds = {}																	# Armazenar o nome da rede e o maior valor do métrica

		for net in os.listdir(dataset):
			print
			if os.path.isdir(dataset+net):
				qds[net] = {'threshold':' ',metric:float("-inf"),'std':float(0)}
				for file in os.listdir(dataset+net):
					data_avg_values = []
					threshold = file.split(".json")
					threshold = threshold[0]
					with open(dataset+net+"/"+file, 'r') as f:
						data = json.load(f)
						if data is not None:
							for k,v in data.iteritems():
								data_avg_values.append(v)
							#print len(data_avg_values)
												
							M = calc.calcular_full(data_avg_values)
							if M is not None:

								print threshold, M['media']
								
								if	float(M['media']) >= qds[net][metric]:
									qds[net] = {'threshold': threshold, metric:float(M['media']),'std':float(M['desvio_padrao'])}
			print																		
		with open(str(output)+str(graph_type)+"_"+str(alg)+"_modularity_density.json", "w") as f:
			f.write(json.dumps(qds))
		return qds

######################################################################################################################################################################
#
#Calcular demais métricas... 
#
######################################################################################################################################################################
def prepare(dataset,metric,qds):
	if not os.path.isdir(dataset):
		print ("Diretório com "+str(metric)+" não encontrado: "+str(dataset))
	else:	
		metric_plot = {}																	# Armazenar o nome da rede e o maior valor do métrica

		for net in os.listdir(dataset):
			if os.path.isdir(dataset+net):
				threshold = qds[net]['threshold'] 
				if os.path.isfile(dataset+net+"/"+threshold+".json"):
					data_avg_values = []
					with open(dataset+net+"/"+threshold+".json", 'r') as f:
						data = json.load(f)
						if data is not None:
							for k,v in data.iteritems():
								data_avg_values.append(v)
							#print len(data_avg_values)
												
							M = calc.calcular_full(data_avg_values)
							if M is not None:
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

######################################################################		
######################################################################

	metric = "modularity_density"

######################################################################
	graph_type1 = "graphs_with_ego"
	dataset1 = str(source)+str(metric)+"/"+str(graph_type1)+"/"+str(alg)+"/full/"	
	qds1 = modularity_density_calc(dataset1,metric,graph_type1,alg)
	title = str(metric)+"_graphs_with_ego_"+str(alg)+"_full"		
		
######################################################################
	graph_type3 = "graphs_without_ego"
	dataset3 = str(source)+str(metric)+"/"+str(graph_type3)+"/"+str(alg)+"/full/"	
	qds3 = modularity_density_calc(dataset3,metric,graph_type3,alg)
	title = str(metric)+"_graphs_without_ego_"+str(alg)+"_full"	


	if qds1 is not None and qds3 is not None:
		if len(qds1) == len(qds3):
			plot_metrics.plot_full_without_singletons(output,qds1,qds3,metric,alg)
		else:
			print ("\nImpossível gerar gráfico para os 02 cenários... Data01: "+str(len(qds1))+" - Data03: "+str(len(qds3))+"\n")					
	else:
		print ("\nImpossível gerar gráfico para os 02 cenários...\n")
		print qds1
		print qds3

######################################################################		
######################################################################
######################################################################		
######################################################################
		
	m = ["modularity","N_modularity","intra_edges","intra_density","contraction","inter_edges","expansion","conductance","modularity_degree"]
	for metric in m:
		data1 = {}
		data3 = {}
		
######################################################################		

		dataset1 = str(source)+str(metric)+"/graphs_with_ego/"+str(alg)+"/full/"	
		data1 = prepare(dataset1,metric,qds1)
		title = str(metric)+"_graphs_with_ego_"+str(alg)+"_full"	

######################################################################

		dataset3 = str(source)+str(metric)+"/graphs_without_ego/"+str(alg)+"/full/"	
		data3 = prepare(dataset3,metric,qds3)
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

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth_chen/"
output = "/home/amaury/Dropbox/evaluation_hashmap_statistics/without_ground_truth_chen/"

if not os.path.exists(output):
	os.makedirs(output)

#Executa o método main
if __name__ == "__main__": main()