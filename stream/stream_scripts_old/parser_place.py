# -*- coding: latin1 -*-
#
#Argumentos
#1 - Nome do arquivo de entrada
#
########################################################################
#Script para fazer parser dos arquivos JSON
import json
import mysql.connector
import sys
from mysql.connector import errorcode
# Import library which can print parsed data  
from pprint import pprint

tweet = []

#Colunas
idtweet_fk = []
bounding_box_full = []
bounding_box = []
country = []
country_code = []
full_name = []
id_place = []
name = []
place_type = []
url = []


#contador
i = 0

##########################################################################################################
try:
	cnx = mysql.connector.connect(user='twitter', password='roma031205', host='127.0.0.1', database='twitter')

#Ler arquivo JSON
	file = open(sys.argv[1]) #Verificar como concatenar arquivos em Python...


	try:
		for line in file:
			tweet.append(json.loads(line))		

			idtweet_fk.append(tweet[i]['id'])
 
#Converter lista em String
			bounding_box_full.append(tweet[i]['place']['bounding_box']['coordinates'])	
			if bounding_box_full[i]:
				bounding_box.append(','.join(map(str, bounding_box_full[i][0][0])) + ';' + ','.join(map(str, bounding_box_full[i][0][1])) + ';' + ','.join(map(str, bounding_box_full[i][0][2])) + ';' +','.join(map(str, bounding_box_full[i][0][3])))   
			else:
				bounding_box.append(tweet[i]['place']['bounding_box']['coordinates'])	
			country.append(tweet[i]['place']['country'])
			country_code.append(tweet[i]['place']['country_code'])
			full_name.append(tweet[i]['place']['full_name'])
			id_place.append(tweet[i]['place']['id'])
			name.append(tweet[i]['place']['name'])
			place_type.append(tweet[i]['place']['place_type'])
			url.append(tweet[i]['place']['url'])
			
##########inserir dados no Banco
			try:
				cursor = cnx.cursor()
				add_place = ("INSERT INTO PLACE (idtweet_fk, bounding_box, country, country_code, full_name, id_place, name, place_type, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
				cursor.execute(add_place, (idtweet_fk[i], bounding_box[i], country[i], country_code[i], full_name[i], id_place[i], name[i], place_type[i], url[i]))
				cnx.commit()
				print(idtweet_fk[i],': inserido com sucesso!')

			except Exception as erro:
				print("Linha " + str(i) + ". Erro na inserção dos dados no MySQL: {}".format(erro))		
			
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