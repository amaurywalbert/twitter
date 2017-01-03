# -*- coding: latin1 -*-
########################################################################
#Script para fazer parser dos arquivos JSON
#Argumentos
#1 - Nome do arquivo de entrada
#2 - Código do Local
#	1 - Goiânia
#	2 - São Paulo
#	3 - Salvador
#	4 - Rio Verde
#	5 - Catalão
#
import json, mysql.connector, sys, os.path
from mysql.connector import errorcode  
from pprint import pprint

#############################################################################################################################
#############################################################################################################################

def valida_parametros(arquivo):
	if not os.path.isfile(arquivo):
		print "Arquivo não encontrado!"
		sys.exit()
	else:
		print " 1 - Goiânia"
		print " 2 - São Paulo"
		print " 3 - Salvador"
		print " 4 - Rio Verde"
		print " 5 - Catalão"
		op = raw_input('Escolha uma região: ')
		for letra in opcoes:
			if op not in opcoes:
				print "Região Inválida!"
				sys.exit()
	return(op)
	print "Iniciando..."


#############################################################################################################################
#############################################################################################################################


opcoes = '12345'
regiao = valida_parametros(sys.argv[1]) 

#############################################################################################################################
#############################################################################################################################


#Registros
tweet = []

#Tabela USER
user_iduser = []
user_created_at = []
user_description = []
user_favourites_count = []
user_followers_count = []
user_following = []
user_friends_count = []
user_geo_enabled = []
user_lang = []
user_listed_count = []
user_location = []
user_name = []
user_profile_image_url = []
user_screen_name = []
user_statuses_count = []
user_time_zone = []
user_url = []

#Tabela TWEET
tweet_idtweet = []
tweet_contributors = []
tweet_coordinates = []
tweet_geo_latitude = []
tweet_geo_longitude = []
tweet_created_at = []
tweet_favorite_count = []
tweet_favorited = []
tweet_filter_level = []
tweet_in_reply_to_status_id = []
tweet_in_reply_to_user_id = []
tweet_is_quote_status = []
tweet_lang = []
tweet_retweet_count = []
tweet_retweeted = []
tweet_source = []
tweet_text = []
tweet_timestamp_ms = []
tweet_truncated = []
tweet_iduser_fk = []
tweet_idregion_fk = []

#Tabela ENTITIES
entities_idtweet_fk = []
entities_hashtags_full = []
entities_symbols_full = []
entities_urls_full = []
entities_user_mentions_full = []

#Tabela PLACE
place_idtweet_fk = []
place_bounding_box_full = []
place_bounding_box = []
place_country = []
place_country_code = []
place_full_name = []
place_id_place = []
place_name = []
place_place_type = []
place_url = []

#############################################################################################################################
#############################################################################################################################
#contador
i = 0
#############################################################################################################################
#############################################################################################################################

try:
	cnx = mysql.connector.connect(user='twitter', password='roma031205', host='127.0.0.1', database='twitter')
#Ler arquivo JSON
	file = open(sys.argv[1])
#############################################################################################################################
#############################################################################################################################
#Realizar parser
	try:
		for line in file:			
			tweet.append(json.loads(line))
#user			
			user_iduser.append(tweet[i]['user']['id'])
			user_created_at.append(tweet[i]['user']['created_at'])			
			user_description.append(unicode(tweet[i]['user']['description']))
			user_favourites_count.append(tweet[i]['user']['favourites_count'])
			user_followers_count.append(tweet[i]['user']['followers_count'])
			user_following.append(tweet[i]['user']['following'])
			user_friends_count.append(tweet[i]['user']['friends_count'])
			user_geo_enabled.append(tweet[i]['user']['geo_enabled'])
			user_lang.append(tweet[i]['user']['lang'])
			user_listed_count.append(tweet[i]['user']['listed_count'])
			user_location.append(tweet[i]['user']['location'])
			user_name.append(unicode(tweet[i]['user']['name']))
			user_profile_image_url.append(tweet[i]['user']['profile_image_url'])
			user_screen_name.append(tweet[i]['user']['screen_name'])
			user_statuses_count.append(tweet[i]['user']['statuses_count'])
			user_time_zone.append(tweet[i]['user']['time_zone'])
			user_url.append(tweet[i]['user']['url'])
#tweet
			tweet_idtweet.append(tweet[i]['id'])
			tweet_contributors.append(tweet[i]['contributors'])
			tweet_coordinates.append(tweet[i]['coordinates'])
			if tweet_coordinates[i]:
				tweet_geo_latitude.append(tweet[i]['coordinates']['coordinates'][0])
				tweet_geo_longitude.append(tweet[i]['coordinates']['coordinates'][1])
			else:
				tweet_geo_latitude.append(tweet[i]['coordinates'])
				tweet_geo_longitude.append(tweet[i]['coordinates'])
			tweet_created_at.append(tweet[i]['created_at'])
			tweet_favorite_count.append(tweet[i]['favorite_count'])
			tweet_favorited.append(tweet[i]['favorited'])
			tweet_filter_level.append(tweet[i]['filter_level'])
			tweet_in_reply_to_status_id.append(tweet[i]['in_reply_to_status_id'])
			tweet_in_reply_to_user_id.append(tweet[i]['in_reply_to_user_id'])
			tweet_is_quote_status.append(tweet[i]['is_quote_status'])
			tweet_lang.append(tweet[i]['lang'])		
			tweet_retweet_count.append(tweet[i]['retweet_count'])
			tweet_retweeted.append(tweet[i]['retweeted'])
			tweet_source.append(tweet[i]['source'])
			tweet_text.append(tweet[i]['text'])
			tweet_timestamp_ms.append(tweet[i]['timestamp_ms'])
			tweet_truncated.append(tweet[i]['truncated'])
			tweet_iduser_fk.append(tweet[i]['user']['id'])
			tweet_idregion_fk.append(regiao) ## Verificar argumentosssss ######################################
