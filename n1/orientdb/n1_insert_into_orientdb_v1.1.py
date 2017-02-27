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
# Inserir dados dos EGOs e seus amigos 
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def insert_ego():
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
			ego = json.loads(line)
			ego_id = (ego['ego_id'])
			ego_friends = ego['ego_friends']
			
			try:
				event_ego = {'@V_ego': {"ego_id": ego_id}}
				rec_position_ego = client.record_create(cluster_ego_id, event_ego)
#				print rec_position_ego._rid
			except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
#				print e.errors
				pass
			
			for alter in ego_friends:
				alter_id = alter
				try:
					event_alter = {'@V_alter': {"alter_id": alter_id}}
					rec_position_alter = client.record_create(cluster_alter_id, event_alter)
#					print rec_position_alter._rid
					client.command("CREATE EDGE E_ego_alter FROM (SELECT FROM V_ego WHERE ego_id = '%s') TO (SELECT FROM V_alter WHERE alter_id= '%s')" %(ego_id,alter_id))				
#					client.command("CREATE EDGE E_ego_alter FROM %s TO %s" %(rec_position_ego._rid,rec_position_alter._rid))
				
				except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
					pass
#					print e.errors
				except pyorient.exceptions.PyOrientCommandException as e:
					print e.errors
				
		ef_file.close()
		
		client.db_close()

##########################################################################################################################################################################
#
# Inserir dados dos Alters e seus amigos
#
##########################################################################################################################################################################
##########################################################################################################################################################################

def insert_alter():
	client = pyorient.OrientDB("localhost", 2424)
	session_id = client.connect(db_username, db_password)

	if not client.db_exists(db_name, pyorient.STORAGE_TYPE_PLOCAL):
		print ("Database [" + db_name + "] does not exist! session ending...")
		sys.exit()
	else:
		client.db_open( db_name, db_username, db_password)
		print ("Database [" + db_name + "] opened successfully!")
		
		af_file = open(alters_friends, 'r')
		i = 0
		for line in af_file:
			alter = json.loads(line)
			alter_id = (alter['alter_id'])
			alter_friends = alter['alter_friends']
			try:
				event_alter = {'@V_alter': {"alter_id": alter_id}}
				rec_position_alter = client.record_create(cluster_alter_id, event_alter)
#				print rec_position_alter._rid
			except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
#				print e.errors
				pass
			
			for friend in alter_friends:
				friend_id = friend
				try:
					event_friend = {'@V_friend': {"friend_id": friend_id}}
					rec_position_friend = client.record_create(cluster_friend_id, event_friend)
#					print rec_position_friend._rid
					client.command("CREATE EDGE E_alter_friend FROM (SELECT FROM V_alter WHERE alter_id = '%s') TO (SELECT FROM V_friend WHERE friend_id= '%s')" %(alter_id,friend_id))
				
				except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
#					print e.errors
					pass
				except pyorient.exceptions.PyOrientCommandException as e:
					print e.errors
			i+=1
			print i		
		af_file.close()
		
		client.db_close()
		
###############################################################################################
###############################################################################################

def main():
	insert_ego()
	insert_alter()
	print ("Registros inseridos com sucesso")
	
	
###############################################################################################
#
# INICIO DO PROGRAMA
#
###############################################################################################

egos_friends = "/home/amaury/coleta/n1/egos/friends_data_full.json"
alters_friends = "/home/amaury/coleta/n1/alters/friends_data_full.json"

db_name = "twitter_teste"
db_username = "amaury"
db_password = "amaury"

cluster_ego_id = 21
cluster_alter_id = 25
cluster_friend_id = 29

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()