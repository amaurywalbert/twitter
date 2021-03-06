# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import calc, subprocess


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular métrica definida abaixo para avaliação sem ground truth - Usando a Algoritmo em Java desenvolvido pelo Chen - 
##									Modularity Density - https://github.com/chenmingming/ComQualityMetric - mais antigo - orientado pelo BoleslawS
##
##									ATENÇÃO - PARA O OSLOM, HÁ ELEMENTOS QUE NÃO FORAM ASSOCIADOS A NENHUMA COMUNIDADE, NEM MESMO SINGLETONS,
##												ESTÃO SENDO IGNORADOS... VER O QUE FAZER.
######################################################################################################################################################################

######################################################################################################################################################################
#
# Criar diretórios
#
######################################################################################################################################################################
def create_dirs(paths):
	for item in paths:
		if not os.path.exists(item):
			os.makedirs(item)	

######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(singletons,net,uw,ud,g_type,alg):
	
	communities = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/" 
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type)+"/"
	
	out_Q = str(output_dir)+"modularity/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"		
	out_NQ = str(output_dir)+"N_modularity/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"	
	out_Qds = str(output_dir)+"modularity_density/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_intra_edges = str(output_dir)+"intra_edges/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_intra_density = str(output_dir)+"intra_density/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_contraction = str(output_dir)+"contraction/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_inter_edges = str(output_dir)+"inter_edges/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_expansion = str(output_dir)+"expansion/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_conductance = str(output_dir)+"conductance/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	out_modularity_degree = str(output_dir)+"modularity_degree/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	
	_avg_time = []
	
	if not os.path.exists(communities):
		print ("Diretório com as comunidades não encontrado: "+str(communities)+"\n")

	else:
		print("\n######################################################################")

		for threshold in os.listdir(communities):
			if not os.path.isdir(str(communities)+str(threshold)+"/"):
				print ("Threshold para a rede "+str(net)+" não encontrado: "+str(threshold))

			else:
				partial_start = time.time()
				paths = [out_Q,out_NQ,out_Qds,out_intra_edges,out_intra_density,out_contraction,out_inter_edges,out_expansion,out_conductance,out_modularity_degree]
				create_dirs(paths)

				if os.path.exists(str(out_Q)+str(threshold)+".json") and os.path.exists(str(out_NQ)+str(threshold)+".json") and os.path.exists(str(out_Qds)+str(threshold)+".json") and os.path.exists(str(out_intra_edges)+str(threshold)+".json") and os.path.exists(str(out_intra_density)+str(threshold)+".json") and os.path.exists(str(out_contraction)+str(threshold)+".json") and os.path.exists(str(out_inter_edges)+str(threshold)+".json")  and os.path.exists(str(out_expansion)+str(threshold)+".json") and os.path.exists(str(out_conductance)+str(threshold)+".json") and os.path.exists(str(out_modularity_degree)+str(threshold)+".json"):
					print ("Arquivo de destino já existe: "+str(threshold)+".json")
					
				else:	
					print("######################################################################")
							
					Q = {}		
					NQ = {}	
					Qds = {}
					intra_edges = {}
					intra_density = {}
					contraction = {}
					inter_edges = {}
					expansion = {}
					conductance = {}
					modularity_degree = {}
					
					i=0 		#Ponteiro para o ego
					for file in os.listdir(str(communities)+str(threshold)+"/"):
						if os.path.isfile(str(communities)+str(threshold)+"/"+file):
							ego_id = file.split(".txt")
							ego_id = long(ego_id[0])
							i+=1

							if not os.path.isfile(str(graphs)+str(ego_id)+".edge_list"):
								print ("ERROR - EGO: "+str(i)+" - Arquivo com lista de arestas não encontrado:" +str(graphs)+str(ego_id)+".edge_list")

							else:
								community_file = str(communities)+str(threshold)+"/"+file
								graph_file = str(graphs)+str(ego_id)+".edge_list"

								print("Ego: "+str(i)+" - "+communities+threshold+"/"+file)
									
									

								if uw is False and ud is False:		# Para grafo Ponderado e Direcionado (n2,n3,n4)
									execute = subprocess.Popen(["java", "OverlappingCommunityQuality", str(graph_file),str(community_file)], stdout=subprocess.PIPE)

								elif uw is True and ud is False:		# Para grafo NÂO Ponderado e Direcionado (n1,n9)
									execute = subprocess.Popen(["java", "OverlappingCommunityQuality", str(graph_file),str(community_file),"isUnweighted"], stdout=subprocess.PIPE)

								elif uw is False and ud is True:		# Para grafo Ponderado e NÃO Direcionado (n5,n6,n7,n8,n10)
									execute = subprocess.Popen(["java", "OverlappingCommunityQuality", str(graph_file),str(community_file),"isUndirected"], stdout=subprocess.PIPE)								

								elif uw is True and ud is True:		# Para grafo NÃO Ponderado e NÃO Direcionado (não tem nenhum...)
									execute = subprocess.Popen(["java", "OverlappingCommunityQuality", str(graph_file),str(community_file),"isUnweighted","isUndirected"], stdout=subprocess.PIPE)

								resp = execute.communicate()[0]
								print resp
								value = resp.split(", ")
								for item in value:
									item = item.split(" = ")
									
									if item[0] == "Q":
										Q[ego_id] = float(item[1])
									elif item[0] == "NQ":
										NQ[ego_id] = float(item[1])
									elif item[0] == "Qds":
										Qds[ego_id] = float(item[1])
									elif item[0] == "intraEdges":
										intra_edges[ego_id] = float(item[1])
									elif item[0] == "intraDensity":
										intra_density[ego_id] = float(item[1])
									elif item[0] == "contraction":
										contraction[ego_id] = float(item[1])
									elif item[0] == "interEdges":
										inter_edges[ego_id] = float(item[1])
									elif item[0] == "expansion":
										expansion[ego_id] = float(item[1])
									elif item[0] == "conductance":
										conductance[ego_id] = float(item[1])
									elif item[0] == "modularity degree":
										modularity_degree[ego_id] = float(item[1])
										
					print("######################################################################")	

	
					with open(str(out_Q)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(Q))
						
					with open(str(out_NQ)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(NQ))

					with open(str(out_Qds)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(Qds))
											
					with open(str(out_intra_edges)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(intra_edges))

					with open(str(out_intra_density)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(intra_density))

					with open(str(out_contraction)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(contraction))

					with open(str(out_inter_edges)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(inter_edges))						

					with open(str(out_expansion)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(expansion))

					with open(str(out_conductance)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(conductance))

					with open(str(out_modularity_degree)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(modularity_degree))
				
				partial_end = time.time()
				partial_time_exec = partial_end - partial_start
				print ("\nTempo de execução para o threshold "+str(threshold)+": "+str(partial_time_exec)+"\n")
				_avg_time.append(partial_time_exec)
	avg_time = calc.calcular(_avg_time)
	print ("\nTempo de médio de execução em cada threshold: "+str(avg_time)+"\n")
	print("\n######################################################################\n")		

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
	print" 			Avaliação de Comunidades - Chen's Software - OVERLAPPING						"
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

	if op == 1 or op == 9:																						# Testar se é um grafo direcionado ou não
		uw = True
	else:
		uw = False
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
	print
	print"  1 - COPRA"
	print"  2 - OSLOM"
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		alg = "copra"
	elif op2 == 2:
		alg = "oslom"			
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()		
	print
	print ("\n")
#######################################################################
#######################################################################	

	print
	print ("Opção escolhida: "+str(net)+" - "+str(alg))
	print ("Aguarde...")
	time.sleep(3)
	
######################################################################################################################
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_without_ego"
	
	singletons1 = "full"
	singletons2 = "without_singletons"

	
######################################################################################################################
	os.system('clear')

	start = time.time()
	
	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type1)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
	calculate_alg(singletons1,net,uw,ud,g_type1,alg)
	

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
	calculate_alg(singletons1,net,uw,ud,g_type2,alg)

	end = time.time()
	time_exec = end - start
######################################################################################################################		

	print("######################################################################")
	print("\nScript finalizado! Tempo de execução: "+str(time_exec)+"\n")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

output_dir = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth_chen/"

######################################################################################################################
if __name__ == "__main__": main()
