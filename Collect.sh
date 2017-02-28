#!/bin/bash
INTERVALO=300	#5 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."
		gnome-terminal -x bash -c "python ~/twitter/n1/n1_egos_friends_collect_v2.0.py; exec $SHELL";
	fi
	sleep $INTERVALO
done
