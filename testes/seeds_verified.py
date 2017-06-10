# -*- coding: latin1 -*-
################################################################################################
# Script para coletar amigos a partir de um conjunto de alters do twitter
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')



##Verificar quais dos seeds se tornaram egos.


################################################################################################
#
# Testa se lista ou usuário já foi adicionada(o) ao arquivo correspondente.
#
################################################################################################
		
def check(search,datafile):
	file = datafile.readlines()
	found = False
	for line in file:
		if str(search) in line:
			found = True
			break
		else:
			found = False
	return (found)



######################################################################################################################################################################
######################################################################################################################################################################
#
# Método principal do programa.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	m = 0
	n = 0
	seeds_collected = open(seeds_file,'r')
	eof = False
	while not eof:
		seeds = seeds_collected.readline()		
		if (seeds == ''):
				eof = True
		else:
			egos_collected = open(egos_file,'r')
			if check(seeds,egos_collected):
				m+=1
				print ("Usuário: "+str(seeds)+" é um usuário ego!")
				print	
			else:
				n+=1
			egos_collected.close()
	seeds_collected.close()
	print	
	print("Coleta finalizada!")
	
######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################


seeds_file = "/home/amaury/coleta/users_collected/data/201701041441_seeds_collected.txt"
egos_file = "/home/amaury/coleta_old/ego_collection/data/ego_list.txt"


#Executa o método main
if __name__ == "__main__": main()