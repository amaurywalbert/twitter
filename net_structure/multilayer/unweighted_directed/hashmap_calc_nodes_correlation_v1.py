# -*- coding: latin1 -*-
################################################################################################
#	
#
import snap, datetime, sys, time, json, os, os.path, shutil, time, random, math
import numpy as np
from math import*
from scipy.stats.stats import pearsonr    


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular a correlação entre número de vértices entre as camadas
##								- Considerar apenas redes-ego com a presença do ego.
## 
##	INPUT: Redes-ego
##
## Output: arquivo texto. Formato:
##
##ID_ego a:amigos s:seguidores r:retuítes l:likes m:menções 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cria diretórios
#
######################################################################################################################################################################
def create_dirs(x):
	if not os.path.exists(x):
		os.makedirs(x)
									
######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(dataset_json):
	with open(output_dir_json+"nodes_correlation.json","w") as f:
		f.write(json.dumps(dataset_json))					

######################################################################################################################################################################
#
# Calcula Correlação de Pearson entre nodes dos pares de layers  
#
######################################################################################################################################################################
def calc_correlation(dataset):
	pairs = {}
	for k,v in dataset.iteritems():
		for j, x in dataset.iteritems():
#			if j >= k and j != k:
				nodes1 = v
				nodes2 = x					
				name = str(k)+str(j)
				result,p = pearsonr(nodes1,nodes2)		# Comparando o conjunto de vértices entre as camadas
				pairs[name]={"pearson":result,"p-value":p} 
	print pairs
	return pairs


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
	print" Cálculo de nodes correlation em entre as camadas Layer			"
	print"																											"
	print"#################################################################################"
	print
	i=0
	if os.path.exists(output_dir_json+"nodes_correlation.json"):
		print ("Arquivo de destino já existe!"+str(output_dir_json+"nodes_correlation.json"))
	else:
		create_dirs(output_dir_json)																			# Cria diretótio para salvar arquivos.
		_a = []
		_s = []
		_r = []
		_l = []
		_m = []
		with open(source_file,'r') as f:
			source = json.load(f)
			for ego,v in dictionary.iteritems():	#Separar os vetores com as informações de cada ego em cada camada.
				_a.append(source[ego]['a'])
				_s.append(source[ego]['s'])
				_r.append(source[ego]['r'])
				_l.append(source[ego]['l'])
				_m.append(source[ego]['m'])				
			nodes = {"a":_a,"s":_s,"r":_r,"l":_l,"m":_m}
			pairs = calc_correlation(nodes) 
		save_json(pairs)																										# Salvar arquivo no formato JSON
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

data_dir = "/home/amaury/graphs_hashmap/n1/graphs_with_ego/"												# Pegar a lista com os ids dos egos
source_file = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/basics/nodes.json"
output_dir_json = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/"	# Pegar a lista com os ids dos egos


dictionary = {}				#################################################### Tabela {chave:valor} para armazenar lista de egos
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print("######################################################################")
print ("Criando tabela hash...")
n = 0	#Conta quantos arquivos existem no diretório
for file in os.listdir(data_dir):
	user_id = file.split(".edge_list")
	user_id = str(user_id[0])
	dictionary[user_id] = user_id
	n+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
if n <> 500:
	print ("Diretório não contém lista com todos os egos...")
	sys.exit()
else:

	#Executa o método main
	if __name__ == "__main__": main()