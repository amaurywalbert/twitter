# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, shutil, snap
import networkx as nx


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Script para calcular se as redes-ego são small-world.
##								- Considerar apenas redes-ego com a presença do ego.
##								- Calcula-se as métricas a partir da lista de arestas...
##								- Usa biblioteca SNAP
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
	IsDir = True
	
	n_nodes = G.GetNodes()
	n_edges = G.GetEdges()
################################################################################## RANDOM GRAPH

	print (str(net)+" "+str(i)+" - Gerando grafo aleatório com "+str(n_nodes)+" vertices e "+str(n_edges)+" arestas...")
	connected = False
	Rnd = snap.TRnd()
	while not connected:
		print (str(net)+" "+str(i)+" - Testando se grafo aleatório é conectado...")		
		Gnm = snap.GenRndGnm(snap.PNGraph, n_nodes, n_edges, IsDir, Rnd) 			# Cria um grafo aleatório com as mesmas dimensões do original (nodes,edges)
		connected = snap.IsConnected(Gnm)
	print (str(net)+" "+str(i)+" - Grafo conectado... OK")
	
################################################################################### Coef Clust

	print (str(net)+" "+str(i)+" - Calculando o coeficiente de clustering do grafo...")
	coef_clust_G = snap.GetClustCf(G, -1)																				# Calcula o coeficiente de clustering
	print (str(net)+" "+str(i)+" - Calculando a coeficiente de clustering do grafo aleatório...")
	coef_clust_Gnm = snap.GetClustCf(Gnm, -1)																			# Calcula o coeficiente de clustering do grafo aleatório

################################################################################## AVERAGE SHORTEST PATH LENGHT

	print (str(net)+" "+str(i)+" - Calculando média dos menores caminhos mínimos do grafo...")	
	t_spl_G = 0.0																				# Somatório dos caminhos mínimos = total do somatório dos caminhos mínimos de cada vértice
	n_paths_G = 0																				# Contador para quantidade de caminhos mínimos
	for node in G.Nodes():
		NIdToDistH = snap.TIntH()
		node_spl = snap.GetShortPath(G, node.GetId(), NIdToDistH, IsDir)
		path = 0
		for item in NIdToDistH:
#			print node.GetId(),item,NIdToDistH[item]
			path +=1
			t_spl_G += NIdToDistH[item]
		n_paths_G += path-1
#		print
#		print ego,node.GetId(),t_spl_G,n_paths_G,path
#	print
	avg_spl_G = t_spl_G/float(n_paths_G)												# Calcula a média dos caminhos mínimos para todo o grafo considerando apenas caminhos existentes.
	avg_spl_G_all = t_spl_G/float(n_nodes*(n_nodes-1))								# Calcula a média dos caminhos mínimos para todo o grafo.

#	labels = snap.TIntStrH()
#	for NI in G.Nodes():
#		labels[NI.GetId()] = str(NI.GetId())
#	snap.DrawGViz(G, snap.gvlDot, "/home/amaury/"+str(ego)+"_G.png", " ", labels)
################################################################################## AVERAGE SHORTEST PATH LENGHT RANDOM GRAPH

	print (str(net)+" "+str(i)+" - Calculando média dos menores caminhos mínimos do grafo aletório...")	
	t_spl_Gnm = 0.0																			# Somatório dos caminhos mínimos = total do somatório dos caminhos mínimos de cada vértice
	n_paths_Gnm = 0																			# Contador para quantidade de caminhos mínimos
	for node in Gnm.Nodes():
		NIdToDistH = snap.TIntH()
		node_spl = snap.GetShortPath(Gnm, node.GetId(), NIdToDistH, IsDir)
		path = 0
		for item in NIdToDistH:
#			print node.GetId(),item,NIdToDistH[item]
			path +=1
			t_spl_Gnm += NIdToDistH[item]
		n_paths_Gnm += path-1
#		print
#		print ego, node.GetId(),t_spl_Gnm,n_paths_Gnm,path
#	print
	avg_spl_Gnm = t_spl_Gnm/float(n_paths_Gnm)										# Calcula a média dos caminhos mínimos para todo o grafo considerando apenas caminhos existentes.
	avg_spl_Gnm_all = t_spl_Gnm/float(n_nodes*(n_nodes-1))						# Calcula a média dos caminhos mínimos para todo o grafo = (N*(N-1)) nodes.

#	labels = snap.TIntStrH()
#	for NI in Gnm.Nodes():
#		labels[NI.GetId()] = str(NI.GetId())
#	snap.DrawGViz(Gnm, snap.gvlDot, "/home/amaury/"+str(ego)+"_Gnm.png", " ", labels)
	
#	print ("Ego / Coef Clust: Graph / Random Graph")
#	print ego,coef_clust_G,coef_clust_Gnm
#	print ("ASPL Exists Path: Graph / Random Graph")
#	print ego,avg_spl_G, avg_spl_Gnm
#	print ("EGO / ASPL Total Paths: Graph / Random Graph")
#	print avg_spl_G_all, avg_spl_Gnm_all
#	print "##############################################"
#	print
################################################################################### S METRIC
#
	if coef_clust_Gnm == 0:
		GAMMA = 0
	else:		
		GAMMA = float(coef_clust_G)/float(coef_clust_Gnm)										# Numerador da métrica S
	
	LAMBDA_paths_exists = float(avg_spl_G)/float(avg_spl_Gnm)								# Denominador da métrica S com todos os caminhos existentes (só considera caminhos que existem)
	LAMBDA_all_paths = float(avg_spl_G_all)/float(avg_spl_Gnm_all)							# Denominador da métrica S com todos os caminhos possiveis (N*(N-1)) nodes
	
