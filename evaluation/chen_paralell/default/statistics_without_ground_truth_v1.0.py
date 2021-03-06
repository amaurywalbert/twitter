	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random, math
import numpy as np
from math import*
import calc
import plot_statistics_chen

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Gerar Estatísticas a partir dos dados Obtidos pelo CHEN
##				
##							0.2 - Calcula qual melhor threshold
##							0.3 - Plota gráficos comparando cada métrica
##												
## # INPUT: Arquivos com os resultado obtidos em cada métricas 
## # OUTPUT:
##		- Arquivos com estatísticas dos resultados
######################################################################################################################################################################


######################################################################################################################################################################
#
# Prepara apresentação dos resultados para cada - METRICA
#
######################################################################################################################################################################
def algorithm(data_source,output_dir,metric):
	
	data_overview = {}																	# Armazenar o nome da rede e o maior valor do trheshold do algoritmo para a MetricaI - Formato {{'N1':0.012},...	
	data = {}

	if not os.path.isdir(data_source):
		print ("\n##################################################\n\n")
		print ("Diretório não encontrado: "+str(data_source))
		print ("\n\n##################################################\n")					
	else:	

		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
	
		for file in os.listdir(data_source):
			network = file.split(".json")														# pegar o nome do arquivo que indica o a rede analisada
			network = network[0]

			data_overview[network] = {'threshold':' ',metric:float("-inf")}
			print ("##################################################")
			print ("Preparando resultados para a métrica: "+(metric)+" - Recuperando dados da rede "+str(network))	
		
			with open(data_source+file, 'r') as g:
				for line in g:
					comm_data = json.loads(line) 
					for k, v in comm_data.iteritems():										# Para cada threshold
						values = []
						for item in v:
							if not math.isnan(item):
								if item != float("inf") and item != float("-inf"): 											# exclui calculo de da METRICA que retorna valor NaN e Infinity
									values.append(item)
						print 						
						print metric
						print values
						print
													
						result = calc.calcular_full(values)									# Calcula média e outros dados da METRICA recuperados para o conjunto de egos usando o threshold k				 				
						if result is not None:	
														
							if	float(result['media']) > data_overview[network][metric]:
								data_overview[network] = {'threshold':k,metric:float(result['media'])}
								result['n_egos'] = len(values)
								result['t_egos'] = len(v)
								data[network] = {'threshold':k,metric:result}
		print ("##################################################")	
	
		with open(output_dir+metric+".json", 'w') as f:
			for k in data:
				output_file = {}
				output_file[k] = data[k]
				f.write(json.dumps(output_file)+"\n")
	
	return data_overview


######################################################################################################################################################################
#
# Realiza as configurações necessárias para os dados do METRICA
#
######################################################################################################################################################################
def instructions(alg):
################################################################################################

	source_dir = str(source)+"graphs_with_ego/"+alg+"/by_metrics/full/"
	output_dir = str(output)+"graphs_with_ego/"+alg+"/by_metrics/full/"
	
	data_print1 = {}

	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):
			data_source = source_dir+metric+"/"												# Diretório com os resultados de cada métrica
			data_overview = algorithm(data_source,output_dir,metric)	
			data_print1[metric] = data_overview

################################################################################################

	source_dir = str(source)+"graphs_with_ego/"+alg+"/by_metrics/without_singletons/"
	output_dir = str(output)+"graphs_with_ego/"+alg+"/by_metrics/without_singletons/"
		
	data_print2 = {}

	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):
			data_source = source_dir+metric+"/"												# Diretório com os resultados de cada métrica
			data_overview = algorithm(data_source,output_dir,metric)	
			data_print2[metric] = data_overview
################################################################################################

	source_dir = str(source)+"graphs_without_ego/"+alg+"/by_metrics/full/"
	output_dir = str(output)+"graphs_without_ego/"+alg+"/by_metrics/full/"

	data_print3 = {}
	
	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):
			data_source = source_dir+metric+"/"												# Diretório com os resultados de cada métrica
			data_overview = algorithm(data_source,output_dir,metric)	
			data_print3[metric] = data_overview
################################################################################################

	source_dir = str(source)+"graphs_without_ego/"+alg+"/by_metrics/without_singletons/"
	output_dir = str(output)+"graphs_without_ego/"+alg+"/by_metrics/without_singletons/"
		
	data_print4 = {}
	
	for metric in os.listdir(source_dir):													# Para cada Métrica...
		if os.path.isdir(source_dir+metric):
			data_source = source_dir+metric+"/"												# Diretório com os resultados de cada métrica
			data_overview = algorithm(data_source,output_dir,metric)	
			data_print4[metric] = data_overview
################################################################################################
# Salvando Gráficos
	output_graphics = output+"/graphics/"

	for k, v in data_print1.iteritems():
		
		plot_statistics_chen.plot_bars_full(output_graphics,data_print1[k],data_print2[k],data_print3[k],data_print4[k],k,alg)		
		
######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "\n#######################################################################\n"	

	print "\n#######################################################################\n"	
	print ("Algoritmo usado na detecção das comunidades:\n")
	print("01 - COPRA ")
	print("02 - OSLOM")
	print	
	alg_op = int(raw_input("Escolha uma opção acima: "))
	print ("\n##################################################\n")
#######################################################################
	if alg_op == 01:
		alg = "copra"
#######################################################################		
	elif alg_op == 02:
		alg = "oslom"
#######################################################################
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		exit()	
#######################################################################

	instructions(alg)
	
#######################################################################
	print
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
#####Alterar as linhas para Dropbox quando executado em ambiente de produção
source = "/home/amaury/Dropbox/Chen_software_results/without_ground_truth/"
output = "/home/amaury/Dropbox/Chen_software_statistics/without_ground_truth/"
######################################################################################################################

if __name__ == "__main__": main()