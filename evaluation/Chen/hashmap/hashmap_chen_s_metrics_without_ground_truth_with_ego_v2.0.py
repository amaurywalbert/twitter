# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import subprocess


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular métricas usando o software desenvolvido por Chen: - Usando arquivos de entrada convertidos pelo HASHMAP
##					Versão 2 - Salva os dados no arquivo a cada threshold e não a cada rede como na versão anterior.
## 
##			SALVA ARQUIVOS NOS DIRETÒRIOS:
##				RAW: conforme calculado - 
##				SEPARATE BY METRICS
## 
##	Mingming Chen, Sisi Liu, and Boleslaw Szymanski, “Parallel Toolkit for Measuring the Quality of Network Community Structure”, 
##		The First European Network Intelligence Conference (ENIC), Wroclaw, Poland, September, 2014, pp. 22-29.
## 							
## # INPUT: Arquivos com as comunidades detectadas, rede e o ground truth
## 
## # OUTPUT:
##		- Com Ground-Truth:
##				total_running_time_pair_counting_metrics computation_time msg_passing_time
##				numProcs VI NMI F-measure NVD RI ARI JI	
##
##		- Sem Ground-Truth:
##				numProcs total_running_time 
##				numProcs modularity modularity_density #intra-edges intra-density contraction #inter-edges expansion conductance
##
######################################################################################################################################################################

######################################################################################################################################################################
#
# Prepara arquivos para ficar no mesmo formato  que a versão anterior - separados por METRICA
#
######################################################################################################################################################################
def prepare_data(data_dir,output_dir):
	
	if not os.path.isdir(data_dir):
		print ("\n\n\nDIRETÓRIO NÃO ENCONTRADO: "+str(data_dir)+"\n\n\n")
		
	else:	
		if not os.path.isdir(output_dir):
			os.makedirs(output_dir)			
			
		for file in os.listdir(data_dir):
			network = file.split(".json")														# pegar o nome do arquivo que indica o a rede analisada
			network = network[0]
	
			print ("\n##################################################")
			print ("Separando por métrica - Recuperando dados da rede "+str(network)+" - "+str(data_dir)+"\n")	
	
	
			with open(data_dir+file, 'r') as f:
				partial = {}
				for line in f:
					comm_data = json.loads(line)
					for k, v in comm_data.iteritems():											# Preparação para ler o arquivo JSON que tem o Formato  {"threshold": {metric": [values ---- {"5": {"VI": [0.542,...], "NMI": [0,214,0,36...],...}}
						threshold = k
						for _k,_v in v.iteritems():
							dictionary = {}
							values = _v
							metric = _k

							dictionary[threshold] = values
							print ("Salvando dados em: "+str(output_dir)+str(metric)+"/"+str(network)+".json")

							if not os.path.isdir(output_dir+str(metric)+"/"):
								os.makedirs(output_dir+str(metric)+"/")			
							
							with open(output_dir+str(metric)+"/"+str(network)+".json", "a") as f:
								f.write(json.dumps(dictionary, separators=(',', ':'))+"\n")

	print ("##################################################")	

######################################################################################################################################################################
#
# Realiza as configurações necessárias para separar os dados por métrica METRICA
#
######################################################################################################################################################################
def instructions(alg):																												
################################################################################################
	data_dir = str(source)+"graphs_with_ego/"+alg+"/raw/full/"
	output_dir = str(source)+"graphs_with_ego/"+alg+"/by_metrics/full/"

	prepare_data(data_dir,output_dir)

################################################################################################
	data_dir = str(source)+"graphs_with_ego/"+alg+"/raw/without_singletons/"
	output_dir = str(source)+"graphs_with_ego/"+alg+"/by_metrics/without_singletons/"

	prepare_data(data_dir,output_dir)

