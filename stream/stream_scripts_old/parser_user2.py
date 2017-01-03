# -*- coding: latin1 -*-
########################################################################
#Script para fazer parser dos arquivos JSON
import json
import mysql.connector
import sys
from mysql.connector import errorcode
# Import library which can print parsed data  
from pprint import pprint

#tabela
user = []
################################## Tentar remover o contador i
#Colunas
iduser = []
created_at = []
description = []
favourites_count = []
followers_count = []
following = []
friends_count = []
geo_enabled = []
lang = []
listed_count = []
location = []
name = []
profile_image_url = []
screen_name = []
statuses_count = []
time_zone = []
url = []

#contador
i = 0


##########################################################################################################
try:
	cnx = mysql.connector.connect(user='twitter', password='roma031205', host='127.0.0.1', database='twitter')
#print("Tudo certo até aqui!")
#Ler arquivo JSON
	file = open(sys.argv[1])
	try:
		for line in file:
			user = json.loads(line)
			iduser = user[i]['user']['id']
			created_at = user[i]['user']['created_at']
			description = user[i]['user']['description']
			favourites_count = user[i]['user']['favourites_count']
			followers_count = user[i]['user']['followers_count']
			following = user[i]['user']['following']

			friends_count = user[i]['user']['friends_count']
			geo_enabled = user[i]['user']['geo_enabled']
			lang = user[i]['user']['lang']
			listed_count = user[i]['user']['listed_count']
			location = user[i]['user']['location']
			name = user[i]['user']['name']
			profile_image_url = user[i]['user']['profile_image_url']
			screen_name = user[i]['user']['screen_name']
			statuses_count = user[i]['user']['statuses_count']
			time_zone = user[i]['user']['time_zone']
			url = user[i]['user']['url']

##########inserir dados no Banco		
			try:
				cursor = cnx.cursor()
				add_user = ("INSERT INTO USER VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
				cursor.execute(add_user, (iduser[i], created_at[i], description[i], favourites_count[i], followers_count[i], following[i], friends_count[i], geo_enabled[i], lang[i], listed_count[i], location[i], name[i], profile_image_url[i], screen_name[i], statuses_count[i], time_zone[i], url[i]))
				cnx.commit()
				print(name[i],': inserido com sucesso!')
			except Exception as erro:
				print('Erro na inserção dos dados no MySQL: {}'.format(erro))		
			
			i = i+1

	except Exception as erro2:
		print('Erro no parser do arquivo JSON: {}'.format(erro2))
	

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Algo errado com usuário ou senha!")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database não existe!")
	else:
		print(err)
else:
	cnx.close()
