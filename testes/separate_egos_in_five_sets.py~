# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, shutil


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para separar o conjunto de egos em 05 conjuntos, pra facilitar a paralelização dos scripts
##									Salvar um dicionário json com 05 linhas.
##									Usar a partir dos grafos gerados pro infomap sem peso.
## 
######################################################################################################################################################################

######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	os.system('clear')
	i=0																						# Contador do ego
	dataset = {}																			# Salvar Arquivos no Formato Json - linha por linha
	set1 = []
	set2 = []
	set3 = []
	set4 = []
	set5 = []
	for ego,v in dictionary.iteritems():
		if i < 100:
			set1.append(long(ego))
		elif i < 200:
			set2.append(long(ego))
		elif i < 300:
			set3.append(long(ego))			
		elif i < 400:
			set4.append(long(ego))
		else:
			set5.append(long(ego))
		i+=1
	dataset = {"set1":set1,"set2":set2,"set3":set3,"set4":set4,"set5":set5} 
	with open(out_file,"w") as f:
		f.write(json.dumps(dataset)) 	
######################################################################################################################################################################	
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
				
				

egos_ids = "/home/amaury/graphs_hashmap_infomap_without_weight/n1/graphs_with_ego/"	# Pegar a lista com os ids dos egos
out_file = "/home/amaury/Dropbox/egos_in_five_sets.json"
dictionary = {}				#################################################### Tabela {chave:valor} para armazenar lista de egos
###### Iniciando dicionário - tabela hash a partir dos arquivos já criados.
print("######################################################################")
print ("Criando tabela hash...")
n = 0	#Conta quantos arquivos existem no diretório
for file in os.listdir(egos_ids):
	user_id = file.split(".edge_list")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	n+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
#if n <> 500:
#	print ("Diretório não contém lista com todos os egos...")
#	sys.exit()
#else:
#
	#Executa o método main
if __name__ == "__main__": main()