# -*- coding: latin1 -*-
################################################################################################
#	
#
import sys,os,os.path,time
import numpy as np
from math import*
# Load CSV using Pandas from URL
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt


reload(sys)
sys.setdefaultencoding('utf-8')



######################################################################################################################################################################
#
##		Status - Versão 1 - Script para plotar gráficos contendo as principais informações sobre as comunidades detectadas...
#
######################################################################################################################################################################

######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
	print "################################################################################"
	print"																											"
	print" 	Plotando infomações sobre as comunidades detectadas com o INFOMAP					"
	print"																											"
	print"																											"
	print"#################################################################################"
	print"#################################################################################"
	print "Algoritmo utilizado na detecção das comunidades"
	print
	print"  1 - COPRA - Without Weight - K=10"
#	print"  2 - COPRA - Without Weight - K=2-20"
#	print"  3 - OSLOM - Without Weight - K=5,10,50"
	print"  4 - OSLOM - Without Weight - K=50"
	print"  5 - RAK - Without Weight"		
#
#	print"  6 - INFOMAP - Partition"
	print"  6 - INFOMAP - Partition - Without Weight"												
	print
	op2 = int(raw_input("Escolha uma opção acima: "))
#
	if op2 == 1:
		alg = "copra_without_weight_k10"
#	elif op2 == 2:
#		alg = "copra_without_weight"
#	elif op2 == 3:
#		alg = "oslom_without_weight"
	elif op2 == 4:
		alg = "oslom_without_weight_k50"
	elif op2 == 5:
		alg = "rak_without_weight"
	elif op2 == 6:
		alg = "infomap_without_weight"		
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()	
	print ("\n")
	print	

	
	nets = ['n1','n2','n3','n4']
#	names = ['n_nodes','n_edges','n_comm','max_comm_len','min_comm_len','comm_size_avg','comm_size_std','n_singletons','alters_ignored','chen_modularity_avg','chen_mod_density_avg','chen_conductance_avg','chen_intra_density_avg','snap_coef_clust_avg','snap_conductance_avg','snap_density_avg','snap_modularity_avg']


	for net in nets:
		source_dir = str(source)+str(alg)+"/"+str(net)+"/"
		if not os.path.isdir(source_dir):
			print ("Impossível localizar diretório: "+str(source_dir))
		else:
			for file in os.listdir(source_dir):
				df = pd.read_csv(source_dir+file, encoding='ISO-8859-1')
				df = df.drop(['ego_id','min_comm_len','n_singletons','alters_ignored','comm_size_std','snap_coef_clust_avg','snap_conductance_avg','snap_density_avg','snap_modularity_avg'], axis=1)
				if 'Unnamed: 18' in df.columns:
					df = df.drop(['Unnamed: 18'], axis=1)
				df.columns = ['nodes','edges','comm','max_comm','comm_size','modularity','mod_density','conductance','intra_density']
				description = df.describe()
				print ("---------------------------------------------------------------------------------------------------")
				print(alg, net,description)
				scatter_matrix(df)

#				if net == "n1":
#					title = "Follow"
#				elif net == "n2":
#					title = "Retweets"
#				elif net == "n3":
#					title = "Likes"
#				elif net == "n4":
#					title = "Mentions"
#				else:
#					sys.exit()
#				plt.title(str(title))
				
				plt.show()

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap_statistics/"

#Executa o método main
if __name__ == "__main__": main()