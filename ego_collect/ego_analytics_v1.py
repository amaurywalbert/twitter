# -*- coding: latin1 -*-
################################################################################################
#
# Script para analisar informações coletadas dos egos do Twitter:
#
################################################################################################
import tweepy, datetime, sys, time, json, os, os.path, shutil, time

reload(sys)
sys.setdefaultencoding('utf-8')


################################################################################################
##		Status - Versão 1.0 - SCRIPT 01
##
##					1 - TESTE - Analisando informações estatísticas das listas coletadas pelos EGOs
##
################################################################################################


            
            
##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	i = 0
	elo = []															#Egos_lists_overview recebe dictionary (arquivo json)
	for line in open(dir_data+"full_ego_lists_overview.json", 'r'):	# Arquivo contendo informações das listas de cada ego (ownerships e subscription)
		elo.append(json.loads(line))
		i+=1
		print i

	
#	elo_dict = 
	
	print len(elo)
	time.sleep(5)



################################################################################################
#
# INICIO DO PROGRAMA
#
################################################################################################

dir_data = "/home/amaury/data_collected/ego_collection/data/"				# SCRIPT - COLETA 1
#dir_data = "/home/amaury/data_collected/ego_collection2/data/"				# SCRIPT - COLETA 2

dir_error = "/home/amaury/data_collected/ego_collection/error/"				# SCRIPT - COLETA 1
#dir_error = "/home/amaury/data_collected/ego_collection2/error/"				# SCRIPT - COLETA 2


# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()	