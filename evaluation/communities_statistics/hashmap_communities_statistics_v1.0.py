# -*- coding: latin1 -*-
################################################################################################
import snap,datetime, sys, time, json, os, os.path, shutil, time, struct, random
#import metrics


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular e plotar a quantidade e tamanho das comunidades detectadas.
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
def prepare_communities(community_file,n_nodes,size):
	i=0
	communities = {}
	for line in community_file:
		i+=1
		key="com"+str(i)																# Chave para o dicionário comm
		comm = []																		# Lista para armazenar as comunidades			
		a = line.split(' ')
		for item in a:
			if item != "\n":
				comm.append(long(item))
		communities[key] = comm														# dicionário communities recebe a lista de ids dos membros das comunidades tendo como chave o valor key
		b = float(len(comm))/float(n_nodes)
		size.append(b)
	return communities

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
#	op3 = int(raw_input("Escolha um threshold para o algoritmo "+str(alg)+": "))
#	if op3 is not None:
#		threshold = op3
#	else:
#		threshold = ""
#		print("Opção inválida! Saindo...")
#		sys.exit()
#	print("######################################################################\n")	
	
	communities = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/" 
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type)+"/"
	
	out_dir = str(output_dir)+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"		
	
	if not os.path.exists(communities):
		print ("Diretório com as comunidades não encontrado: "+str(communities)+"\n")

	else:
		print("\n######################################################################")

		for threshold in os.listdir(communities):
			if not os.path.isdir(str(communities)+str(threshold)+"/"):
				print ("Threshold para a rede "+str(net)+" não encontrado: "+str(threshold))

			else:
				print ("Threshold: "+str(threshold))
				create_dirs(out_dir)

				if os.path.exists(str(out_dir)+str(threshold)+".json"):
					print ("Arquivo de destino já existe: "+str(threshold)+".json")
					
				else:	
					print("######################################################################")
							
					statistics = {}
					size = []
					lenght = []
					i=0 		#Ponteiro para o ego
					for file in os.listdir(str(communities)+str(threshold)+"/"):
						if os.path.isfile(str(communities)+str(threshold)+"/"+file):
							ego_id = file.split(".txt")
							ego_id = long(ego_id[0])
							i+=1
							if not os.path.isfile(str(graphs)+str(ego_id)+".edge_list"):
								print ("ERROR - EGO: "+str(i)+" - Arquivo com lista de arestas não encontrado:" +str(graphs)+str(ego_id)+".edge_list")

							else:

								with open(str(communities)+str(threshold)+"/"+file, 'r') as community_file:
									if ud is False:
										G = snap.LoadEdgeList(snap.PNGraph, str(graphs)+str(ego_id)+".edge_list", 0, 1)					   # load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
									else:
										G = snap.LoadEdgeList(snap.PUNGraph, str(graphs)+str(ego_id)+".edge_list", 0, 1)						# load from a text file - pode exigir um separador.: snap.LoadEdgeList(snap.PNGraph, file, 0, 1, '\t')
									
									n_nodes = (G.GetNodes())														# Numero de vértices
									communities_dict = prepare_communities(community_file,n_nodes,size)							#Função para devolver um dicionário com as comunidades
									lenght.append(len(communities_dict))
									
					print size
					print len(size)
					print
					print lenght
					print len(lenght)
					print g_type,singletons,alg,net
					statistics = {'size':size,'lenght':lenght}													 
					print("######################################################################")
					print	

					with open(str(out_dir)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(statistics, separators=(',', ':'))+"\n")

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
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
	if op2 == 01:
		alg = "copra"
	elif op2 == 02:
		alg = "oslom"	
	elif op2 == 03:
		alg = "gn"
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print
	print ("\n")
	
######################################################################################################################
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_with_ego"
	g_type3 = "graphs_without_ego"
	g_type4 = "graphs_without_ego"
	
	singletons1 = "full"
	singletons2 = "without_singletons"
	singletons3 = "full"
	singletons4 = "without_singletons"
	
######################################################################################################################
	os.system('clear')
	
	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type1)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
	calculate_alg(singletons1,net,ud,g_type1,alg)
	

	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons2))
	calculate_alg(singletons2,net,ud,g_type2,alg)
	

	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type3)+" - Algoritmo: "+str(alg)+" - "+str(singletons3))
	calculate_alg(singletons3,net,ud,g_type3,alg)


	print ("\nCalculando statisticas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type4)+" - Algoritmo: "+str(alg)+" - "+str(singletons4))
	calculate_alg(singletons4,net,ud,g_type4,alg)
	

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
