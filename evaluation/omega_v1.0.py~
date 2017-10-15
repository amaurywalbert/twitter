# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time, struct, random
import omega_index

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Calcular Õmega Index
##								
## # INPUT: Arquivos com as comunidades detectadas e o ground truth 
## # OUTPUT:
##		- Arquivos com os índices Omega
######################################################################################################################################################################

######################################################################################################################################################################
#
# Formata entrada e envia para calculo do Omega Index
#
######################################################################################################################################################################
def omega_calc(communities_file, ground_truth_communities_file):

#communities = {
#   "com1": ["item1", "item2"],
#    "com2": ["item3", "item4"],
#    "com3": ["item5", "item6", "item9"],
#    "com4": ["item7", "item8"],
#    "com5": ["item9", "item10", "item4"],
#    "com6": ["item11", "item12"],
#    "com7": ["item13", "item14"]
#}

	with open(communities_file, 'r') as f:
		i=0
		communities = {}
		for line in f:
			i+=1
			key="com"+str(i)																#Chave para o dicionário comm
			comm = []																		#Lista para armazenar as comunidades			
			a = line.split(' ')
			for item in a:
				if item != "\n":
					comm.append(item)
			communities[key] = comm														#dicionário communities recebe a lista de ids das comunidades tendo como chave o valor key
	
	with open(ground_truth_communities_file, 'r') as f:
		i=0
		ground_truth_communities = {}
		for line in f:
			i+=1
			key="com"+str(i)																#Chave para o dicionário comm
			comm = []																		#Lista para armazenar as comunidades			
			a = line.split(' ')
			for item in a:
				if item != "\n":
					comm.append(item)
			ground_truth_communities[key] = comm									#dicionário communities recebe a lista de ids das comunidades tendo como chave o valor key				
					
	omega = omega_index.Omega(communities, ground_truth_communities)
	return omega


######################################################################################################################################################################
#
# Prepara apresentação dos resultados - OMEGA
#
######################################################################################################################################################################
def omega_alg(communities,output,singletons,net,ground_truth):
	
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
		for threshold in range(20):	#Parâmetro do algoritmo
			threshold+=1
			i=0 		#Ponteiro para o ego
			if os.path.isdir(str(communities)+str(threshold)+"/"):
				print("######################################################################")
				score = []																				# Armazenar os indices de cada ego e salvar depois em uma linha para cada threshold do arquivo result.json
				for file in os.listdir(str(communities)+str(threshold)+"/"):
					i+=1
					if os.path.isfile(str(ground_truth)+str(file)):
						try:
							omega = omega_calc(str(communities)+str(threshold)+"/"+str(file),str(ground_truth)+str(file))
							print ("Ômega Index para a rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego: "+str(i)+": "+str(omega.omega_score))
							score.append(omega)
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
	print" Algoritmo para cálculo da métrica Ômega Index												"
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
	print "Algoritmo utilizado na detecção das comunidades:"
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
	ground_truth = "/home/amaury/dataset/ground_truth/lists_users_TXT/"
	communities1 = "/home/amaury/communities/graphs_with_ego/"+str(alg)+"/"
	communities2 = "/home/amaury/communities/graphs_without_ego/"+str(alg)+"/" 
	output1 = "/home/amaury/Dropbox/evaluation/graphs_with_ego/"+str(alg)+"/omega/"
	output2 = "/home/amaury/Dropbox/evaluation/graphs_without_ego/"+str(alg)+"/omega/"

	for i in range(10):								# Para cada rede-ego gerada
		i+=1
		net = "n"+str(i)
		print
		print ("Calculando Ômega Index nas comunidades detectadas na rede: "+str(net)+" - SEM o ego - Algoritmo: "+str(alg))
		omega_alg(communities1,output1,singletons,net,ground_truth)
		print
		print ("Calculando Ômega Index nas comunidades detectadas na rede: "+str(net)+" - COM o ego - Algoritmo: "+str(alg))
		omega_alg(communities2,output2,singletons,net,ground_truth)
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