# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import subprocess



reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular NMI
##								
## # INPUT: Arquivos com as comunidades detectadas e o ground truth 
## # OUTPUT:
##		- Arquivos com os índices NMI
######################################################################################################################################################################

######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def nmi_alg(communities,output,singletons,net,ground_truth):
	
	communities = communities+singletons+"/"+net+"/"
	ground_truth = ground_truth+singletons+"/"
	output = output+singletons+"/"
	if not os.path.exists(output):
		os.makedirs(output)
	print	
	print("######################################################################")
	print ("Os arquivos serão armazenados em: "+str(output))
	print("######################################################################")
	if not os.path.isfile(str(output)+str(net)+".json"):
		result={}
		for threshold in range(51):	#Parâmetro do algoritmo
			threshold+=1
			i=0 		#Ponteiro para o ego
			if os.path.isdir(str(communities)+str(threshold)+"/"):
				print("######################################################################")
				score = []																				# Armazenar os indices de cada ego e salvar depois em uma linha para cada threshold do arquivo result.json
				for file in os.listdir(str(communities)+str(threshold)+"/"):
					i+=1
					if os.path.isfile(str(ground_truth)+str(file)):
						try:
							execute = subprocess.Popen(["/home/amaury/algoritmos/Metricas/mutual3/mutual", str(communities)+str(threshold)+"/"+str(file),str(ground_truth)+str(file)], stdout=subprocess.PIPE)
							value = execute.communicate()[0]
							a = value.split('\t')
							nmi = float(a[1])
							print ("NMI para a rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego: "+str(i)+": "+str(nmi))
							score.append(nmi)
						except Exception as e:
							print e	
					else:
						print ("ERROR - EGO: "+str(i)+" - Arquivo de ground truth não encontrado:" +(str(ground_truth)+str(file)))
				print("######################################################################")					
				result[threshold] = score						
			else:
				print ("Diretório com as comunidades não encontrado: "+str(communities)+str(threshold))
		if len(result) > 0:
			with open(str(output)+str(net)+".json", 'w') as f:
				f.write(json.dumps(result))						
	else:
		print ("Arquivo de destino já existe: "+str(output)+str(net)+".json")			
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
	print" Algoritmo para cálculo da métrica NMI 														"
	print"																											"
	print"#################################################################################"
	
	singletons = "full"
#######################################################################
#######################################################################
	print("######################################################################")	
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print 
	print" 01 - COPRA"
	print" 02 - OSLOM"
	print" 03 - GN - Partition"
	print" 04 - COPRA - Partition"
	print" 05 - Infomap - Partition"
	print" 06 - Infomap - Partition - Without Weight"
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
	elif op2 == 05:
		alg = "infomap"
	elif op2 == 06:
		alg = "infomap_without_weight"						
	else:
		alg = ""
		print("Algoritmo - Opção inválida! Saindo...")
		sys.exit()
	print
	######################################################################################################################
	#####Alterar as linhas para Dropbox quando executado em ambiente de produção
	ground_truth = "/home/amaury/dataset/ground_truth/lists_users_TXT_hashmap/"
	communities1 = "/home/amaury/communities_hashmap/graphs_with_ego/"+str(alg)+"/"
	communities2 = "/home/amaury/communities_hashmap/graphs_without_ego/"+str(alg)+"/" 
	output1 = "/home/amaury/Dropbox/evaluation_hashmap/with_ground_truth/nmi/graphs_with_ego/"+str(alg)+"/"
	output2 = "/home/amaury/Dropbox/evaluation_hashmap/with_ground_truth/nmi/graphs_without_ego/"+str(alg)+"/"

	for i in range(10):								# Para cada rede-ego gerada
		i+=1
		net = "n"+str(i)
		print
		print ("Calculando NMI nas comunidades detectadas na rede: "+str(net)+" - SEM o ego - Algoritmo: "+str(alg))
		nmi_alg(communities1,output1,singletons,net,ground_truth)
		print
		print ("Calculando NMI nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))
		nmi_alg(communities2,output2,singletons,net,ground_truth)
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
