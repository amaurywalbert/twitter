# -*- coding: latin1 -*-
################################################################################################
import snap,datetime, sys, time, json, os, os.path, shutil, time, struct, random
import metrics


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular métrica definida em abaixo para avaliação sem ground truth de acordo com
## 
##			SALVA ARQUIVOS NOS DIRETÒRIOS:
##				RAW: conforme calculado - 
##				SEPARATE BY METRICS
## 							
## # INPUT: Arquivos com as comunidades detectadas, rede e o ground truth
## 
## # OUTPUT:
##			Resultados separados por métrica
######################################################################################################################################################################

		
######################################################################################################################################################################
#
# Recebe arquivo e devolve dicionário com as comunidades
#
######################################################################################################################################################################
def prepare_communities(community_file):
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
		communities[key] = comm														# dicionário communities recebe a lista de ids das comunidades tendo como chave o valor key
	return communities
		
######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(singletons,net,uw,ud,g_type,alg,metric):
	
	communities = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/" 
	output = str(output_dir)+str(metric)+"/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+"/"
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type)+"/"
	
	if not os.path.exists(communities):
		print ("Diretório com as comunidades não encontrado: "+str(communities)+"\n")

	else:
		print	
		print("######################################################################")
		print ("Os arquivos serão armazenados em: "+str(output))
		print("######################################################################")

		for threshold in os.listdir(communities):
			if not os.path.isdir(str(communities)+str(threshold)+"/"):
				print ("Threshold para a rede "+str(net)+" não encontrado: "+str(threshold))

			else:	
				print ("Salvando dados em: "+str(output)+str(threshold)+".json")
				if not os.path.exists(output):
					os.makedirs(output)
				
				if os.path.exists(str(output)+str(threshold)+".json"):
					print ("Arquivo de destino já existe: "+str(output)+str(threshold)+".json")
					
				else:	
					print("######################################################################")
							
					result = []
					
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

									print(str(g_type)+" - "+str(alg)+" - "+str(singletons)+" - Rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego("+str(i)+"): "+str(file))
									
									communities_dict = prepare_communities(community_file)							#Função para devolver um dicionário com as comunidades							
									
									avg  = metrics.calc_metrics(communities_dict,G,ud,metric)		# Calcular as métricas
									result.append(avg['media'])  									# Salvar Métrica

									print metric,result[i-1]
									print

					print("######################################################################")	

					with open(str(output)+str(threshold)+".json", "w") as f:
						f.write(json.dumps(result, separators=(',', ':'))+"\n")

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
	print" 			Avaliação de Comunidades - Amaury's Software										"
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
	print" 01 - COPRA"
	print" 02 - OSLOM"
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
	if op2 == 01:
		alg = "copra"
	elif op2 == 02:
		alg = "oslom"	
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print
	print ("\n")
#######################################################################
#######################################################################	
	print"#################################################################################"
	print
	print"  1 - Separability"
	print"  2 - Density"		
	print"  3 - Cohesiveness"
	print"  4 - Expansion"		
	print
	op3 = int(raw_input("Escolha uma opção acima: "))

	if op3 == 1:
		metric = "separability"
	elif op3 == 2:
		metric = "density"
	elif op3 == 3:
		metric = "cohesiveness"
	elif op3 == 4:
		metric = "expansion"
	else:
		print("Opção inválida! Saindo...")
		sys.exit()
	print ("\n")

	print
	print ("Opção escolhida: "+str(net)+" - "+str(alg)+" - "+str(metric))
	print ("Aguarde...")
	time.sleep(5)
	
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
	
	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type1)+" - Algoritmo: "+str(alg)+" - "+str(singletons1))
	calculate_alg(singletons1,net,uw,ud,g_type1,alg,metric)
	

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type2)+" - Algoritmo: "+str(alg)+" - "+str(singletons2))
	calculate_alg(singletons2,net,uw,ud,g_type2,alg,metric)
	

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type3)+" - Algoritmo: "+str(alg)+" - "+str(singletons3))
	calculate_alg(singletons3,net,uw,ud,g_type3,alg,metric)


	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - "+str(g_type4)+" - Algoritmo: "+str(alg)+" - "+str(singletons4))
	calculate_alg(singletons4,net,uw,ud,g_type4,alg,metric)
	

######################################################################################################################		

	print("######################################################################")
	print("\nScript finalizado!\n")
	print("######################################################################\n")

	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

output_dir = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/"

######################################################################################################################
if __name__ == "__main__": main()
