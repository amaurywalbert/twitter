# -*- coding: latin1 -*-
################################################################################################
import sys, time, json, os, os.path, shutil

reload(sys)
sys.setdefaultencoding('utf-8')
######################################################################################################################################################################
##		Status - copia somente egos com mais de 3,5k amigos, que já estão separados em um diretório
######################################################################################################################################################################
#########################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	i=0
	for file in os.listdir(source):
		if os.path.isfile(origem+file):
			i+=1
			shutil.move(origem+file, destino)
			print str(i)+" - ok"
			
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
source = "/home/amaury/graphs/n5_3_5k/graphs_with_ego/"
origem = "/home/amaury/graphs/n5/graphs_without_ego/"
destino ="/home/amaury/graphs/n5_3_5k/graphs_without_ego/"

#Cria os diretórios para armazenamento dos arquivos
if not os.path.exists(destino):
	os.makedirs(destino)	

#Executa o método main
if __name__ == "__main__": main()