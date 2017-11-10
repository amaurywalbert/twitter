# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Receber dataset e converter o longint dos usuários para int
##	
##								
## # INPUT: Arquivos com o ground_truth, rede-ego e communities em longint para cada ego
## 
## # OUTPUT: Arquivos de entrada convertidos para int
##
######################################################################################################################################################################


######################################################################################################################################################################
#
# ADD ground_truth and communitites ao hashmap
#
#		Adiciona o id do usuário como chave de um dicionário e vincula essa chave a um numero dado pela numero sequencial correspondente à aparição do usuário no arquivo. 
#
######################################################################################################################################################################
def add_hashmap(i,hashmap,f):		
	for line in f:
		alters = line.split(' ')
		for alter in alters:
			if alter != "\n" and alter != " ":
				i+=1
				hashmap[long(alter)] = i
	return (i,hashmap)	
######################################################################################################################################################################
#
# ADD egonet ao hashmap 
#
#		Para cada par de usuários representando cada terminal de uma aresta, adiciona o id do usuário como chave de um dicionário e vincula essa chave a um numero dado pela numero sequencial correspondente à aparição do usuário no arquivo.
#
######################################################################################################################################################################
def add_hashmap_egonet(i,hashmap,f):	
	for line in f:
		alters = line.split(' ')
		if alters[0] != "\n" and alters[0] != " ":
			i+=1
			hashmap[long(alters[0])] = i
		if alters[1] != "\n" and alters[1] != " ":
			i+=1	
			hashmap[long(alters[1])] = i
	return (i,hashmap)	

######################################################################################################################################################################
#
# SAVE ground truth and communities - hashmap 
#
#		Percorre o arquivo e verifica o valor vinculado a ele consultando o HashMAP. Escreve o novo valor no mesmo formato do arquivo de entrada.
#
######################################################################################################################################################################
def save_hashmap(i,hashmap,f,g,test):
	for line in f:
		alters = line.split(' ')
		for alter in alters:
			if alter != "\n" and alter != " ":
				g.write(str(hashmap[long(alter)])+" ")									# Escreve os ids das Listas separadas por espaço
				test.append(long(alter))
		g.write("\n")

######################################################################################################################################################################
#
# SAVE egonet - hashmap 
#
##		Percorre o arquivo e verifica o valor vinculado a ele consultando o HashMAP. Escreve o novo valor no mesmo formato do arquivo de entrada, mantendo o valor do peso da aresta inalterado, caso houver.
#
######################################################################################################################################################################
def save_hashmap_egonet(i,hashmap,f,g,test):
	for line in f:
		alters = line.split(' ')
		if alters[0] != "\n" and alters[0] != " " and alters[1] != "\n" and alters[1] != " ":			
			alters[0] = long(alters[0])
			alters[1] = long(alters[1])
			if len(alters) > 2:
				g.write(str(hashmap[alters[0]])+" "+str(hashmap[alters[1]])+" "+str(alters[2]))
			else:
			g.write(str(hashmap[alters[0]])+" "+str(hashmap[alters[1]]))

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
	print" 			Converte longint para int usando HashMap											"
	print"																											"
	print"#################################################################################"	
	j = 0
	for file in os.listdir(ground_truth_source+str("full/")):				# Iniciar o ego
		j+=1
		ego = file.split(".txt")
		ego = ego[0]
		hashmap = {}
		i=0
######################################################################################################################
################################################################## GROUND TRUTH
		for net_type in os.listdir(ground_truth_source):
			if net_type in("full","without_singletons"):
				if os.path.isdir(ground_truth_source+"/"+net_type):

					with open(ground_truth_source+net_type+"/"+file, 'r') as f:		# SOURCE - Para arquivos no diretório ground_truth/...
						i,hashmap = add_hashmap(i,hashmap,f)

################################################################## EGONETS
		nets = []
		for diretorio in os.listdir(egonet_source):
			if os.path.isdir(egonet_source+diretorio):
				nets.append(diretorio)
		
		for net in nets:
			for diretorio in os.listdir(egonet_source+net):
				if diretorio in ("graphs_with_ego","graphs_without_ego"):
					if os.path.isdir(egonet_source+net+"/"+diretorio):

						with open(egonet_source+net+"/"+diretorio+"/"+str(ego)+".edge_list", 'r') as f:		# SOURCE - Para arquivos no diretório ego/net/nx/graphs_with_ego/
							i,hashmap = add_hashmap_egonet(i,hashmap,f)

