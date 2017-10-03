#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades GANXiS_v3.0.2 para cada rede-ego
##								
## # INPUT:
##		- Redes-ego
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

op=0
clear
algorithm="ganxis"

instructions()
{
	#PARÂMETROS
	# $1 == $DESCRIPTION
	# $2 == $INPUT_DIR
	# $3 == $OUTPUT_DIR
	# $4 == $TYPE_GRAPH
	clear
	echo "###############################################################"
	echo "																					"
	echo " Algoritmo de Detecção de Comunidades $algorithm 					"
	echo "																					"
	echo "###############################################################"
	echo
	echo "[0, 0.5] - Qualquer valor no intervalo"
	echo "  1      - DEFAULT - rodar para cada valor de r ∈ {0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5}"
	echo	
	echo -n "Informe um valor para o threshold r: "
	read THRESHOLD
	echo
	echo "Detectando comunidades para a rede $1"
	echo
	echo "Os arquivos serão armazenados em: \"$3\""
	i=0

	for file in `ls $2`
		do
			let i=$i+1;
			echo "Detectando comunidades para o ego: $i"
			INPUT_FILE=$2$file
			OUTPUT_FILES=$3$THRESHOLD"/"$file
			mkdir -p $OUTPUT_FILES
			TYPE_GRAPH=$4
			ganxis $INPUT_FILE $OUTPUT_FILES $TYPE_GRAPH $THRESHOLD
		done
	echo
	echo -n "Script Finalizado!"
}
	
ganxis()
{
#GANXiSw 3.0.2(used to be SLPAw) is for weighted (directed) networks, version=3.0.2
#Usage: java -jar GANXiSw.jar -i networkfile
#Options:
#  -i input network file
#  -d output director (default: output)
#  -L set to 1 to use only the largest connected component
#  -t maximum iteration (default: 100)
#  -run number of repetitions
#  -r a specific threshold in [0,0.5]
#  -ov set to 0 to perform disjoint detection
#  -W treat the input as a weighted network, set 0 to ignore the weights(default 1)
#  -Sym set to 1 to make the edges symmetric/bi-directional (default 0)
#  -seed user specified seed for random generator
#  -help to display usage info
# -----------------------------Advanced Parameters---------------------------------
#  -v weighted version in {1,2,3}, default=3
#  -Oov set to 1 to output overlapping file, default=0
#  -Onc set to 1 to output <nodeID communityID> format, 2 to output <communityID nodeID> format
#  -minC min community size threshold, default=2
#  -maxC max community size threshold
#  -ev embedded SLPAw's weighted version in {1,2,3}, default=1
#  -loopfactor determine the num of loops for depomposing each large com, default=1.0
#  -Ohis1 set to 1 to output histgram Level1
#  -Ohis2 set to 1 to output histgram Level2
#
#  -OMem1 set to 1 to output each node's memory content at Level 1
#  -EC evolution cutoff, a real value > 1.0 
#NOTE: 1. more parameters refer to Readme.pdf
#      2. parameters are *CASE-SENSITIVE*, e.g., -Onc is not -onc
##############################################################################################################
	echo
	echo
	echo "INPUT_FILE: $1"
	echo "OUTPUT_DIR: $2"
	echo "THRESHOLD: $4"
	R1=$(echo "$4 >= 0" | bc)
	R2=$(echo "$4 <= 0.5" | bc)
	if [ $R1 == 1 ] && [ $R2 == 1 ]; then
		if [ $3 == "D" ]; then
			echo "TYPE_GRAPH: DIRECTED - $3"
			java -jar /home/amaury/algoritmos/LabelPropagation/GANXiS_v3.0.2/GANXiS_v3.0.2/GANXiSw.jar -i $1 -d $2 -r $4
		else
			echo "TYPE_GRAPH: UNDIRECTED - $3"			
			java -jar /home/amaury/algoritmos/LabelPropagation/GANXiS_v3.0.2/GANXiS_v3.0.2/GANXiSw.jar -i $1 -Sym 1 -d $2 -r $4
		fi
	else
		if [ $3 == "D" ]; then
			echo "TYPE_GRAPH: DIRECTED - $3"
			java -jar /home/amaury/algoritmos/LabelPropagation/GANXiS_v3.0.2/GANXiS_v3.0.2/GANXiSw.jar -i $1 -d $2
		else
			echo "TYPE_GRAPH: UNDIRECTED - $3"			
			java -jar /home/amaury/algoritmos/LabelPropagation/GANXiS_v3.0.2/GANXiS_v3.0.2/GANXiSw.jar -i $1 -Sym 1 -d $2
		fi
	fi
	echo
	echo		 
}

echo "###############################################################"
echo "																					"
echo " Algoritmo de Detecção de Comunidades $algorithm 					"
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
echo "###############################################################"
echo "Utilizar grafo:" 
echo " 01 - SEM ego (Padrão)"
echo " 02 - COM o ego"
echo
echo -n "Escolha uma opção: "
read ego

if [ -z $ego ]; then
	GRAPH="graphs_without_ego"
elif [ $ego == 02 ]; then
	GRAPH="graphs_with_ego"
else
	GRAPH="graphs_without_ego"
fi
###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
case $op in

01)DESCRIPTION="Follow"	
	TYPE_GRAPH="D"
	NET="n1"
	;;

02)DESCRIPTION="Retweets"
	TYPE_GRAPH="D"	
	NET="n2"
	;;

03)DESCRIPTION="Likes"
	TYPE_GRAPH="D"	
	NET="n3"
	;;

04)DESCRIPTION="Mentions"
	TYPE_GRAPH="D"
	NET="n4"
	;;

05)DESCRIPTION="Co-Follow"
	TYPE_GRAPH="U"
	NET="n5"
	;;

06)DESCRIPTION="Co-Retweets"
	TYPE_GRAPH="U"	
	NET="n6"
	;;

07)DESCRIPTION="Co-Likes"
	TYPE_GRAPH="U"	
	NET="n7"
	;;

08)DESCRIPTION="Co-Mentions"
	TYPE_GRAPH="U"
	NET="n8"
	;;

09)DESCRIPTION="Followers"
	TYPE_GRAPH="D"
	NET="n9"
	;;

10)DESCRIPTION="Co-Followers"
	TYPE_GRAPH="U"
	NET="n10"
	;;

*) echo
	echo "Opção Inválida! Saindo do script..."
	echo
	;;
esac
INPUT_DIR=/home/amaury/graphs/$NET/$GRAPH/
OUTPUT_DIR=/home/amaury/communities/$NET/$algorithm/$GRAPH/

#Execução do algoritmo...
###############################################################
instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH