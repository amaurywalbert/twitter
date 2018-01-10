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
## 
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
	size = []																# Lista com os tamanhos das communidades
	size_norm = []															# Lista com os tamanhos das communidades normalizada pelo número de vértices da rede-ego
	n_singletons = 0														# Número de Singletons (comunidades formada por apenas um vértice) 
	n_non_singletons = 0													# Número de Não Singletons

	for line in community_file:
		i+=1
		key="com"+str(i)													# Chave para o dicionário comm - um identificador "comm1"
		comm = []															# Lista para armazenar as os membros da comunidade i
		a = line.split(' ')
		for item in a:
			if item != "\n":
				comm.append(long(item))

		if len(comm) > 1:
			n_singletons+=1
		else:
			n_non_singletons+=1

		communities[key] = comm											# dicionário communities recebe a lista de ids dos membros das comunidades tendo como chave o valor key
		b = float(len(comm))/float(n_nodes)
		size.append(len(comm))
		size_norm.append(b)

	n_comm = len(communities)											# Quantidade de comunidades para o ego em questão

	avg_size = calc.calcular(size)										# Somar o vetor com o tamanho das comunidades...
	avg_size_norm = calc.calcular(size_norm)										# Somar o vetor com o tamanho das comunidades normalizado...
			
	overlap = float(avg_size['soma'])/float(n_nodes)				# The overlap: the average number of communities to which each vertex belongs. This is the sum of the sizes of all communities (including singletons) divided by the number of vertices, n.
	
	return communities, n_comm, size, avg_size['media'], size_norm, avg_size_norm['media'], overlap, n_singletons, n_non_singletons

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
def calculate_alg(singletons,net,ud,g_type,alg):
	
	communities_dir = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/" 

	net_struct = "/home/amaury/Dropbox/net_structure_hashmap/snap/"+str(g_type)+"/"+str(net)+"/"     #Substituindo os dados dos grafos...
	
	
	out_dir = str(output_dir)+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"		
	
	if not os.path.exists(communities_dir):
		print ("Diretório com as comunidades não encontrado: "+str(communities_dir)+"\n")

	else:
		print("\n######################################################################")

		for threshold in os.listdir(communities_dir):
			print communities_dir
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
								
									communities, n_comm, size, avg_size, size_norm, avg_size_norm, overlap, n_singletons, n_non_singletons = prepare_communities(community_file,net_struct_nodes[str(ego_id)])		#Função para devolver um dicionário com as comunidades
									statistics[ego_id] = {'n_nodes':net_struct_nodes[str(ego_id)],'n_edges':net_struct_edges[str(ego_id)],'n_communities':n_comm,'size':size,'avg_size':avg_size,'size_norm':size_norm,'avg_size_norm':avg_size_norm,'overlap':overlap, 'n_singletons':n_singletons,'n_non_singletons':n_non_singletons}							

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
	print
	print"  1 - Follow"
	print"  9 - Follwowers"
	print"  2 - Retweets"
	print"  3 - Likes"
	print"  4 - Mentions"
	
	print " "
	print"  5 - Co-Follow"
	print" 10 - Co-Followers"				
	print"  6 - Co-Retweets"
	print"  7 - Co-Likes"
	print"  8 - Co-Mentions"
			
	print
	op = int(raw_input("Escolha uma opção acima: "))

	if op in (5,6,7,8,10):																						# Testar se é um grafo direcionado ou não
		ud = True
	elif op in (1,2,3,4,9):
		ud = False 
	else:
		print("Opção inválida! Saindo...")
		sys.exit()

	
	print
	print ("\n")
######################################################################
	
	net = "n"+str(op)	

#######################################################################
#######################################################################
	print("######################################################################")	
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print 
	print" 01 - COPRA"
	print" 02 - OSLOM"
	print" 03 - GN"
	print" 04 - COPRA -Partition"
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
	if op2 == 01:
		alg = "copra"
	elif op2 == 02:
		alg = "oslom"	
	elif op2 == 03:
		alg = "gn"
	elif op2 == 04:
		alg = "copra_partition"		
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print
	print ("\n")
	
######################################################################################################################
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_without_ego"

	singletons1 = "full"
	singletons2 = "without_singletons"
	
######################################################################################################################
	os.system('clear')
	
	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type1)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
	calculate_alg(singletons1,net,ud,g_type1,alg)
	

#	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons2))
#	calculate_alg(singletons2,net,ud,g_type1,alg)
	

	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
	calculate_alg(singletons1,net,ud,g_type2,alg)


#	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type4)+" - Algoritmo: "+str(alg)+" - "+str(singletons4))
#	calculate_alg(singletons2,net,ud,g_type2,alg)
	

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
