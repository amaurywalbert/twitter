# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
import plotly
import plotly.plotly as py
import plotly.graph_objs as go				


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Juntar os resultados da Camada Follow para as métricas Small World em apenas um único arquivo.
##									Os conjuntos de egos haviam sido separados para facilitar a paralelização dos cálculos
######################################################################################################################################################################

######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(data,out_file):
	print data
	out_file.write(json.dumps(data)+"\n")				# Salva linha com os dados calculados para o ego i

######################################################################################################################################################################
#
# Prepara os dados
#
######################################################################################################################################################################
def prepare(set1,set2,set3,set4,set5):
	print len(set1),len(set2),len(set3),len(set4),len(set5)
	print
	out_file = open(str(output_dir)+"n1_merged.json",'w')	# Se arquivo não existe então apenas abre o arquivo

	for line in set1:
		data = json.loads(line)
		save_json(data,out_file)

	for line in set2:
		data = json.loads(line)
		save_json(data,out_file)	

	for line in set3:
		data = json.loads(line)
		save_json(data,out_file)

	for line in set4:
		data = json.loads(line)
		save_json(data,out_file)

	for line in set5:
		data = json.loads(line)
		save_json(data,out_file)
				
				
######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	if not os.path.exists(str(source_dir)+"n1_set1.json") or not os.path.exists(str(source_dir)+"n1_set2.json") or not os.path.exists(str(source_dir)+"n1_set3.json") or not os.path.exists(str(source_dir)+"n1_set4.json") or not os.path.exists(str(source_dir)+"n1_set5.json"):
		print ("Arquivos dos cinco conjuntos de egos não encontrados em: ")
		print source_dir
	else:
		f1 = open(str(source_dir)+"n1_set1.json",'r')
		f2 = open(str(source_dir)+"n1_set2.json",'r')
		f3 = open(str(source_dir)+"n1_set3.json",'r')
		f4 = open(str(source_dir)+"n1_set4.json",'r')
		f5 = open(str(source_dir)+"n1_set5.json",'r')
		
		set1 = f1.readlines()
		set2 = f2.readlines()
		set3 = f3.readlines()
		set4 = f4.readlines()
		set5 = f5.readlines()

		if len(set1) != len(set2) and len(set1) != len(set3) and len(set1) != len(set4) and len(set1) != len(set5):
			print ("Diferentes números de egos entre as camadas... Saindo")
			sys.exit()
		else:
			prepare(set1,set2,set3,set4,set5)	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
os.system('clear')
print "################################################################################"
print"																											"
print" Merge Results of S metric for five egos sets in one file								"
print" 			ONLY FOLLOW LAYER								"
print"																											"
print"#################################################################################"
print
print
print"  1 - NetworkX"
print"  2 - SNAP"
			
print
op = int(raw_input("Escolha a biblioteca utilizada para calcular a métrica S : "))
	
if op == 1:
	source_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world/"
	output_dir = source_dir
elif op == 2: 
	source_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world_snap/"
	output_dir = source_dir
else:
	print ("Opção inválida...")
	source_dir = " "
	output_dir = source_dir
	sys.exit()
			
#Executa o método main
if __name__ == "__main__": main()

