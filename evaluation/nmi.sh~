#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de validação dos resultados - Nomalized Mutual Information
##					- NMI - Andrea Lancichinetti et al 2009 New J. Phys. 11 033015
##			 					
## # INPUT:
##		- Comunidades detectadas - Arquivos texto para cada ego em que cada linha contendo os ids do usuários representam uma comunidade do ego.
##		- Comunidades Ground-Truth - Arquivo texto para cada ego em que cada linha contendo os ids do usuários representam uma Lista do ego.
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

op=0
clear
METRIC="nmi"


copra()
{
	clear
	TYPE_GRAPH=$1
	NET=$2
	METRIC=$3
	SINGLETONS=$4
	ALG=$5
	GROUND_TRUTH=/home/amaury/dataset/ground_truth/lists_users_TXT/$SINGLETONS/
	COMMUNITIES=/home/amaury/communities/$TYPE_GRAPH/$ALG/$SINGLETONS/$NET/
	OUTPUT_DIR=/home/amaury/Dropbox/evaluation/$TYPE_GRAPH/$ALG/$METRIC/$SINGLETONS/$NET/
	############################################################################################################
	mkdir -p $OUTPUT_DIR
	V=20	#Parâmetro do COPRA
	echo
	echo
	echo "Os arquivos serão armazenados em: $OUTPUT_DIR"
	for ((THRESHOLD=1; THRESHOLD<=$V; THRESHOLD++)); do
		i=0 		#Ponteiro para o ego
		e=0		#Quantidade de arquivos compativeis... Alguns arquivos para algumas variações do parâmetro V não foram obtidos.
		if [ -e $OUTPUT_DIR$THRESHOLD".txt" ] ; then
			rm $OUTPUT_DIR$THRESHOLD".txt"				# Remover arquivos existentes na pasta de saída.
		fi	
		for file in `ls $COMMUNITIES$THRESHOLD`; do
			let i=$i+1;
			IFS="." read -a fields <<<"$file"					# Renomear (temp) o arquivo "clusters-97197087.edge_list" para clusters-97197087
			IFS="-" read -a file_temp <<<"${fields[0]}"		# Renomear (temp) o arquivo "97197087.edge_list" para 97197087
			
			if [ -e $GROUND_TRUTH${file_temp[1]}".txt" ] ; then
				echo "Calculando $METRIC para o ego: $i - THRESHOLD $THRESHOLD"
#				echo "Ground-Truth File: ${file_temp[1]}".txt" ----- Communitites Detected File: $file"
				/home/amaury/algoritmos/Metricas/mutual3/mutual $COMMUNITIES$THRESHOLD/$file $GROUND_TRUTH${file_temp[1]}".txt" >> $OUTPUT_DIR$THRESHOLD".txt"
				let e=$e+1;
			else
				echo "ERROR - EGO: $i - Arquivo não encontrado!"
			fi
		done
		echo "COPRA - Total de arquivos verificados para o THRESHOLD $THRESHOLD: $e"
	echo "###############################################################"
	echo "###############################################################"
	echo
	done
}

############################################################################################################
echo "###############################################################"
echo "																					"
echo " Algoritmo para cálculo da métrica $METRIC - versão BATCH"
echo "																					"
echo "###############################################################"
echo
echo "Realizar o cálculo usando Singletons?" 
echo " 01 - SIM (Padrão)"
echo " 02 - NÃO"
echo
echo -n "Escolha uma opção: "
read op

if [ -z $op ]; then
	SINGLETONS="singletons"
elif [ $op == 02 ]; then
	SINGLETONS="full"
else
	SINGLETONS="without_singletons"
fi

echo "###############################################################"
echo
echo " 01 - COPRA"
echo	
echo -n "Informe o algoritmo que gerou as comunidades para que seja calculada a métrica: "
read op2
case $op2 in
	01)ALG=copra
		for ((i=1; i<=10; i++)); do
			NET="n$i"
			echo "Calculando $METRIC das comunidades detectadas pelo algoritmo $ALG na rede $NET"
			copra "graphs_with_ego" $NET $METRIC $SINGLETONS $ALG
			copra "graphs_without_ego" $NET $METRIC $SINGLETONS $ALG
		done
		;;

	*) echo
		echo "Opção Inválida! Saindo do script..."
		echo
		exit
		;;
esac