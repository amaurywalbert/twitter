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
	print

#	algs = ['infomap']
	algs = ['infomap','infomap_without_weight']
	nets = ['n1','n2','n3','n4']
#	names = ['n_nodes','n_edges','n_comm','max_comm_len','min_comm_len','comm_size_avg','comm_size_std','n_singletons','alters_ignored','chen_modularity_avg','chen_mod_density_avg','chen_conductance_avg','chen_intra_density_avg','snap_coef_clust_avg','snap_conductance_avg','snap_density_avg','snap_modularity_avg']

	for alg in algs:
		for net in nets:
			source_dir = str(source)+str(alg)+"/"+str(net)+"/"
			if not os.path.isdir(source_dir):
				print ("Impossível localizar diretório: "+str(source_dir))
			else:
				for file in os.listdir(source_dir):
					df = pd.read_csv(source_dir+file, encoding='ISO-8859-1')
					df = df.drop(['ego_id','Unnamed: 18','min_comm_len','n_singletons','alters_ignored','comm_size_std','snap_coef_clust_avg','snap_conductance_avg','snap_density_avg','snap_modularity_avg'], axis=1)
					df.columns = ['nodes','edges','comm','max_comm','comm_size','modularity','mod_density','conductance','intra_density']
					description = df.describe()
					print(net,description)
					scatter_matrix(df)

#					if net == "n1":
#						title = "Follow"
#					elif net == "n2":
#						title = "Retweets"
#					elif net == "n3":
#						title = "Likes"
#					elif net == "n4":
#						title = "Mentions"
#					else:
#						sys.exit()
#					plt.title(str(title))
					
					plt.show()
					 						
				 
		

	





######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

source = "/home/amaury/Dropbox/evaluation_hashmap_statistics/"

#Executa o método main
if __name__ == "__main__": main()