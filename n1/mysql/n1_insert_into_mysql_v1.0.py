# -*- coding: latin1 -*-
################################################################################################
# Script para preparar um arquivo coletado do twitter para ser salvo no MySQL
#	
#
import datetime, sys, os, os.path, shutil, json, mysql.connector, time, MySQLdb
from mysql.connector import errorcode
from pprint import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

################################################################################################
##		Status - Versão 1.0 - Preparar arquivo JSON e inserir no MySQL
## 
################################################################################################

class Database:
    host = 'localhost'
    user = 'amaury'
    password = '1234'
    db = 'twitter_networks'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()

#############################################################################################################################
#
# Método principal do programa. 
#
#############################################################################################################################
#############################################################################################################################

def main():
	db = Database()
 	ef_file = open(egos_friends, 'r')
	for line in ef_file:
		ego = json.loads(line)
		ego_id = ego['ego_id']
		ego_friends = ego['ego_friends']
	
# Data Insert into the table
		try:
			query_ego = """INSERT INTO egos VALUES (%d)""" %(ego_id)
			db.insert(query_ego)
			print query_ego

			for alter_id in ego_friends:
		# Data Insert into the table
				try:
					query_alter = """INSERT INTO alters VALUES (%d)""" %(alter_id)					
					db.insert(query_alter)
					print query_alter
					
					try:
			# Data Insert into the table
						query_ego_alter = """INSERT INTO ego_has_alter VALUES (%d,%d)""" %(ego_id,alter_id)
						db.insert(query_ego_alter)
						print query_ego_alter
					
					
					except:
						print ("Erro ao inserir registro na tabela ALTER_HAS_EGO. ego_id: "+str(ego_id)+" - alter_id: "+str(alter_id))
				
				except:
					print ("Erro ao inserir registro na tabela ALTERS. ego_id: "+str(ego_id)+" - alter_id: "+str(alter_id))

		except:
			print ("Erro ao inserir registro na tabela EGOS. ego_id: "+str(ego_id))
################################################################################################
#
# INICIO DO PROGRAMA
#
#######################################################################################################################################################

egos_friends = "/home/amaury/coleta/n1/egos/friends_data_full.json"
alters_friends = "/home/amaury/coleta/n1/alters/friends_data_full.json"

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()