# -*- coding: latin1 -*-
################################################################################################
import datetime, sys, time, json, os, os.path, shutil, time

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
######################################################################################################################################################################
##		Status - Versão 1 - Receber dataset e converter o longint dos usuários para int - ids começam em 01
##									Converte dados para cada ego, portanto não dá pra comparar o conjunto de alters entre os egos...
##									Para comparar conjunto de alters, deve-se usar o "hashmap_dataset.py"
##	
##								ATENÇÃO - ESTE SCRIPT ESTÁ SENDO USADO APENAS PARA AS REDES N5 E N10 - PARA OS EGOS COM MAIS DE 3,5K ALTERS.
##
## # INPUT: Arquivos só com redes-ego
## 
## # OUTPUT: Arquivos de entrada convertidos para int
##
######################################################################################################################################################################


######################################################################################################################################################################
#
# ADD egonet ao hashmap 
#
#		Para cada par de usuários representando cada terminal de uma aresta, adiciona o id do usuário como chave de um dicionário e vincula essa chave a um numero dado pela numero sequencial correspondente à aparição do usuário no arquivo.
#
######################################################################################################################################################################
def add_hashmap_egonet(f):	
	hashmap = {}
	i=0
	for line in f:
		alters = line.split(' ')
		if alters[0] != "\n":
			alter0 = long(alters[0])			
			if not hashmap.has_key(alter0):
				i+=1
				hashmap[alter0] = i
		if alters[1] != "\n":
			alter1 = long(alters[1])			
			if not hashmap.has_key(alter1):
				i+=1
				hashmap[alter1] = i
	return(hashmap)
	
######################################################################################################################################################################
#
# SAVE egonet - hashmap 
#
##		Percorre o arquivo e verifica o valor vinculado a ele consultando o HashMAP. Escreve o novo valor no mesmo formato do arquivo de entrada, mantendo o valor do peso da aresta inalterado, caso houver.
#
######################################################################################################################################################################
def save_hashmap_egonet(hashmap,f,g):
	for line in f:
		alters = line.split(' ')			
		alter0 = long(alters[0])
		alter1 = long(alters[1])
		if len(alters) > 2:
			g.write(str(hashmap[alter0])+" "+str(hashmap[alter1])+" "+str(alters[2])) 	# Já tem a quebra (\n) no último elemento alters[2]
		else:
			g.write(str(hashmap[alter0])+" "+str(hashmap[alter1])+"\n")

#####################################################################################################################################################################
#Prepara os dados para converter
########################################################################################
def prepare(egonet_source,egonet_output):
	for diretorio in os.listdir(egonet_source):
		if diretorio in ("graphs_with_ego","graphs_without_ego"):
			j=0				
			for file in os.listdir(egonet_source+"/"+diretorio+"/"):			
				j+=1
				print ("Convertendo arquivos - net: "+str(egonet_source)+" - "+str(diretorio)+" - ego: "+str(j)+": "+str(file))
					
				with open(egonet_source+"/"+diretorio+"/"+str(file), 'r') as f:		# SOURCE - Para arquivos no diretório ego/net/nx/graphs_with_ego/
					hashmap = add_hashmap_egonet(f)
						
				print len(hashmap)
						
				if not os.path.exists(egonet_output+"/"+diretorio+"/"):
					os.makedirs(egonet_output+"/"+diretorio+"/")
					
				with open(egonet_source+"/"+diretorio+"/"+str(file), 'r') as f:		# Tenho que abrir de novo para que ele leia do início do arquivo.
					with open(egonet_output+"/"+diretorio+"/"+str(file), 'w') as g:
						save_hashmap_egonet(hashmap,f,g)
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
	
	egonet_source1 = "/home/amaury/graphs/n5_3_5k/"
	egonet_output1 = "/home/amaury/graphs_hashmap/n5_3_5k/"

#	egonet_source2 = "/home/amaury/graphs/n10_3_5k/"
#	egonet_output2 = "/home/amaury/graphs_hashmap/n10_3_5k/"


	print ("Atenção! Este script apagará os seguintes diretórios:")
	print egonet_output1
#	print egonet_output2
	print
	op = str(raw_input("Deseja continuar? (s/n) "))

	if op != 's' and op != 'sim':
		print ("Script finalizado pelo usuário...")
		sys.exit()

	else:
		if os.path.exists(egonet_output1):
			shutil.rmtree(egonet_output1)
		
#		if os.path.exists(egonet_output2):
#			shutil.rmtree(egonet_output2)
			
		prepare(egonet_source1,egonet_output1)
#		prepare(egonet_source2,egonet_output2)			
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


######################################################################################################################
if __name__ == "__main__": main()
