# -*- coding: latin1 -*-
################################################################################################
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Mover arquivos do threshold 1 do Copra para uma pasta nova Copra_partition
######################################################################################################################################################################

######################################################################################################################################################################
# Move os arquivos
######################################################################################################################################################################

def move(origem,destino):
	
	if os.path.exists(origem):
		if not os.path.exists(destino):
			os.makedirs(destino)
				
		for threshold in os.listdir(origem):
			if threshold == "1" or threshold == "01" or threshold == "1.json" or threshold == "01.json":
				print str(origem)+str(threshold)

				shutil.move(origem+threshold,destino)


######################################################################################################################################################################
# Prepara os diretórios
######################################################################################################################################################################

def prepare(g_type,singletons):
	
	for i in range(10):
		i+=1
		net = "n"+str(i)
		origem1 = "/home/amaury/communities_hashmap/"+str(g_type)+"/copra/"+str(singletons)+"/"+str(net)+"/"
		destino1 = "/home/amaury/communities_hashmap/"+str(g_type)+"/copra_partition/"+str(singletons)+"/"+str(net)+"/"
	
		origem2 = "/home/amaury/communities/"+str(g_type)+"/copra/"+str(singletons)+"/"+str(net)+"/"
		destino2 = "/home/amaury/communities/"+str(g_type)+"/copra_partition/"+str(singletons)+"/"+str(net)+"/"
		
		origem3 = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/"+str(g_type)+"/copra/"+str(singletons)+"/"+str(net)+"/"
		destino3 = "/home/amaury/Dropbox/evaluation_hashmap/communities_statistics/"+str(g_type)+"/copra_partition/"+str(singletons)+"/"+str(net)+"/"
		
		origem4 = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/average_degree/"+str(g_type)+"/copra/"+str(singletons)+"/"+str(net)+"/"
		destino4 = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth/average_degree/"+str(g_type)+"/copra_partition/"+str(singletons)+"/"+str(net)+"/"
	
		origem5 = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth_old/average_degree/"+str(g_type)+"/copra/"+str(singletons)+"/"+str(net)+"/"	
		destino5 = "/home/amaury/Dropbox/evaluation_hashmap/without_ground_truth_old/average_degree/"+str(g_type)+"/copra_partition/"+str(singletons)+"/"+str(net)+"/"
		
		move(origem1,destino1)
		move(origem2,destino2)
		move(origem3,destino3)
		move(origem4,destino4)
		move(origem5,destino5)		

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_without_ego"
	singletons1 = "full"
	singletons2 = "without_singletons"
	

	prepare(g_type1,singletons1)
	prepare(g_type1,singletons2)
	prepare(g_type2,singletons1)
	prepare(g_type2,singletons2)

	print("######################################################################")
	print("Script finalizado!")
	print("######################################################################\n")
#####################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################



#Executa o método main
if __name__ == "__main__": main()