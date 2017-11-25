# -*- coding: latin1 -*-
################################################################################################
import snap,datetime, sys, time, json, os, os.path, shutil, time, struct, random
import metrics


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular métricas principais métricas para avaliação sem ground truth de acordo com
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
# Prepara arquivos para ficar no mesmo formato  que a versão anterior - separados por METRICA
#
######################################################################################################################################################################
def by_metrics(alg,g_type,singletons):
	
	data_dir = str(output)+"raw/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"
	
	if not os.path.isdir(data_dir):
		print ("\n\n\nDIRETÓRIO NÃO ENCONTRADO: "+str(data_dir)+"\n\n\n")
		
	else:
		for net in os.listdir(data_dir):
			if os.path.isdir(data_dir+net):
				print ("\n##################################################")
				print ("Separando por métrica - Recuperando dados da rede "+str(net)+" - "+str(data_dir)+"\n")
			
				for file in os.listdir(data_dir+net):	
					threshold = file.split(".json")											# pegar o nome do arquivo que indica o a rede analisada
					threshold = threshold[0]
				
					with open(data_dir+net+"/"+file, 'r') as f:
						data = json.load(f)
						for k, v in data.iteritems():											# Preparação para ler o arquivo JSON que tem o Formato  {metric": [values ---- {"VI": [0.542,...], "NMI": [0,214,0,36...],...}
							dictionary = {}
							values = v
							metric = k

							dictionary[threshold] = values

							if os.path.exists(output+"by_metrics/"+str(metric)+"/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+".json"):
								print ("Arquivo de destino já existe: "+output+"by_metrics/"+str(metric)+"/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+".json")
							else:
								print ("Salvando dados em: "+str(output)+"by_metrics/"+str(metric)+"/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+".json")
	
								if not os.path.isdir(output+"by_metrics/"+str(metric)+"/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"):
									os.makedirs(output+"by_metrics/"+str(metric)+"/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/")			
								
								with open(output+"by_metrics/"+str(metric)+"/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"+str(net)+".json", "a+") as f:
									f.write(json.dumps(dictionary, separators=(',', ':'))+"\n")

	print ("##################################################")
		
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
def calculate_alg(communities,output,singletons,net,graphs,uw,ud,g_type,alg):
	
	communities = communities+singletons+"/"+net+"/"

	if not os.path.exists(communities):
		print ("Diretório com as comunidades não encontrado: "+str(communities)+"\n")

	else:
			
		output = output+singletons+"/"+net+"/"
		if not os.path.exists(output):
			os.makedirs(output)
		print	
		print("######################################################################")
		print ("Os arquivos serão armazenados em: "+str(output))
		print("######################################################################")

		for threshold in os.listdir(communities):
			if not os.path.isdir(str(communities)+str(threshold)+"/"):
				print ("Threshold para a rede "+str(net)+" não encontrado: "+str(threshold))

			else:	
				if os.path.isfile(str(output)+str(threshold)+".json"):
					print ("Arquivo de destino já existe: "+str(output)+str(threshold)+".json")
					
				else:	
					print("######################################################################")
					result = {}		
							
					separability = []
					density = []
					cohesiveness = []
					expansion = []
					
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
									
									avg_separability,avg_density,avg_cohesiveness,avg_expansion  = metrics.calc_metrics(communities_dict,G,ud)			# Calcular as métricas
									separability.append(avg_separability['media'])  									# Salvar Separability
									density.append(avg_density['media'])  													# Salvar Density
									cohesiveness.append(avg_cohesiveness['media'])  									# Salvar Cohesiveness
									expansion.append(avg_expansion['media'])												# Salvar Expansion
										
									print separability[i-1],density[i-1],cohesiveness[i-1], expansion[i-1]
									print

					print("######################################################################")
					result['separability'] = separability
					result['density'] = density
					result['cohesiveness'] = cohesiveness
					result['expansion'] = expansion		

					with open(str(output)+str(threshold)+".json", 'w') as f:
						f.write(json.dumps(result))

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
	print"  3 - Mentions"
	
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
	print
	print ("Opção escolhida: "+str(net)+" - "+str(alg))
	print ("Aguarde...")
	
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

	communities = "/home/amaury/communities_hashmap/"+str(g_type1)+"/"+str(alg)+"/" 
	output_raw = str(output)+"raw/"+str(g_type1)+"/"+str(alg)+"/"
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type1)+"/"

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))

	calculate_alg(communities,output_raw,singletons1,net,graphs,uw,ud,g_type1,alg)
	
######################################################################################################################
######################################################################################################################

	communities = "/home/amaury/communities_hashmap/"+str(g_type2)+"/"+str(alg)+"/" 
	output_raw = str(output)+"raw/"+str(g_type2)+"/"+str(alg)+"/"
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type2)+"/"

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))

	calculate_alg(communities,output_raw,singletons2,net,graphs,uw,ud,g_type2,alg)
	
#######################################################################################################################
#######################################################################################################################

	communities = "/home/amaury/communities_hashmap/"+str(g_type3)+"/"+str(alg)+"/" 
	output_raw = str(output)+"raw/"+str(g_type3)+"/"+str(alg)+"/"
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type3)+"/"

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))

	calculate_alg(communities,output_raw,singletons3,net,graphs,uw,ud,g_type3,alg)
	
#######################################################################################################################
#######################################################################################################################

	communities = "/home/amaury/communities_hashmap/"+str(g_type4)+"/"+str(alg)+"/" 
	output_raw = str(output)+"raw/"+str(g_type4)+"/"+str(alg)+"/"
	graphs = "/home/amaury/graphs_hashmap/"+str(net)+"/"+str(g_type4)+"/"

	print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))

	calculate_alg(communities,output_raw,singletons4,net,graphs,uw,ud,g_type4,alg)
	
######################################################################################################################		

#	 Separa por Métricas...

	by_metrics(alg,g_type1,singletons1)
	by_metrics(alg,g_type2,singletons2)
	by_metrics(alg,g_type3,singletons3)
	by_metrics(alg,g_type4,singletons4)

	######################################################################################################################

	print("######################################################################")
	print
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")

	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

output = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/"

######################################################################################################################
if __name__ == "__main__": main()
