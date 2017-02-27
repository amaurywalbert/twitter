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
		i=0

		for line in ef_file:
			ego = json.loads(line)
			ego_id = (ego['ego_id'])
			ego_friends = ego['ego_friends']
			
			try:
				event = {'@user': {"id": ego_id, "type":"ego"}}
				rec_position = client.record_create(cluster_id, event)
			except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
				pass
			
			for alter in ego_friends:
				alter_id = alter
				try:
					event = {'@user': {"id": alter_id, "type":"alter"}}
					rec_position = client.record_create(cluster_id, event)				
				except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
					pass
				except pyorient.exceptions.PyOrientCommandException as e:
					print e.errors

				try:
					client.command("CREATE EDGE is_friend FROM (SELECT FROM user WHERE id = '%s') TO (SELECT FROM user WHERE id = '%s')" %(ego_id,alter_id))
				except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
					pass
				except pyorient.exceptions.PyOrientCommandException as e:
					print e.errors				
			i+=1
			print i		
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
				event = {'@user': {"id": alter_id, "type":"alter"}}
				rec_position = client.record_create(cluster_id, event)
				print ("Alter "+str(alter_id)+" adicionado sem vínculo ego.")
			except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
				pass
			
			for friend in alter_friends:
				friend_id = friend

				try:
					event = {'@user': {"id": friend_id, "type":"friend"}}
					rec_position = client.record_create(cluster_id, event)
				except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
					pass
				except pyorient.exceptions.PyOrientCommandException as e:
					print e.errors
				
				
				try:
					client.command("CREATE EDGE is_friend FROM (SELECT FROM user WHERE id = '%s') TO (SELECT FROM user WHERE id= '%s')" %(alter_id,friend_id))					
				except pyorient.exceptions.PyOrientORecordDuplicatedException as e:
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
	inicio = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')		# Recupera o instante atual na forma AnoMesDiaHoraMinuto
	insert_ego()
	insert_alter()
	fim = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')		# Recupera o instante atual na forma AnoMesDiaHoraMinuto
	print ("Registros inseridos com sucesso. Inicio: "+str(inicio)+" - Fim: "+str(fim))
	
	
###############################################################################################
#
# INICIO DO PROGRAMA
#
###############################################################################################

egos_friends = "/home/amaury/coleta/n1/egos/friends_data_full.json"
alters_friends = "/home/amaury/coleta/n1/alters/friends_data_full.json"

db_name = "twitter"
db_username = "amaury"
db_password = "amaury"

cluster_id = 21

# Verifica se eh para executar o metodo main()
if __name__ == "__main__": main()