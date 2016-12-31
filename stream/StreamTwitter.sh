##!/bin/bash
#INTERVALO=300 #5 minutos
#while true; do
#	# Verifica se o python está sendo executado
#	if pgrep -x "python" > /dev/null
#	then
#		echo "Executando"
#	else
#		echo "Iniciando..."
#		gnome-terminal -x bash -c "python /home/amaury/twitter/stream/regioes/StreamGYN.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/amaury/twitter/stream/regioes/StreamSalvador.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/amaury/twitter/stream/regioes/StreamCatalao.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/amaury/twitter/stream/regioes/StreamRioVerde.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/amaury/twitter/stream/regioes/StreamSampa.py; exec $SHELL";
#	fi
#	sleep $INTERVALO
#done
