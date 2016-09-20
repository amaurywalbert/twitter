#!/bin/bash
INTERVALO=300 #5 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."
		python /home/amaury/twitter/stream/StreamGYN.py
	fi
	sleep $INTERVALO
done
