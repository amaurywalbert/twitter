#!/bin/bash
#Script para concatenar os arquivos JSON contendo informações dos tweets coletados
#Indique um diretório contendo os arquivos como parametro

if [ ! -d "$1" ]; then # testa se diretório existe
	echo "Entre com um diretório válido!";
else
	cat *.json > join.json
fi