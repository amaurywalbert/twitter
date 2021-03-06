# -*- coding: latin1 -*-
################################################################################################
import snap,datetime, sys, time, json, os, os.path, time
import calc


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular e plotar a quantidade e tamanho das comunidades detectadas.
##		Status - Versão 2 - Não carrega o grafo novamente (lê de arquivo net struct)- Adicionar o número de singletons, não singletons e tamanho médio de sobreposição. (número médio de comunidades que um vértice pertence)
## 	Status - Versão 3 - Adicionar informação sobre cobertura do algoritmo - se ele considera todos so vértices ou deixa algum sem rótulo
##		Status - Versão 4 - Calcula dados para infomap sem peso
## 							
## # INPUT: Comunidades Detectadas
## 
## # OUTPUT:
##			Gráficos com os resultados
######################################################################################################################################################################

		
######################################################################################################################################################################
#
# Recebe arquivo e devolve dicionário com as comunidades
#
######################################################################################################################################################################
def prepare_communities(community_file,n_nodes):
	i=0

	communities = {}														# Dicionário com uma chave (id da community): e uma lista de ids dos membros da comunidade
	alters_set = set()
	size = []																# Lista com os tamanhos das communidades
	size_norm = []															# Lista com os tamanhos das communidades normalizada pelo número de vértices da rede-ego
	greater_comm_norm = 0												# Tamanho da maior comunidade normalizado pelo conjunto de vértices do grafo
	n_singletons = 0														# Número de Singletons (comunidades formada por apenas um vértice) 
	n_non_singletons = 0													# Número de Não Singletons
	greater_comm = 0														# Tamanho da maior comunidade
	smaller_comm = "inf"													# Tamanho da menor comunidade

	for line in community_file:
		i+=1
		key="com"+str(i)													# Chave para o dicionário comm - um identificador "comm1"
		comm = []															# Lista para armazenar as os membros da comunidade i
		a = line.split(' ')
		for item in a:
			if item != "\n":
				comm.append(long(item))
				alters_set.add(long(item))

		if len(comm) > 1:
			n_non_singletons+=1
		elif len(comm) == 1:
			n_singletons+=1
		
		if len(comm) > greater_comm:										# Tamanho da maior comunidade
			greater_comm = len(comm)

		if len(comm) < smaller_comm:										# Tamanho da menor comunidade
			smaller_comm = len(comm)
			
			
		communities[key] = comm												# dicionário communities recebe a lista de ids dos membros das comunidades tendo como chave o valor key
		b = float(len(comm))/float(n_nodes)
		size.append(len(comm))
		size_norm.append(b)

	n_comm = len(communities)												# Quantidade de comunidades para o ego em questão
	greater_comm_norm = float(greater_comm)/float(n_nodes)
	
	if n_nodes > alters_set:	
		alters_ignored = n_nodes - len(alters_set)					# Número de alters que foram ignorados no processo de detecção e não receberam rótulos.
		alters_ignored_norm = float(alters_ignored)/float(n_nodes)
	else:
		alters_ignored = 0
		alters_ignored_norm = 0

	avg_size = calc.calcular_full(size)									# Somar o vetor com o tamanho das comunidades...
	avg_size_norm = calc.calcular(size_norm)							# Somar o vetor com o tamanho das comunidades normalizado...
			
	overlap = float(avg_size['soma'])/float(n_nodes)				# The overlap: the average number of communities to which each vertex belongs. This is the sum of the sizes of all communities (including singletons) divided by the number of vertices, n.
	
	return communities, n_comm, size, avg_size['media'],avg_size['desvio_padrao'], size_norm, avg_size_norm['media'], overlap, n_singletons, n_non_singletons, alters_ignored, alters_ignored_norm, greater_comm, greater_comm_norm, smaller_comm

######################################################################################################################################################################
#
# Criar diretórios
#
######################################################################################################################################################################
def create_dirs(out_dir):
	
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)	

