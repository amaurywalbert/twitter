	# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab
import numpy as np
import powerlaw
import seaborn as sns
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import math
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
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calcular(valores=None):
	calculos = {}
	if valores:
		if valores.__class__.__name__ == 'list' and calculos.__class__.__name__ == 'dict':
			def somar(valores):
				soma = 0
				for v in valores:
					soma += v
				return soma
 
			def media(valores):
				soma = somar(valores)
				qtd_elementos = len(valores)
				media = soma / float(qtd_elementos)
				return media
 
 			def variancia(valores):
 				_media = media(valores)
 				soma = 0
 				_variancia = 0
 
 				for valor in valores:
 					soma += math.pow( (valor - _media), 2)
 					_variancia = soma / float( len(valores) )
 					return _variancia
 
 			def desvio_padrao(valores):
 				return math.sqrt( variancia(valores) )

			calculos['soma'] = somar(valores)
			calculos['media'] = media(valores)
			calculos['variancia'] = variancia(valores)
			calculos['desvio_padrao'] = desvio_padrao(valores)
			return calculos

######################################################################################################################################################################
#
# Salva os dados de cada algoritmo em formato JSON
#
######################################################################################################################################################################
def save_data(output,data,data_overview):
	if not os.path.exists(output):
		os.makedirs(output)
	print ("\n##################################################\n")
	print ("Salvando dados em: "+str(output))
	
	with open(output+"statistics.json", 'w') as f:
		for k, v in data.iteritems():
			network = k,v	 
			f.write(json.dumps(network)+"\n")	
	with open(output+"statistics_overview.json", 'w') as g:
		for k, v in data_overview.iteritems():	 
			network = k,v	 
			g.write(json.dumps(network)+"\n")	
	print ("##################################################\n")
	
######################################################################################################################################################################
#
# Prepara apresentação dos resultados para o algoritmo COPRA - NMI
#
######################################################################################################################################################################
def nmi_copra(comm_data_dir):
	nmi_data = {}																				# Armazenar todos os valores NMI para cada threshold do COPRA em cada rede - Formato {'n8': {1: {'soma': 6.059981138000007, 'media': 0.025787153778723433, 'desvio_padrao': 0.006377214443559922, 'variancia': 4.0668864059149294e-05}, 2: {'soma': 6.059981138000007...}}	
	nmi_data_overview = {}																	# Armazenar o nome da rede e o maior valor do trheshold do COPRA para o NMI - Formato {{'N1':0.012},...}
	
	if os.path.isdir(comm_data_dir):
		for file in os.listdir(comm_data_dir):
			network = file.split(".json")														# pegar o nome do arquivo que indica o a rede analisada
			network = network[0]
			nmi_data_overview[network] = {'threshold':' ','nmi':float(0)}
			print ("\n##################################################")
			print ("Recuperando dados da rede "+str(network))	

			if os.path.isfile(comm_data_dir+file):		
				with open(comm_data_dir+file, 'r') as f:
					partial = {}

					for line in f:
						comm_data = json.loads(line) 
						for k, v in comm_data.iteritems():
							values = []
							for item in v:
								if not math.isnan(item):											# exclui calculo de NMI que retorna valor NaN
									values.append(item)				

							result = calcular(values)												# Calcula média e outros dados dos NMIs recuperados para o conjunto de egos usando o threshold k				 				
							if result is not None:						
								if	float(result['media']) > nmi_data_overview[network]['nmi']:
									nmi_data_overview[network] = {'threshold':k,'nmi':float(result['media'])}
								partial[k] = result														# Adiciona os caclulos feitos num dicionário com indice k (ou seja, o threshold usado pelo COPRA)
								nmi_data[network] = partial				
			else:
				print ("Arquivo não encontrado: "+str(comm_data_dir+file))
		
			print nmi_data_overview[network]														# Maior média para a rede [network]
	else:
		print ("Diretório não encontrado: "+str(comm_data_dir))					
	print
#	print
#	print nmi_data_overview
	print ("##################################################\n")
	return nmi_data,nmi_data_overview
	print ("##################################################")	

######################################################################################################################################################################
#
# Realiza as configurações necessárias para os dados do NMI
#
######################################################################################################################################################################
def nmi(metric):
		comm_data_dir = str(source)+"graphs_with_ego/"+algorithm+"/"+str(metric)+"/full/"
		output_dir = str(output)+"graphs_with_ego/"+algorithm+"/"+str(metric)+"/full/"
		nmi_data,nmi_data_overview = nmi_copra(comm_data_dir)
		save_data(output_dir,nmi_data,nmi_data_overview)		

		comm_data_dir = str(source)+"graphs_with_ego/"+algorithm+"/"+str(metric)+"/without_singletons/"
		output_dir = str(output)+"graphs_with_ego/"+algorithm+"/"+str(metric)+"/without_singletons/"
		nmi_data,nmi_data_overview = nmi_copra(comm_data_dir)
		save_data(output_dir,nmi_data,nmi_data_overview)	

		comm_data_dir = str(source)+"graphs_without_ego/"+algorithm+"/"+str(metric)+"/full/"
		output_dir = str(output)+"graphs_without_ego/"+algorithm+"/"+str(metric)+"/full/"
		nmi_data,nmi_data_overview = nmi_copra(comm_data_dir)
		save_data(output_dir,nmi_data,nmi_data_overview)		

		comm_data_dir = str(source)+"graphs_without_ego/"+algorithm+"/"+str(metric)+"/without_singletons/"
		output_dir = str(output)+"graphs_without_ego/"+algorithm+"/"+str(metric)+"/without_singletons/"
		nmi_data,nmi_data_overview = nmi_copra(comm_data_dir)
		save_data(output_dir,nmi_data,nmi_data_overview)	

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
	print ("Métrica a ser aplicada na geração dos resultados:\n")
	print("01 - NMI - Normalized Mutual Infomation. ")
	print("02 - Ômega Index.")
	print("03 - Jaccard Similarity.")
	print	
	metric_op = int(raw_input("Escolha uma opção acima: "))
	print ("\n##################################################\n")
#######################################################################
	if metric_op == 01:
		metric = "nmi"
		nmi(metric)
#######################################################################		
	elif metric_op == 02:
		metric = "omega"
		nmi(metric)
#######################################################################
	elif metric_op == 03:
		metric = "jaccard"
		nmi(metric)
#######################################################################
	else:
		metric = ""
		print("Opção inválida! Saindo...")
		exit()	
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
algorithm = "copra"
source = "/home/amaury/Dropbox/evaluation/"
output = "/home/amaury/Dropbox/statistics/"
######################################################################################################################


if __name__ == "__main__": main()