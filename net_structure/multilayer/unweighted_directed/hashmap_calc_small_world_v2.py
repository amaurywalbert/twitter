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
##					Versão 2 - Corrige o Cálculo do Average Shortest Path Lenght em Grafos Direcionados com o artigo abaixo:
##									Analysis of average shortest-path length of scale-free network - Mao, Guoyong - Zhang, Ning 2013
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
# Salvar arquivo no formato JSON: ego_id:{as:data,ar:data,al:data,am:data,...,rm:data}  
#
######################################################################################################################################################################
def save_json(ego,dataset,out_file):
	out_file.write(json.dumps(dataset)+"\n")				# Salva linha com os dados calculados para o ego i
	ego = long(ego)
	egos_saved[ego] = ego										# Adiciona o id do ego na tabela hash dos já calculados
	
		
######################################################################################################################################################################
#
# Cálcular Métricas para verificar small world
#
######################################################################################################################################################################
def calc_metric(net,i,ego,G):
	nodes_G = G.nodes()
	edges_G = G.edges()


################################################################################## RANDOM GRAPH
	print (str(net)+" "+str(i)+" - Gerando grafo aleatório com "+str(len(nodes_G))+" vertices e "+str(len(edges_G))+" arestas...")
	connected = False
	while not connected:
		print (str(net)+" "+str(i)+" - Testando se grafo aleatório é conectado...")		
		Gnm = nx.gnm_random_graph(len(nodes_G), len(edges_G), directed=True)	# Cria um grafo aleatório com as mesmas dimensões do original (nodes,edges)
		connected = nx.is_weakly_connected(Gnm)
	print (str(net)+" "+str(i)+" - Grafo conectado... OK")
	nodes_Gnm = Gnm.nodes()
	edges_Gnm = Gnm.edges()

################################################################################## TRANSITIVIDADE
	print (str(net)+" "+str(i)+" - Calculando a transitividade do grafo...")
	transitivity_G = nx.transitivity(G)												# Calcula a transitividade do grafo.
	print (str(net)+" "+str(i)+" - Calculando a transitividade do grafo aleatório...")
	transitivity_Gnm = nx.transitivity(Gnm)										# Calcula a transitividade do grafo aleatório


################################################################################## AVERAGE SHORTEST PATH LENGHT
	print (str(net)+" "+str(i)+" - Calculando média dos menores caminhos mínimos do grafo...")	
	t_spl = 0.0																				# Somatório dos caminhos mínimos = total do somatório dos caminhos mínimos de cada vértice
	n_paths = 0																				# Contador para quantidade de caminhos mínimos
	for node in nodes_G:
		node_spl = nx.shortest_path_length(G,source=node)
		t_spl += sum(node_spl.values())
		n_paths += (len(node_spl) - 1)
	avg_spl_G = t_spl/n_paths															# Calcula a média dos caminhos mínimos para todo o grafo.


	print (str(net)+" "+str(i)+" - Calculando média dos menores caminhos mínimos do grafo aleatório...")
	t_spl = 0.0																				# Somatório dos caminhos mínimos = total do somatório dos caminhos mínimos de cada vértice
	n_paths = 0																				# Contador para quantidade de caminhos mínimos
	for node in nodes_Gnm:
		node_spl = nx.shortest_path_length(Gnm,source=node)
		t_spl += sum(node_spl.values())
		n_paths += (len(node_spl) - 1)
	avg_spl_Gnm = t_spl/n_paths														# Calcula a média dos caminhos mínimos para todo o grafo.


################################################################################## S METRIC

	if transitivity_Gnm == 0:
		GAMMA = 0
	else:		
		GAMMA = float(transitivity_G)/float(transitivity_Gnm)					# Numerador da métrica S
	LAMBDA = float(avg_spl_G)/float(avg_spl_Gnm)									# Denominador da métrica S
	

	S = float(GAMMA)/float(LAMBDA)													# Métrica S de acordo com o artigo que o Prof. Thierson enviou
	return transitivity_G, transitivity_Gnm, avg_spl_G, avg_spl_Gnm, S

######################################################################################################################################################################
#
# Preparar os dados  
#
######################################################################################################################################################################
def prepare(net,out_file):
	i=0																											# Contador do ego
	for ego,v in dictionary.iteritems():
		i+=1
		if ego in egos_saved:
			print (str(net)+" "+str(i)+" - Métrica já calculada para o ego: "+str(ego))		
		else:	
			dataset = {}																						# Salvar Arquivos no Formato Json - linha por linha
			source = str(data_dir)+str(net)+"/graphs_with_ego/"+str(ego)+".edge_list"
			if not os.path.isfile(source):																# Verifica se diretório existe	
				print (str(net)+" "+str(i)+" - Impossível localizar arquivo com lista de arestas: "+str(source))
			else:
				G = nx.read_edgelist(source,create_using=nx.DiGraph())
				transitivity_G,transitivity_Gnm, avg_spl_G, avg_spl_Gnm, S = calc_metric(net,i,ego,G) # Calcula Métrica
				dataset[ego] = {"transitivity_G":transitivity_G,"transitivity_Gnm":transitivity_Gnm,"avg_spl_G":avg_spl_G,"avg_spl_Gnm":avg_spl_Gnm,"S":S}			
				print net,i,ego,dataset[ego]
				print("\n###########################################################")
				print

				save_json(ego,dataset,out_file)										# Salvar arquivo no formato JSON com todos os dados calculados

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
	print
	print"  1 - Follow"
#	print"  9 - Follwowers"
	print"  2 - Retweets"
	print"  3 - Likes"
	print"  4 - Mentions"
	
#	print " "
#	print"  5 - Co-Follow"
#	print" 10 - Co-Followers"				
#	print"  6 - Co-Retweets"
#	print"  7 - Co-Likes"
#	print"  8 - Co-Mentions"
			
	print
	op = int(raw_input("Escolha uma opção acima: "))
	
	print("\n###########################################################")
	net = "n"+str(op)

	if op not in (1,2,3,4):
		print ("Opção inválida...")
		sys.exit()
	
	if os.path.exists(str(output_dir)+str(net)+".json"):
		print ("Arquivo de destino já existe! "+str(output_dir)+str(net)+".json - Fazendo leitura do arquivo...\n")
		out_file = open(str(output_dir)+str(net)+".json",'a+')
		for line in out_file:
			data_saved = json.loads(line)
			for k,v in data_saved.iteritems():
				k = long(k)
				egos_saved[k] = k														#lê o arquivo e armazena uma tabela hash com o id dos egos já calculados
	else:
		out_file = open(str(output_dir)+str(net)+".json",'a+')			# Se arquivo não existe então apenas abre o arquivo

	prepare(net,out_file)													# Prepara os dados para cálculo e armazenamento dos dados
	
	print("\n######################################################################\n")
	print("Script finalizado!")
	print("\n######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

egos_ids = "/home/amaury/graphs_hashmap_infomap_without_weight/n1/graphs_with_ego/"										# Pegar a lista com os ids dos egos
data_dir = "/home/amaury/graphs_hashmap_infomap_without_weight/"																# Diretório com as redes-ego
output_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world/"	# Pegar a lista com os ids dos egos

create_dir(output_dir)																					# Cria diretótio para salvar arquivos.	
	
metric = "small_world"
egos_saved = {}

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