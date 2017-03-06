# -*- coding: latin1 -*-
################################################################################################
# Script para teste de busca com árvore binária ou tabela hash
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, simplejson
from BSTNode import BSTNode	
#Script que contém as chaves para autenticação do twitter e o outro é uma implementação de árvore para facilitar a busca

reload(sys)
sys.setdefaultencoding('utf-8')

def bst():
	t_i = datetime.datetime.now()
	print ("Tempo inicial: "+str(t_i))
	with open(users_list_file,'r') as users_verified:	
		tree = BSTNode(0)
		for line in users_verified:
			node = line
			tree.add(long(node))
	t_f = datetime.datetime.now()
	print ("Tempo final  : "+str(t_f))
	t = t_f-t_i
	print ("Tempo de construção: "+str(t))
	return tree
#############################################################################################################################################
def hash_table():
	t_i = datetime.datetime.now()
	print ("Tempo inicial: "+str(t_i))
	dictionary = {}
	with open(users_list_file,'r') as users_verified:	
		for line in users_verified:
			line = long(line)
			data = "/home/amaury/coleta/n1/egos/bin/"+str(line)+".dat"
			dictionary[line] = data
	t_f = datetime.datetime.now()
	print ("Tempo final  : "+str(t_f))
	t = t_f-t_i
	print ("Tempo de construção: "+str(t))
	return dictionary
#############################################################################################################################################
#############################################################################################################################################

def main():
	print ("Construindo Árvore Binária...")
	tree = bst()
	print
	print ("Construindo Tabela Hash...")
	dictionary = hash_table()

	print
	print
	
	print ("Consultando Árvore Binária...")
	t_i_bst = datetime.datetime.now()
	with open(users_list_file,'r') as users_list:
		for user in users_list:
			if not tree.get(long(user)):							#Consulta na árvore binária se o user já foi verificado.
				print("######################################################################")
	t_f_bst = datetime.datetime.now()
	t_bst = t_f_bst - t_i_bst
	
	print
				
	print ("Consultando Tabela Hash...")
	t_i_hash = datetime.datetime.now()				
	with open(users_list_file,'r') as users_list:
		for user in users_list:
			dir = dictionary.get(long(user))					#Consulta na tabela se o usuário já foi verificado
			if not dir:
				print("######################################################################")	
	t_f_hash = datetime.datetime.now()
	t_hash = t_f_hash - t_i_hash			
	
	print
	print("Teste finalizado!")
	print
	
	print ("Tempo de consulta da árvore binária: "+str(t_bst))
	print ("Tempo de consulta da tabela hash   : "+str(t_hash))

#############################################################################################################################################
# INÍCIO DO PROGRAMA
#
#############################################################################################################################################

users_list_file = "/home/amaury/coleta/n1_10egos/egos_list.txt" #### Arquivo contendo a lista dos usuários a serem buscados


#Executa o método main
if __name__ == "__main__": main()