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
# Realiza as configurações necessárias para os dados do METRICA
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
def calculate_alg(communities,output,singletons,net,ground_truth,g_type):
	
	communities = communities+singletons+"/"+net+"/"
	ground_truth = ground_truth+singletons+"/"
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
				VI = []
				NMI = []
				F_measure = []
				NVD = []
				RI = []
				ARI = []
				JI = []																				# Armazenar os indices de cada ego e salvar depois em uma linha para cada threshold do arquivo result.json
				for file in os.listdir(str(communities)+str(threshold)+"/"):

					i+=1

					if not os.path.isfile(str(ground_truth)+str(file)):
						print ("ERROR - EGO: "+str(i)+" - Arquivo de ground truth não encontrado:" +(str(ground_truth)+str(file)))

					else:	
						try:
							execute = subprocess.Popen(["mpirun","-np","1","/home/amaury/algoritmos/Metricas/ParallelComMetric-master/src/mpimetric","1",str(ground_truth)+str(file),str(communities)+str(threshold)+"/"+str(file)], stdout=subprocess.PIPE)
							value = execute.communicate()[0]
							b = value.split('\n')							
							t = b[0].split('\t')
							a = b[1].split('\t')

							vi = float(a[1])
							nmi = float(a[2])
							f_measure = float(a[3])
							nvd = float(a[4])
							ri = float(a[5])
							ari = float(a[6])
							ji = float(a[7])

							print (str(g_type)+" - "+str(singletons)+" - Rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego("+str(i)+"): "+str(file)+" - "+str(a))

							VI.append(vi)
							NMI.append(nmi)
							F_measure.append(f_measure)
							NVD.append(nvd)
							RI.append(ri)
							ARI.append(ari)
							JI.append(ji)																																				

						except Exception as e:
							print e

				print("######################################################################")
				result['VI'] = VI
				result['NMI'] = NMI
				result['F_measure'] = F_measure
				result['NVD'] = NVD
				result['RI'] = RI
				result['ARI'] = ARI
				result['JI'] = JI					

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
	ground_truth = "/home/amaury/dataset/ground_truth/lists_users_TXT_hashmap/"
	communities1 = "/home/amaury/communities_hashmap/graphs_with_ego/"+str(alg)+"/"
	communities2 = "/home/amaury/communities_hashmap/graphs_without_ego/"+str(alg)+"/" 
	output1 = "/home/amaury/Dropbox/Chen_software_results_hashmap/with_ground_truth/graphs_with_ego/"+str(alg)+"/raw/"
	output2 = "/home/amaury/Dropbox/Chen_software_results_hashmap/with_ground_truth/graphs_without_ego/"+str(alg)+"/raw/"

	for i in range(10):								# Para cada rede-ego gerada
		i+=1
		net = "n"+str(i)

		print
		print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))
		g_type = "graphs_with_ego"
		calculate_alg(communities1,output1,singletons,net,ground_truth,g_type)

#		print
#		print ("Calculando métricas nas comunidades detectadas na rede: "+str(net)+" - SEM o ego - Algoritmo: "+str(alg))
#		g_type = "graphs_without_ego"
#		calculate_alg(communities2,output2,singletons,net,ground_truth,g_type)
	######################################################################################################################
		
	instructions(alg)									# Separar por métrica

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
source = "/home/amaury/Dropbox/Chen_software_results_hashmap/with_ground_truth/"
output = "/home/amaury/Dropbox/Chen_software_statistics_hashmap/with_ground_truth/"

######################################################################################################################
if __name__ == "__main__": main()
