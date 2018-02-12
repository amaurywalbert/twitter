# -*- coding: latin1 -*-
################################################################################################
#	
#
import datetime, sys, time, json, os, os.path, subprocess
reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versão 1 - Remover linhas em branco de um conjunto de arquivos TXT...
## 		
##		DEVE-SE RENOMEAR O DIRETORIO PARA *******_with_white_lines ANTES DE INICIAR O SCRIPT
######################################################################################################################################################################


######################################################################################################################################################################
#
# Cálculos iniciais sobre o conjunto de dados lidos.
#
######################################################################################################################################################################
def remove_lines(singletons,g_type,alg):
	
	communities = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"_with_white_lines/"+str(singletons)+"/"
	output = "/home/amaury/communities_hashmap/"+str(g_type)+"/"+str(alg)+"/"+str(singletons)+"/"	

	for net in os.listdir(communities):
		if os.path.isdir(communities+net+"/"):
			for threshold in os.listdir(communities+net+"/"):
				if os.path.isdir(communities+net+"/"+threshold+"/"):
					print("######################################################################")
					i=0 		#Ponteiro para o ego
					if not os.path.exists(output+net+"/"+threshold+"/"):
						os.makedirs(output+net+"/"+threshold+"/")
								
					for file in os.listdir(communities+net+"/"+threshold+"/"):
						if os.path.isfile(communities+net+"/"+threshold+"/"+file):
							i+=1	
							if os.path.isfile(output+net+"/"+threshold+"/"+file): 			# Se arquivo existe, pula.
								print ("Arquivo já existe no destino: "+output+net+"/"+threshold+"/"+file)

							else:	
								print(str(g_type)+" - "+str(alg)+" - "+str(singletons)+" - Rede: "+str(net)+" - THRESHOLD: "+str(threshold)+" - ego("+str(i)+"): "+str(file))
								with open(communities+net+"/"+threshold+"/"+file, 'r') as f:
									linhas = f.read().splitlines()									# Elimina linhas em branco (suprime "\n")
									with open(output+net+"/"+threshold+"/"+file, 'w') as g:
										for linha in linhas:
											g.write(linha+"\n")															# Passa para a próxima linha de g

#####################################################################################################################################################################
#
# Método principal do programa.
# Realiza teste e coleta dos dados de cada user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	os.system('clear')
#######################################################################
#######################################################################
	print("######################################################################")	
	print
	print "Algoritmo utilizado na detecção das comunidades"
	print 
	print
	print"  1 - COPRA"
	print"  2 - OSLOM"
	print"  3 - GN"					
	print
	op2 = int(raw_input("Escolha uma opção acima: "))

	if op2 == 1:
		alg = "copra"
	elif op2 == 2:
		alg = "oslom"
	elif op2 == 3:
		alg = "gn"				
	else:
		alg = ""
		print("Opção inválida! Saindo...")
		sys.exit()		
	print
	print ("\n")
######################################################################################################################
	g_type1 = "graphs_with_ego"
	g_type2 = "graphs_without_ego"
	
	singletons1 = "full"
	singletons2 = "without_singletons"

	
######################################################################################################################
	os.system('clear')

	remove_lines(singletons1,g_type1,alg)
	
	remove_lines(singletons1,g_type2,alg)

	remove_lines(singletons2,g_type1,alg)
	
	remove_lines(singletons2,g_type2,alg)

######################################################################################################################		

	print("######################################################################")
	print("\nScript finalizado!\n")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INÍCIO DO PROGRAMA
#
######################################################################################################################################################################

######################################################################################################################
if __name__ == "__main__": main()
