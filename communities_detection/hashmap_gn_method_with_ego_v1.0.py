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
##		Status - Versão 1 - GirvanNewman algorithm and find the best community split by maximizing modularity measure
## 
## 							
## # INPUT: Grafos
## 
## # OUTPUT:
##			Communities
######################################################################################################################################################################


######################################################################################################################################################################
#
# Plota os Gráficos das redes-ego... não necessário...
#
######################################################################################################################################################################
def plot_gn_method(partition):
	size = float(len(set(partition.values())))
	pos = nx.spring_layout(G)
	count = 0
	for com in set(partition.values()):
		count = count + 1
		list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
		nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, node_color = str(count / size))

	nx.draw_networkx_edges(G,pos, alpha=0.5)
	plt.show()
			
######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def calculate_alg(output,net,uw,ud,g_type,alg,graphs_pajek):

	if not os.path.exists(graphs_pajek):
		print ("\nDiretório com grafos não encontrado: "+str(graphs_pajek)+"\n")
	else:					
		
		print	
		print("######################################################################")
		print ("Os arquivos serão armazenados em: "+str(output))
		print("######################################################################")
		if not os.path.exists(output):
			os.makedirs(output)						
		i=0
		for file in os.listdir(graphs_pajek):
			ego_id = file.split(".pajek")
			ego_id = long(ego_id[0])
			i+=1
		
			print("Detectando comunidades: "+str(g_type)+" - "+str(alg)+" - Rede: "+str(net)+" - ego("+str(i)+"): "+str(file))
			
			try:
				if uw is False:
					execute = subprocess.Popen(["/home/amaury/algoritmos/radatools-4.1-linux64/Communities_Detection/Communities_Detection.exe", "N", "WN", "f", "1", "0", "1.0", graphs_pajek+file, output+file], stdout=subprocess.PIPE)
				else:
					execute = subprocess.Popen(["/home/amaury/algoritmos/radatools-4.1-linux64/Communities_Detection/Communities_Detection.exe", "N", "UN", "f", "1", "0", "1.0", graphs_pajek+file, output+file], stdout=subprocess.PIPE)						
				value = execute.communicate()[0]
				print value
			except Exception as e:
				print e				
						
#			with open(str(output)+str(ego_id)".txt", 'w') as f:
#				f.write(json.dumps(partition))

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
	print" 			Detecção de Comunidades - Girvan and Newman (GN) Method										"
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
######################################################################
	
	net = "n"+str(op)	
	
######################################################################################################################
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_without_ego"
	
	alg = "gn"
######################################################################################################################
 
	output = "/home/amaury/communities_hashmap/"+str(g_type1)+"/"+str(alg)+"/raw/"+str(net)+"/"
	graphs_pajek = "/home/amaury/graphs_hashmap_pajek/"+str(net)+"/"+str(g_type1)+"/"

	print ("Calculando Comunidades para a rede: "+str(net)+" - COM o ego")

	calculate_alg(output,net,uw,ud,g_type1,alg,graphs_pajek)
	
######################################################################################################################
######################################################################################################################

#	output = "/home/amaury/communities_hashmap/"+str(g_type2)+"/"+str(alg)+"/raw/"+str(net)+"/"
#	graphs_pajek = "/home/amaury/graphs_hashmap_pajek/"+str(net)+"/"+str(g_type2)+"/"
#
#	print ("Calculando Comunidades para a rede: "+str(net)+" - SEM o ego")
#
#	calculate_alg(output,net,uw,ud,g_type2,alg,graphs_pajek)
	
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
