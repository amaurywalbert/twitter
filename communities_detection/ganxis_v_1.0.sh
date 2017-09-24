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

case $op in
01)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Follow"
	INPUT_DIR=/home/amaury/graphs/n1/graphs/
	OUTPUT_DIR=/home/amaury/communities/n1/$algorithm/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

02)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Retweets"
	INPUT_DIR=/home/amaury/graphs/n2/graphs/
	OUTPUT_DIR=/home/amaury/communities/n2/$algorithm/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

03)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Likes"
	INPUT_DIR=/home/amaury/graphs/n3/graphs/
	OUTPUT_DIR=/home/amaury/communities/n3/$algorithm/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

04)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Mentions"
	INPUT_DIR=/home/amaury/graphs/n4/graphs/
	OUTPUT_DIR=/home/amaury/communities/n4/$algorithm/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

05)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Follow"
	INPUT_DIR=/home/amaury/graphs/n5/graphs/
	OUTPUT_DIR=/home/amaury/communities/n5/$algorithm/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

06)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Retweets"
	INPUT_DIR=/home/amaury/graphs/n6/graphs/
	OUTPUT_DIR=/home/amaury/communities/n6/$algorithm/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

07)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Likes"
	INPUT_DIR=/home/amaury/graphs/n7/graphs/
	OUTPUT_DIR=/home/amaury/communities/n7/$algorithm/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

08)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Mentions"
	INPUT_DIR=/home/amaury/graphs/n8/graphs/
	OUTPUT_DIR=/home/amaury/communities/n8/$algorithm/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

09)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Followers"
	INPUT_DIR=/home/amaury/graphs/n9/graphs/
	OUTPUT_DIR=/home/amaury/communities/n9/$algorithm/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

10)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Followers"
	INPUT_DIR=/home/amaury/graphs/n10/graphs/
	OUTPUT_DIR=/home/amaury/communities/n10/$algorithm/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

*) echo
	echo "Opção Inválida! Saindo do script..."
	echo
	;;
esac