######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(singletons,net,g_type,alg,thresholds):
	
	communities_dir = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/" 

	net_struct = "/home/amaury/Dropbox/net_structure_hashmap/snap/"+str(g_type)+"/"+str(net)+"/"     #Substituindo os dados dos grafos...
	
	
	out_dir = str(output_dir)+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"		
	
	if not os.path.exists(communities_dir):
		print ("Diretório com as comunidades não encontrado: "+str(communities_dir)+"\n")

	else:
		print("\n######################################################################")

		print communities_dir
		for threshold in thresholds:
			if not os.path.isdir(str(communities_dir)+str(threshold)+"/"):
				print ("Threshold para a rede "+str(net)+" não encontrado: "+str(threshold))

			else:
				print ("Threshold: "+str(threshold))
				create_dirs(out_dir)	

				if os.path.exists(str(out_dir)+str(threshold)+".json"):
					print ("Arquivo de destino já existe: "+str(out_dir)+str(threshold)+".json")
					
				else:	
					print("######################################################################")
							
					statistics = {}


					i=0 		#Ponteiro para o ego
					
					if not os.path.isfile(str(net_struct)+str(net)+"_nodes.json"):
						print ("ERROR - EGO: "+str(i)+" - Arquivo com informações da estrutura da rede não encontrado - NODES:" +str(net_struct)+str(net)+"_nodes.json")

					elif not os.path.isfile(str(net_struct)+str(net)+"_edges.json"):
						print ("ERROR - EGO: "+str(i)+" - Arquivo com informações da estrutura da rede não encontrado - EDGES:" +str(net_struct)+str(net)+"_nodes.json")
						
					else:
						with open(str(net_struct)+str(net)+"_nodes.json", 'r') as f:
							net_struct_nodes = json.load(f)
						with open(str(net_struct)+str(net)+"_edges.json", 'r') as g:	
							net_struct_edges = json.load(g)

						for file in os.listdir(str(communities_dir)+str(threshold)+"/"):
							if os.path.isfile(str(communities_dir)+str(threshold)+"/"+file):
								ego_id = file.split(".txt")
								ego_id = long(ego_id[0])
								i+=1
																								
								with open(str(communities_dir)+str(threshold)+"/"+file, 'r') as community_file:
								
									communities, n_comm, size, avg_size, std_size, size_norm, avg_size_norm, overlap, n_singletons, n_non_singletons, alters_ignored, alters_ignored_norm, greater_comm, greater_comm_norm, smaller_comm = prepare_communities(community_file,net_struct_nodes[str(ego_id)])		#Função para devolver um dicionário com as comunidades
									statistics[ego_id] = {'n_nodes':net_struct_nodes[str(ego_id)],'n_edges':net_struct_edges[str(ego_id)],'n_communities':n_comm,'size':size,'avg_size':avg_size, "std_size":std_size, 'size_norm':size_norm,'avg_size_norm':avg_size_norm,'overlap':overlap, 'n_singletons':n_singletons,'n_non_singletons':n_non_singletons,'alters_ignored':alters_ignored,'alters_ignored_norm':alters_ignored_norm,'greater_comm':greater_comm,'greater_comm_norm':greater_comm_norm,"smaller_comm":smaller_comm}							

						print g_type,singletons,alg,net
																		 
						print("######################################################################")
						print	

						with open(str(out_dir)+str(threshold)+".json", "w") as f:
							f.write(json.dumps(statistics))


#Impressão na tela dos dados salvos...					
#						with open(str(out_dir)+str(threshold)+".json", "r") as g:
#							_statistics = json.load(g)
#							for k,v in _statistics.iteritems():
#								print
#								print k,v
#								print
	print("######################################################################")		

######################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" 			Avaliação de Comunidades - Communities Statistics									"
	print"																											"
	print"#################################################################################"
	print
#######################################################################
#######################################################################
	print("######################################################################")	
	print
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print
	print"  1 - COPRA - Without Weight - K=10"
	print"  2 - COPRA - Without Weight - K=2"
	print"  4 - OSLOM - Without Weight - K=50"
	print"  5 - RAK - Without Weight"		
	print"  6 - INFOMAP - Partition - Without Weight"												
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
#
	if op2 == 1:
		alg = "copra_without_weight_k10"
		thresholds = [10]
	elif op2 == 2:
		alg = "copra_without_weight_k2"
		thresholds = [2]
	elif op2 == 4:
		alg = "oslom_without_weight_k50"
		thresholds = [50]
	elif op2 == 5:
		alg = "rak_without_weight"
		thresholds = [1]
	elif op2 == 6:
		alg = "infomap_without_weight"
		thresholds = [10]		
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print ("\n")
	print	

######################################################################################################################
	networks = ["n1","n2","n3","n4"]	
	for net in networks:
		g_type1 = "graphs_with_ego"
		g_type2 = "graphs_without_ego"

		singletons1 = "full"
		singletons2 = "without_singletons"
	
		print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type1)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
		calculate_alg(singletons1,net,g_type1,alg,thresholds)
	

#		print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons2))
#		calculate_alg(singletons2,net,g_type1,alg)
	

#		print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
#		calculate_alg(singletons1,net,g_type2,alg)


#		print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type4)+" - Algoritmo: "+str(alg)+" - "+str(singletons4))
#		calculate_alg(singletons2,net,g_type2,alg)
	

######################################################################################################################		

	print("######################################################################")
	print("\nScript finalizado!\n")
	print("######################################################################\n")

	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

output_dir = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/"

######################################################################################################################
if __name__ == "__main__": main()
