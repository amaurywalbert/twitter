	# -*- coding: latin1 -*-
################################################################################################
#	
#
# O módulo subprocess é necessário para executar comandos externos ao Python
import subprocess 
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import networkx as nx
import matplotlib.pyplot as plt
from math import*

reload(sys)
sys.setdefaultencoding('utf-8')




######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de validação dos resultados - Nomalized Mutual Information
##					- NMI - Andrea Lancichinetti et al 2009 New J. Phys. 11 033015
##								
## # INPUT:
##		- Comunidades detectadas - Arquivos texto para cada ego em que cada linha contendo os ids do usuários representam uma comunidade do ego.
##		- Comunidades Ground-Truth - Arquivo texto para cada ego em que cada linha contendo os ids do usuários representam uma Lista do ego.
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	return_code = subprocess.Popen(['/home/amaury/algoritmos/Metricas/mutual3/mutual', '/home/amaury/algoritmos/Metricas/mutual3/one.dat', '/home/amaury/algoritmos/Metricas/mutual3/two.dat'],stdout=subprocess.PIPE)

	output = return_code.communicate()[0]
	print ("Saída: "+str(output))
	a = output.split('\t')
	b= float(a[1])
	print a
	print b
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
communities = "/home/amaury/dataset/n1/egos_limited_5k/bin/"###### Diretório contendo os arquivos dos Egos
ground_truth = "/home/amaury/dataset/n1/alters/bin/" # Diretório contendo os arquivos dos Alters
output_dir = "/home/amaury/graphs/n5/graphs_without_ego/" ################# Diretório para armazenamento dos arquivos das listas de arestas 
######################################################################################################################


if __name__ == "__main__": main()