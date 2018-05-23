# -*- coding: latin1 -*-
################################################################################################
import snap,datetime, sys, time, json, os, os.path, shutil, time, struct, random
import subprocess
import networkx as nx
import matplotlib.pyplot as plt


reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - INFOMAP - http://www.mapequation.org/code.html
## 
## 							
## # INPUT: Grafos
## 
## # OUTPUT:
##			Communities
######################################################################################################################################################################

			
######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(output,net,uw,ud,g_type,alg,graphs):

	if not os.path.exists(graphs):
		print ("\nDiretório com grafos não encontrado: "+str(graphs)+"\n")
	else:					
		print	
		print("######################################################################")
		print ("Os arquivos serão armazenados em: "+str(output))
		print("######################################################################")
		if not os.path.exists(output):
			os.makedirs(output)						
		i=0
		for file in os.listdir(graphs):
			ego_id = file.split(".edge_list")
			ego_id = long(ego_id[0])
			i+=1
		
			print("Detectando comunidades: "+str(g_type)+" - "+str(alg)+" - Rede: "+str(net)+" - ego("+str(i)+"): "+str(file))
			
			try:

				if ud is False:		# Para grafo Directed
					execute = subprocess.Popen(["/home/amaury/algoritmos/Infomap/Infomap","-i link-list", str(graphs)+str(file), str(output), "--out-name "+str(ego_id), "-N 10", "--directed", "--two-level", "--map"], stdout=subprocess.PIPE)
				else:						# Para grafos Undirected							
					execute = subprocess.Popen(["/home/amaury/algoritmos/Infomap/Infomap","-i link-list", str(graphs)+str(file), str(output), "--out-name "+str(ego_id), "-N 10", "--undirected", "--two-level", "--map"], stdout=subprocess.PIPE)
				value = execute.communicate()[0]
				print value
			except Exception as e:
				print e

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
	print" 			Detecção de Comunidades - INFOMAP Method											"
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

#	if op == 1 or op == 9:																						# Testar se é um grafo direcionado ou não
#		uw = True
#	else:
#		uw = False
	uw = True
######################################################################
	
	net = "n"+str(op)	
	
######################################################################################################################
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_without_ego"
	
	alg = "infomap"
######################################################################################################################
 
	output = "/home/amaury/communities_hashmap/"+str(g_type1)+"/"+str(alg)+"_without_weight/raw/"+str(net)+"/10/"
	graphs = "/home/amaury/graphs_hashmap_infomap_without_weight/"+str(net)+"/"+str(g_type1)+"/"

	print ("Calculando Comunidades para a rede: "+str(net)+" - COM o ego")

	calculate_alg(output,net,uw,ud,g_type1,alg,graphs)
	
######################################################################################################################
######################################################################################################################

#	output = "/home/amaury/communities_hashmap/"+str(g_type2)+"/"+str(alg)+"_without_weight/raw/"+str(net)+"/10/"
#	graphs = "/home/amaury/graphs_hashmap_infomap_without_weight/"+str(net)+"/"+str(g_type2)+"/"
#
#	print ("Calculando Comunidades para a rede: "+str(net)+" - SEM o ego")
#
#	calculate_alg(output,net,uw,ud,g_type2,alg,graphs)
	
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

######################################################################################################################
if __name__ == "__main__": main()
