# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, shutil
import networkx as nx


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular se as redes-ego são small-world.
##								- Considerar apenas redes-ego com a presença do ego.
##								- Calcula-se as métricas a partir da lista de arestas...
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
def create_dir(x):
	if not os.path.exists(x):
		os.makedirs(x)		

######################################################################################################################################################################
#
# Cálcular Métricas para verificar small world
#
######################################################################################################################################################################
def calc_metric(G,metric):
	transitivity = nx.transitivity(G)																	#Calcula o coeficiente de Clustering para o Grafo.
	print i, ego,net,transitivity
	gnm_random_graph(n, m, seed=None, directed=False)
	result = 0
	return transitivity, result
######################################################################################################################################################################
#
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(dataset,name):
	with open(str(output_dir)+str(name)+".json","w") as f:
		f.write(json.dumps(dataset))			
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
	print" Verificação de Small World"
	print"																											"
	print"#################################################################################"
	print			
	print("\n")
	metric = "small_world"
	if os.path.exists(str(output_dir)+"small_world.json"):
		print ("Arquivo de destino já existe!"+(str(output_dir)+"small_world.json"))
	else:	
		create_dir(output_dir)																			# Cria diretótio para salvar arquivos.
		dataset_trans = {}	
		dataset = {}																						# Salvar Arquivos no Formato Json
		i=0																									# Contador do ego
		for ego,v in dictionary.iteritems():
			i+=1
			nets = ["n1","n2","n3","n4"] #[amigos,retweets,likes,menções]					# Camadas de interações no Twitter
			dataset = {}
			dataset_trans = {}
			for net in nets:
				if net == "n1":
					layer = "a"
				elif net == "n2":
					layer = "r"
				elif net == "n3":
					layer = "l"
				elif net == "n4":
					layer = "m"
				else:
					print ("Rede inválida")
					sys.exit()
					
				source = str(data_dir)+str(net)+"/graphs_with_ego/"+str(ego)+".edge_list"
				if not os.path.isfile(source):																				# Verifica se diretório existe	
					print ("Impossível localizar arquivo com lista de arestas: "+str(source))
				else:
					G = nx.read_edgelist(source,create_using=nx.DiGraph())	
					transitivity, result = calc_metric(G,metric)																			# Calcula Métrica
#					dataset_trans[layer] = transitivity
#					dataset[layer] = result

#							
#			dataset_trans[ego] = dataset_trans
#			dataset[ego] = dataset
#			print i, metric, dataset_trans[ego], dataset[ego]
#			print
#		save_json(dataset,name="transitivity")																		# Salvar arquivo no formato JSON
#		save_json(dataset,metric)																						# Salvar arquivo no formato JSON
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

egos_ids = "/home/amaury/graphs_hashmap_infomap_without_weight/n1/graphs_with_ego/"										# Pegar a lista com os ids dos egos
data_dir = "/home/amaury/graphs_hashmap_infomap_without_weight/"																	# Diretório com as redes-ego
output_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world/"	# Pegar a lista com os ids dos egos


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