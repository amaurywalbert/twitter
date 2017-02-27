# -*- coding: latin1 -*-
################################################################################################
# Script para preparar um arquivo coletado do twitter para ser salvo no orientdb
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, simplejson
import pyorient
reload(sys)
sys.setdefaultencoding('utf-8')

################################################################################################
##		Status - Versão 1.0 - Preparar arquivo JSON e inserir no OrientDB
## 
################################################################################################

##########################################################################################################################################################################
##########################################################################################################################################################################
#
# Método principal do programa. 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def main():
	client = pyorient.OrientDB("localhost", 2424)
	session_id = client.connect(db_username, db_password)

	if not client.db_exists(db_name, pyorient.STORAGE_TYPE_PLOCAL):
		print ("Database [" + db_name + "] does not exist! session ending...")
		sys.exit()
	else:
		client.db_open( db_name, db_username, db_password)
		print ("Database [" + db_name + "] opened successfully!")
		
		ef_file = open(egos_friends, 'r')

		for line in ef_file:
			try:
				alter = []
				ego = json.loads(line)
				ego_id = long(ego['ego_id'])
				ego_friends = ego['ego_friends']

				cluster_ego_id = 25
				cluster_alter_id = 21
				cluster_friend_id = 29

### Ver Rollback...				
				rec_position_ego = client.command("INSERT INTO V_ego (ego_id) VALUES (%d)" %(ego_id))
				print rec_position_ego 
				#print rec_position_ego._rid
				time.sleep(5)

				for alter in ego_friends:
					alter_id = long(alter)
					try:
						client.command("INSERT INTO V_alter (alter_id) VALUES (%d)" %(alter_id))
					except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
						print e.errors
					
					
					try:
						client.command("CREATE EDGE E_ego_alter FROM (SELECT FROM V_ego WHERE V_ego.ego_id = %d) TO (SELECT FROM V_alter WHERE V_alter.alter_id = %d)" %(ego_id,alter_id))
					except pyorient.exceptions.PyOrientCommandException as e:
							print e.errors						
					
					#except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
					#	print e.errors
					
			
			except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
				print e.errors
		ef_file.close()
		
		client.db_close()
#####################################################################################################
#				event = {'@V_ego': {"ego_id": ego_id}}
#				rec_position_ego = client.record_create(cluster_id, event)
#				print rec_position_ego._rid
#
#
#			
#				for alter in ego_friends:
#					client.command("INSERT INTO V_alter (alter_id) VALUES(%d)" %(alter))
#					client.command("CREATE EDGE E_ego_alter FROM (SELECT FROM V_ego WHERE V_ego.ego_id = %d) TO (SELECT FROM V_alter WHERE V_alter.alter_id = %d)" %(ego_id,alter))
#			
###############################################################################################
#
# INICIO DO PROGRAMA
#
#######################################################################################################################################################

egos_friends = "/home/amaury/coleta/n1/egos/friends_data_full.json"
alters_friends = "/home/amaury/coleta/n1/alters/friends_data_full.json"

db_name = "twitter_teste"
db_username = "amaury"
db_password = "amaury"


# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()