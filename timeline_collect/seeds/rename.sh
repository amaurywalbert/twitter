#!/bin/sh
#Script para criar arquivo com lista com apenas o ID dos arquivos da pasta. Ex. 12831.egofeat --> 12831

	echo "Informe o diretório: "
	read dir
	for o in $(ls -1 $dir); do
		$(echo $o | awk -F. '{print $1}' >> id_tmp.txt);
	done
	sort id_tmp.txt | uniq > id.txt
	#rm id_tmp