#
	S1 = float(GAMMA)/float(LAMBDA_paths_exists)												# Métrica S de acordo com o artigo que o Prof. Thierson enviou
	S2 = float(GAMMA)/float(LAMBDA_all_paths)													# Métrica S de acordo com o artigo que o Prof. Thierson enviou
	return coef_clust_G, coef_clust_Gnm, avg_spl_G, avg_spl_Gnm, avg_spl_G_all, avg_spl_Gnm_all, S1, S2

######################################################################################################################################################################
#
# Preparar os dados  
#
######################################################################################################################################################################
def prepare(net,out_file,egos_set,current_set):
	i=0																											# Contador do ego
	for ego in egos_set:
		i+=1
		if ego in egos_saved:
			print (str(net)+" "+str(i)+" - Métrica já calculada para o ego: "+str(ego))		
		else:	
			dataset = {}																						# Salvar Arquivos no Formato Json - linha por linha
			source = str(data_dir)+str(net)+"/graphs_with_ego/"+str(ego)+".edge_list"
			if not os.path.isfile(source):																# Verifica se diretório existe	
				print (str(net)+" "+str(i)+" - Impossível localizar arquivo com lista de arestas: "+str(source))
			else:
				G = snap.LoadEdgeList(snap.PNGraph, source, 0, 1)									# Carrega o grafo da camada i - Direcionado e Não Ponderado
				coef_clust_G, coef_clust_Gnm, avg_spl_G, avg_spl_Gnm, avg_spl_G_all, avg_spl_Gnm_all, S1, S2 = calc_metric(net,i,ego,G) # Calcula Métrica
				dataset[ego] = {"coef_clust_G":coef_clust_G,"coef_clust_Gnm":coef_clust_Gnm,"avg_spl_G_paths_exists":avg_spl_G,"avg_spl_Gnm_paths_exists":avg_spl_Gnm,"avg_spl_G_all_paths":avg_spl_G_all,"avg_spl_Gnm_all_paths":avg_spl_Gnm_all,"S_path_exists":S1,"S_all_paths":S2}			
				print				
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
	print" Verificação de Small World Usando Biblioteca SNAP"
	print"																											"
	print"#################################################################################"
	print
	print
	print"  1 - Follow"
#	print"  9 - Follwowers"
#	print"  2 - Retweets"
#	print"  3 - Likes"
#	print"  4 - Mentions"
	
#	print " "
#	print"  5 - Co-Follow"
#	print" 10 - Co-Followers"				
#	print"  6 - Co-Retweets"
#	print"  7 - Co-Likes"
#	print"  8 - Co-Mentions"
			
	print
	op = int(raw_input("Escolha uma opção acima: "))
	
	if op != 1:
		print ("Opção inválida... Só considera rede Follow por enquanto.")
		sys.exit()
			
	print("\n###########################################################\n")
	print"  1 - set 1 -->   1 - 100"
	print"  2 - set 2 --> 101 - 200"
	print"  3 - set 3 --> 201 - 300"
	print"  4 - set 4 --> 301 - 400"
	print"  5 - set 5 --> 401 - 500"
			
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 not in (1,2,3,4,5):
		print ("Opção inválida... Só existem 5 conjuntos possíveis.")
		sys.exit()
		
	if op2 == 1:
		egos_set = egos_sets["set1"]
		current_set = "set1"
	if op2 == 2:
		egos_set = egos_sets["set2"]
		current_set = "set2"
	if op2 == 3:
		egos_set = egos_sets["set3"]
		current_set = "set3"
	if op2 == 4:
		egos_set = egos_sets["set4"]
		current_set = "set4"
	if op2 == 5:
		egos_set = egos_sets["set5"]
		current_set = "set5"
	print("\n###########################################################")
	
	net = "n"+str(op)
	
	if os.path.exists(str(output_dir)+str(net)+".json"):
		print ("Arquivo de destino já existe! "+str(output_dir)+str(net)+".json - Fazendo leitura do arquivo...\n")
		out_file_total = open(str(output_dir)+str(net)+".json",'r')
		for line in out_file_total:
			data_saved = json.loads(line)
			for k,v in data_saved.iteritems():
				k = long(k)
				if not k in egos_saved:
					egos_saved[k] = k														#lê o arquivo e armazena uma tabela hash com o id dos egos já calculados

	if os.path.exists(str(output_dir)+str(net)+"_"+str(current_set)+".json"):
		print ("Arquivo de destino já existe! "+str(output_dir)+str(net)+"_"+str(current_set)+".json - Fazendo leitura do arquivo...\n")
		out_file = open(str(output_dir)+str(net)+"_"+str(current_set)+".json",'a+')
		for line in out_file:
			data_saved = json.loads(line)
			for k,v in data_saved.iteritems():
				k = long(k)
				if not k in egos_saved:
					egos_saved[k] = k														#lê o arquivo e armazena uma tabela hash com o id dos egos já calculados
	else:
		out_file = open(str(output_dir)+str(net)+"_"+str(current_set)+".json",'a+') # Se arquivo não existe então apenas abre o arquivo

	prepare(net,out_file,egos_set,current_set)													# Prepara os dados para cálculo e armazenamento dos dados
		
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
output_dir = "/home/amaury/Dropbox/net_structure_hashmap/multilayer/graphs_with_ego/unweighted_directed/json/small_world_snap/"	# Pegar a lista com os ids dos egos
create_dir(output_dir)																					# Cria diretótio para salvar arquivos.	

metric = "small_world"
egos_saved = {}

egos_set_file = "/home/amaury/Dropbox/egos_in_five_sets.json"

f = open(egos_set_file, "r")
egos_sets = json.load(f)

	#Executa o método main
if __name__ == "__main__": main()