#entities	
			entities_idtweet_fk.append(tweet[i]['id'])
			entities_hashtags_full.append(';'.join(map(str, tweet[i]['entities']['hashtags'])))			
			entities_symbols_full.append(';'.join(map(str, tweet[i]['entities']['symbols'])))
			entities_urls_full.append(';'.join(map(str, tweet[i]['entities']['urls'])))
			entities_user_mentions_full.append(';'.join(map(str, tweet[i]['entities']['user_mentions'])))
#place
			place_idtweet_fk.append(tweet[i]['id'])			
			place_bounding_box_full.append(tweet[i]['place']['bounding_box']['coordinates'])	
			if place_bounding_box_full[i]:
				place_bounding_box.append(','.join(map(str, place_bounding_box_full[i][0][0])) + ';' + ','.join(map(str, place_bounding_box_full[i][0][1])) + ';' + ','.join(map(str, place_bounding_box_full[i][0][2])) + ';' +','.join(map(str, place_bounding_box_full[i][0][3])))   
			else:
				place_bounding_box.append(tweet[i]['place']['bounding_box']['coordinates'])	
			place_country.append(tweet[i]['place']['country'])
			place_country_code.append(tweet[i]['place']['country_code'])
			place_full_name.append(tweet[i]['place']['full_name'])
			place_id_place.append(tweet[i]['place']['id'])
			place_name.append(tweet[i]['place']['name'])
			place_place_type.append(tweet[i]['place']['place_type'])
			place_url.append(tweet[i]['place']['url'])

#############################################################################################################################
#############################################################################################################################
##########inserir dados no Banco
##########Tabela USER
			try:
				cursor = cnx.cursor()
				add_user = ("INSERT INTO USER VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")				
				cursor.execute(add_user, (user_iduser[i], user_created_at[i], user_description[i], user_favourites_count[i], user_followers_count[i], user_following[i], user_friends_count[i], user_geo_enabled[i], user_lang[i], user_listed_count[i], user_location[i], user_name[i], user_profile_image_url[i], user_screen_name[i], user_statuses_count[i], user_time_zone[i], user_url[i]))
				cnx.commit()
			except Exception as erro:
				print("Linha " + str(i) + ". Erro MySQL - Table USER: {}".format(erro))

##########Tabela TWEET							
			try:
				cursor = cnx.cursor()
				add_tweet = ("INSERT INTO TWEET VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
				cursor.execute(add_tweet, (tweet_idtweet[i], tweet_contributors[i], tweet_geo_latitude[i], tweet_geo_longitude[i], tweet_created_at[i], tweet_favorite_count[i], tweet_favorited[i], tweet_filter_level[i], tweet_in_reply_to_status_id[i], tweet_in_reply_to_user_id[i], tweet_is_quote_status[i], tweet_lang[i], tweet_retweet_count[i], tweet_retweeted[i], tweet_source[i], tweet_text[i], tweet_timestamp_ms[i], tweet_truncated[i], tweet_iduser_fk[i], tweet_idregion_fk[i]))
				cnx.commit()
			except Exception as erro:
				print("Linha " + str(i) + ". Erro MySQL - Table TWEET: {}".format(erro))			

##########Tabela ENTITIES
			try:
				cursor = cnx.cursor()
				add_entities = ("INSERT INTO ENTITIES (entities_idtweet_fk, entities_hashtags, entities_symbols, entities_urls, entities_user_mentions) VALUES (%s, %s, %s, %s,%s)")
				cursor.execute(add_entities, (entities_idtweet_fk[i], entities_hashtags_full[i], entities_symbols_full[i], entities_urls_full[i], entities_user_mentions_full[i]))
				cnx.commit()
			except Exception as erro:
				print("Linha " + str(i) + ". Erro MySQL - Table ENTITIES: {}".format(erro))
				
##########Tabela PLACE			
			try:
				cursor = cnx.cursor()
				add_place = ("INSERT INTO PLACE (place_idtweet_fk, place_bounding_box, place_country, place_country_code, place_full_name, place_id_place, place_name, place_place_type, place_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")				
				cursor.execute(add_place, (place_idtweet_fk[i], place_bounding_box[i], place_country[i], place_country_code[i], place_full_name[i], place_id_place[i], place_name[i], place_place_type[i], place_url[i]))
				cnx.commit()
			except Exception as erro:
				print("Linha " + str(i) + ". Erro MySQL - Table PLACE: {}".format(erro))		
			
			i = i+1
#############################################################################################################################
#############################################################################################################################
	except Exception as erro2:
		print('Erro no parser do arquivo JSON: {}'.format(erro2))
	
#############################################################################################################################
#############################################################################################################################
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Algo errado com usuário ou senha!")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database não existe!")
	else:
		print(err)
else:
	cnx.close()







################################################################################################
################################################################################################
################################################################################################

				