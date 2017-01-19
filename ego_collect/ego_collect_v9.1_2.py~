#!/bin/bash
INTERVALO=300 #5 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."
		gnome-terminal -x bash -c "python /home/amaury/twitter/ego_collect/ego_collect_v9_1.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/amaury/twitter/ego_collect/ego_collect_v9_2.py; exec $SHELL";
	fi
	sleep $INTERVALO
done