################################################################## COMMUNITIES
		for diretorio in os.listdir(communities_source):
			if diretorio in ("graphs_with_ego","graphs_without_ego"):
				if os.path.isdir(communities_source+diretorio):
					for alg in os.listdir(communities_source+diretorio):
						if os.path.isdir(communities_source+diretorio+"/"+alg):
							for net_type in os.listdir(communities_source+diretorio+"/"+alg):
								if net_type in("full","without_singletons"):
									if os.path.isdir(communities_source+diretorio+"/"+alg+"/"+net_type):
										for net in os.listdir(communities_source+diretorio+"/"+alg+"/"+net_type):
											if os.path.isdir(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net):
												for threshold in os.listdir(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net):
													if os.path.isdir(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold):
														if os.path.isfile(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold+"/"+file):

															with open(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold+"/"+file, 'r') as f:		# SOURCE - Para arquivos no communities_source/graphs_withX_ego/"alg"/"net_type"/"net"
																i,hashmap = add_hashmap(i,hashmap,f)

######################################################################################################################								
###################################################### SALVAR DADOS CONVERTIDOS
######################################################################################################################
		test = []				
######################################################################################################################
################################################################## GROUND TRUTH
		for net_type in os.listdir(ground_truth_source):
			if net_type in("full","without_singletons"):
				if os.path.isdir(ground_truth_source+"/"+net_type):

					with open(ground_truth_source+net_type+"/"+file, 'r') as f:		# SOURCE - Para arquivos no diretório ground_truth/...						

						if not os.path.exists(ground_truth_output+net_type+"/"):
							os.makedirs(ground_truth_output+net_type+"/")

						with open(ground_truth_output+net_type+"/"+file, 'w') as g:
							save_hashmap(i,hashmap,f,g,test)


################################################################## EGONETS
		for net in nets:
			for diretorio in os.listdir(egonet_source+net):
				if diretorio in ("graphs_with_ego","graphs_without_ego"):
					if os.path.isdir(egonet_source+net+"/"+diretorio):
						
						with open(egonet_source+net+"/"+diretorio+"/"+str(ego)+".edge_list", 'r') as f:		# SOURCE - Para arquivos no diretório ego/net/nx/graphs_with_ego/
							
							if not os.path.exists(egonet_output+net+"/"+diretorio+"/"):
								os.makedirs(egonet_output+net+"/"+diretorio+"/")

							with open(egonet_output+net+"/"+diretorio+"/"+str(ego)+".edge_list", 'w') as g:		# SOURCE - Para arquivos no diretório ego/net/nx/graphs_with_ego/													
								save_hashmap_egonet(i,hashmap,f,g,test)


################################################################## COMMUNITIES
		for diretorio in os.listdir(communities_source):
			if diretorio in ("graphs_with_ego","graphs_without_ego"):
				if os.path.isdir(communities_source+diretorio):
					for alg in os.listdir(communities_source+diretorio):
						if os.path.isdir(communities_source+diretorio+"/"+alg):
							for net_type in os.listdir(communities_source+diretorio+"/"+alg):
								if net_type in("full","without_singletons"):
									if os.path.isdir(communities_source+diretorio+"/"+alg+"/"+net_type):
										for net in os.listdir(communities_source+diretorio+"/"+alg+"/"+net_type):
											if os.path.isdir(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net):
												for threshold in os.listdir(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net):
													if os.path.isdir(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold):
														if os.path.isfile(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold+"/"+file):
															
															with open(communities_source+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold+"/"+file, 'r') as f:		# SOURCE - Para arquivos no communities_source/graphs_withX_ego/"alg"/"net_type"/"net"

																if not os.path.exists(communities_output+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold+"/"):
																	os.makedirs(communities_output+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold+"/")

																with open(communities_output+diretorio+"/"+alg+"/"+net_type+"/"+net+"/"+threshold+"/"+file, 'w') as g:
																	save_hashmap(i,hashmap,f,g,test)																
######################################################################################################################		

		print ("Convertendo arquivos do ego "+str(j)+": "+str(ego)) 						

######################################################################################################################

	print
	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")

	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################
ground_truth_source = "/home/amaury/dataset/ground_truth/lists_users_TXT/"
ground_truth_output = "/home/amaury/dataset/ground_truth/lists_users_TXT_hashmap/"

egonet_source = "/home/amaury/graphs/"
egonet_output = "/home/amaury/graphs_hashmap/"

communities_source = "/home/amaury/communities/"
communities_output = "/home/amaury/communities_hashmap/"

if os.path.exists(ground_truth_output):
	shutil.rmtree(ground_truth_output)
if os.path.exists(egonet_output):
	shutil.rmtree(egonet_output)	
if os.path.exists(communities_output):
	shutil.rmtree(communities_output)				
######################################################################################################################
if __name__ == "__main__": main()
