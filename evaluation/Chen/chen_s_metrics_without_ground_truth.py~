# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import subprocess



reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular métricas usando o software desenvolvido por Chen:
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
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(communities,output,singletons,net,graphs,uw,ud):
	
	communities = communities+singletons+"/"+net+"/"
	output = output+singletons+"/"
	if not os.path.exists(output):
		os.makedirs(output)
	print	
	print("######################################################################")
	print ("Os arquivos serão armazenados em: "+str(output))
	print("######################################################################")

	if os.path.isfile(str(output)+str(net)+".json"):
		print ("Arquivo de destino já existe: "+str(output)+str(net)+".json")

	else:			
		result={}
		for threshold in range(51):	#Parâmetro do algoritmo de detecção
			threshold+=1
			i=0 		#Ponteiro para o ego

			if not os.path.isdir(str(communities)+str(threshold)+"/"):
				print ("Diretório com as comunidades não encontrado: "+str(communities)+str(threshold))

			else:	
				print("######################################################################")
				_result = {}					
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
							execute = subprocess.Popen(["mpirun","-np","4","/home/amaury/algoritmos/Metricas/ParallelComMetric-master/src/mpimetric","0",str(communities)+str(threshold)+"/"+str(file),str(graphs)+str(ego_id)+".edge_list",str(uw),str(ud)], stdout=subprocess.PIPE)
							
							value = execute.communicate()[0]
							b = value.split('\n')							
							t = b[0].split('\t')
							a = b[1].split('\t')

							print ("Metricas para a rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego("+str(i)+"): "+str(file)+" - "+str(a))
							
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
				_result['modularity'] = modularity
				_result['modularity_density'] = modularity_density
				_result['intra_edges'] = intra_edges
				_result['intra_density'] = intra_density
				_result['contraction'] = contraction
				_result['inter_edges'] = inter_edges
				_result['expansion'] = expansion
				_result['conductance'] = conductance														
				result[threshold] = _result


		if len(result) > 0:
			with open(str(output)+str(net)+".json", 'w') as f:
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
	communities1 = "/home/amaury/communities/graphs_with_ego/"+str(alg)+"/"
	communities2 = "/home/amaury/communities/graphs_without_ego/"+str(alg)+"/" 
	output1 = "/home/amaury/Dropbox/Chen_software_results/without_ground_truth/graphs_with_ego/"+str(alg)+"/"
	output2 = "/home/amaury/Dropbox/Chen_software_results/without_ground_truth/graphs_without_ego/"+str(alg)+"/"

	for i in range(10):								# Para cada rede-ego gerada
		i+=1
		if i == 1 or i == 9:
			uw=1											# Rede não ponderada - weighted
		else:
			uw=0
		if i in (5,6,7,8,10):
			ud=1											# Rede não direcionada - directed
		else:
			ud=0	 
		net = "n"+str(i)
		graphs1 = "/home/amaury/graphs/"+str(net)+"/graph_with_ego/"
		graphs2 = "/home/amaury/graphs/"+str(net)+"/graph_without_ego/"
		print

		print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))
		calculate_alg(communities1,output1,singletons,net,graphs1,uw,ud)
		print
		print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - SEM o ego - Algoritmo: "+str(alg))

		calculate_alg(communities2,output2,singletons,net,graphs2,uw,ud)

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

######################################################################################################################
if __name__ == "__main__": main()