################################################################################################
#	data_dir = str(source)+"graphs_without_ego/"+alg+"/raw/full/"
#	output_dir = str(source)+"graphs_without_ego/"+alg+"/by_metrics/full/"
#
#	prepare_data(data_dir,output_dir)
#
################################################################################################
#	data_dir = str(source)+"graphs_without_ego/"+alg+"/raw/without_singletons/"
#	output_dir = str(source)+"graphs_without_ego/"+alg+"/by_metrics/without_singletons/"
#	
#	prepare_data(data_dir,output_dir)	
#
######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(communities,output,singletons,net,graphs,uw,ud,g_type):
	
	communities = communities+singletons+"/"+net+"/"
	output = output+singletons+"/"+net+"/"
	if not os.path.exists(output):
		os.makedirs(output)
	print	
	print("######################################################################")
	print ("Os arquivos serão armazenados em: "+str(output))
	print("######################################################################")

	for threshold in range(51):	#Parâmetro do algoritmo de detecção
		threshold+=1
		i=0 		#Ponteiro para o ego

		if not os.path.isdir(str(communities)+str(threshold)+"/"):
			print ("Diretório com as comunidades não encontrado: "+str(communities)+str(threshold))

		else:	
			if os.path.isfile(str(output)+str(threshold)+".json"):
				print ("Arquivo de destino já existe: "+str(output)+str(threshold)+".json")
			else:	
				print("######################################################################")
				result = {}					
				modularity = []
				modularity_density = []
				intra_edges = []
				intra_density = []
				contraction = []
				inter_edges = []
				expansion = []
				conductance = []

				for file in os.listdir(str(communities)+str(threshold)+"/"):
					ego_id = file.split(".txt")
					ego_id = long(ego_id[0])
					i+=1

					if not os.path.isfile(str(graphs)+str(ego_id)+".edge_list"):
						print ("ERROR - EGO: "+str(i)+" - Arquivo com lista de arestas não encontrado:" +str(graphs)+str(ego_id)+".edge_list")

					else:	
						try:
							execute = subprocess.Popen(["mpirun","-np","2","/home/amaury/algoritmos/Metricas/ParallelComMetric-master/src/mpimetric","0",str(communities)+str(threshold)+"/"+str(file),str(graphs)+str(ego_id)+".edge_list",str(uw),str(ud)], stdout=subprocess.PIPE)
							
							value = execute.communicate()[0]
							b = value.split('\n')							
							t = b[0].split('\t')
							a = b[1].split('\t')

							print (str(g_type)+" - "+str(singletons)+" - Rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego("+str(i)+"): "+str(file)+" - "+str(a))
							
							modularity.append(float(a[1]))
							modularity_density.append(float(a[2]))
							intra_edges.append(float(a[3]))
							intra_density.append(float(a[4]))
							contraction.append(float(a[5]))
							inter_edges.append(float(a[6]))
							expansion.append(float(a[7]))
							conductance.append(float(a[8]))

						except Exception as e:
							print e

				print("######################################################################")
				result['modularity'] = modularity
				result['modularity_density'] = modularity_density
				result['intra_edges'] = intra_edges
				result['intra_density'] = intra_density
				result['contraction'] = contraction
				result['inter_edges'] = inter_edges
				result['expansion'] = expansion
				result['conductance'] = conductance	


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
	print" 			Avaliação de Comunidades - Chen's Software										"
	print"																											"
	print"#################################################################################"
	print
	print"Realizar o cálculo usando Singletons?"
	print 
	print" 01 - SIM - full"
	print" 02 - NÃO"
	print
	op = int(raw_input("Escolha uma opção acima: "))
	if op == 01:
		singletons = "full"
	elif op == 02:
		singletons = "without_singletons"
	else:
		singletons = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
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
	print ("Opção escolhida: "+str(singletons)+" - "+str(alg))
	print ("Aguarde...")
	time.sleep(5)
	######################################################################################################################
	#####Alterar as linhas para Dropbox quando executado em ambiente de produção
	communities1 = "/home/amaury/communities_hashmap/graphs_with_ego/"+str(alg)+"/"
	communities2 = "/home/amaury/communities_hashmap/graphs_without_ego/"+str(alg)+"/" 
	output1 = "/home/amaury/Dropbox/Chen_software_results_hashmap/without_ground_truth/graphs_with_ego/"+str(alg)+"/raw/"
	output2 = "/home/amaury/Dropbox/Chen_software_results_hashmap/without_ground_truth/graphs_without_ego/"+str(alg)+"/raw/"

	for i in range(10):								# Para cada rede-ego gerada
		i+=1
		if i == 1 or i == 9:
			uw=1											# Rede não ponderada - unweighted
		else:
			uw=0
		if i in (5,6,7,8,10):
			ud=1											# Rede não direcionada - undirected
		else:
			ud=0	 
		net = "n"+str(i)
		graphs1 = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_with_ego/"
		graphs2 = "/home/amaury/graphs_hashmap/"+str(net)+"/graphs_without_ego/"

		print
		print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))
		g_type = "graphs_with_ego"	
		calculate_alg(communities1,output1,singletons,net,graphs1,uw,ud,g_type)

#		print
#		print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - SEM o ego - Algoritmo: "+str(alg))
#		g_type = "graphs_without_ego"	
#		calculate_alg(communities2,output2,singletons,net,graphs2,uw,ud,g_type)
	
	######################################################################################################################
		
	instructions(alg)									# Separa por Métricas...

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
source = "/home/amaury/Dropbox/Chen_software_results_hashmap/without_ground_truth/"
output = "/home/amaury/Dropbox/Chen_software_statistics_hashmap/without_ground_truth/"
######################################################################################################################
if __name__ == "__main__": main()
