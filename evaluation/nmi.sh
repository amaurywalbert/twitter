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
METRIC="NMI"


copra()
{
	clear
	#PARÂMETROS $DESCRIPTION $TYPE_GRAPH $NET $METRIC $ALG
	DESCRIPTION=$1
	TYPE_GRAPH=$2
	NET=$3
	METRIC=$4
	ALG=$5
	GROUND_TRUTH=/home/amaury/dataset/ground_truth/lists_users_TXT/
	COMMUNITIES=/home/amaury/communities/$TYPE_GRAPH/$NET/$ALG/
	OUTPUT_DIR=/home/amaury/evaluation/$TYPE_GRAPH/$NET/$ALG/
	############################################################################################################
	mkdir -p $OUTPUT_DIR
	V=10	#Parâmetro do COPRA
	echo
	echo "Calculando $METRIC para a rede $NET"
	echo
	echo "Os arquivos serão armazenados em: $OUTPUT_DIR"
	for ((THRESHOLD=1; THRESHOLD<=$V; THRESHOLD++)); do
		i=0 		#Ponteiro para o ego
		echo "Os arquivos serão armazenados em: $OUTPUT_DIR"
		e=0		#Quantidade de arquivos compativeis... Alguns arquivos para algumas variações do parâmetro V não foram obtidos.
		for file in `ls $COMMUNITIES$THRESHOLD`; do
			let i=$i+1;
			if [ -e "$COMMUNITIES$THRESHOLD/$file" ] ; then
				echo "Calculando $METRIC para o ego: $i"
				/home/amaury/algoritmos/Metricas/mutual3/mutual $COMMUNITIES$THRESHOLD/$file $GROUND_TRUTH$file >> $OUTPUT_DIR$THRESHOLD".txt"
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

instructions()
{
	#PARÂMETROS $DESCRIPTION $TYPE_GRAPH $NET $METRIC
	clear
	echo "###############################################################"
	echo "																					"
	echo " Algoritmo para cálculo da métrica $METRIC - versão BATCH"
	echo "																					"
	echo "###############################################################"
	echo
	echo " 01 - COPRA"
	echo	
	echo -n "Informe o algoritmo que gerou as comunidades para que seja calculada a métrica: "
	read op2
	case $op2 in
	01)ALG=copra
		copra $1 $2 $3 $4 $ALG
		;;

	*) echo
		echo "Opção Inválida! Saindo do script..."
		echo
		exit
		;;
	esac
}
############################################################################################################
echo "###############################################################"
echo "																					"
echo " Algoritmo para cálculo da métrica $METRIC - versão BATCH"
echo "																					"
echo "###############################################################"
echo
echo " 01) Rede N1 - Follow"
echo " 02) Rede N2 - Retweets"
echo " 03) Rede N3 - Likes"
echo " 04) Rede N4 - Mentions"
echo " 09) Rede N9 - Followers"
echo
echo " 05) Rede N5 - Co-Follow"
echo " 06) Rede N6 - Co-Retweets"
echo " 07) Rede N7 - Co-Likes"
echo " 08) Rede N8 - Co-Mentions"
echo " 10) Rede N10 - Co-Followers"
echo
echo -n "Escolha uma opção: "
read op
echo
###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
case $op in

01)DESCRIPTION="Follow"	
	NET="n1"
	;;

02)DESCRIPTION="Retweets"
	NET="n2"
	;;

03)DESCRIPTION="Likes"
	NET="n3"
	;;

04)DESCRIPTION="Mentions"
	NET="n4"
	;;

05)DESCRIPTION="Co-Follow"
	NET="n5"
	;;

06)DESCRIPTION="Co-Retweets"
	NET="n6"
	;;

07)DESCRIPTION="Co-Likes"
	NET="n7"
	;;

08)DESCRIPTION="Co-Mentions"
	NET="n8"
	;;

09)DESCRIPTION="Followers"
	NET="n9"
	;;

10)DESCRIPTION="Co-Followers"
	NET="n10"
	;;

*) echo
	echo "Opção Inválida! Saindo do script..."
	echo
	exit
	;;
esac

echo "###############################################################"
echo "Utilizar grafo:" 
echo " 01 - SEM ego (Padrão)"
echo " 02 - COM o ego"
echo
echo -n "Escolha uma opção: "
read ego

if [ -z $ego ]; then
	TYPE_GRAPH="graphs_without_ego"
elif [ $ego == 02 ]; then
	TYPE_GRAPH="graphs_with_ego"
else
	TYPE_GRAPH="graphs_without_ego"
fi

#Execução do algoritmo...
###############################################################
instructions $DESCRIPTION $TYPE_GRAPH $NET $METRIC
