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
	with open(output_dir_json+"n_comm_correlation.json","w") as f:
		f.write(json.dumps(dataset_json))					

######################################################################################################################################################################
#
# Calcula Correlação de Pearson entre n_communities dos pares de layers  
#
######################################################################################################################################################################
def calc_correlation(dataset):
	pairs = {}
	for k,v in dataset.iteritems():
		for j, x in dataset.iteritems():
			print ("Calculando correlação entre camadas: "+str(k)+" e "+str(j))
#			if j >= k and j != k:
			ego1 = v
			ego2 = x					
			name = str(k)+str(j)
			result,p = pearsonr(ego1,ego2)		# Comparando o conjunto de vértices entre as camadas
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
	print" Cálculo de number of communities correlation em entre as camadas Layer			"
	print"																											"
	print"#################################################################################"
	print
	if os.path.exists(output_dir_json+"n_comm_correlation.json"):
		print ("Arquivo de destino já existe!"+str(output_dir_json+"n_comm_correlation.json"))
	else:
		create_dirs(output_dir_json)																			# Cria diretótio para salvar arquivos.
		_a = []
		_r = []
		_l = []
		_m = []
		nets = ['n1','n2','n3','n4']
		i=0
		print ("Preparando dados...")
		for ego,data in dictionary.iteritems():
			i+=1		
			for net in nets:
				with open(source_dir+net+"/"+str(threshold)+".json",'r') as f:
					source = json.load(f)
					if net == "n1":
						try:
							_a.append(source[ego]['n_communities'])
						except Exception:
							_a.append(0)
					elif net == "n2":
						try:
							_r.append(source[ego]['n_communities'])
						except Exception:
							_r.append(0)
					elif net == "n3":
						try:
							_l.append(source[ego]['n_communities'])
						except Exception:
							_l.append(0)
					elif net == "n4":
						try:
							_m.append(source[ego]['n_communities'])
						except Exception:
							_m.append(0)
					else:
						print ("\nErro!!\n")
						sys.exit()
			print ("Ego: "+str(i))						
		n_comm = {"a":_a,"r":_r,"l":_l,"m":_m}
		pairs = calc_correlation(n_comm) 
		save_json(pairs)																										# Salvar arquivo no formato JSON
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
print" Calcular N Comm Correlation	"
print"																											"
print"																											"
print"#################################################################################"
print

print "Algoritmo utilizado na detecção das comunidades"
print
print"  1 - COPRA - Without Weight - K=10"
print"  2 - COPRA - Without Weight - K=2-20"
print"  4 - OSLOM - Without Weight - K=50"
print"  5 - RAK - Without Weight"		
print"  6 - INFOMAP - Partition - Without Weight"												
print
op2 = int(raw_input("Escolha uma opção acima: "))
#
if op2 == 1:
	alg = "copra_without_weight_k10"
elif op2 == 2:
	alg = "copra_without_weight"
elif op2 == 4:
	alg = "oslom_without_weight_k50"
elif op2 == 5:
	alg = "rak_without_weight"
elif op2 == 6:
	alg = "infomap_without_weight"		
else:
	alg = ""
	print("Opção inválida! Saindo...")
	sys.exit()	
print ("\n")
print	
	
data_dir = "/home/amaury/graphs_hashmap/n1/graphs_with_ego/"												# Pegar a lista com os ids dos egos
source_dir = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/graphs_with_ego/"+str(alg)+"/full/"
output_dir_json = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/graphs_with_ego/"+str(alg)+"/"	# Pegar a lista com os ids dos egos


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