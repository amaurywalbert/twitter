#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades OSLOM para cada rede-ego
##								
## # INPUT:
##		- Redes-ego
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

op=0
clear
algorithm="oslom"

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
	echo
	echo "-r - number of runs for the first hierarchical level. The default value is 10."
	echo	
	echo -n "Informe um valor para o threshold r: "
	read THRESHOLD	
	echo "Detectando comunidades para a rede $1"
	echo
	echo "Os arquivos serão armazenados em: \"$3\""
	i=0

	if [ -z $THRESHOLD ]; then
		OUTPUT_DIR=$3"default/"
		THRESHOLD=10
	else	
		OUTPUT_DIR=$3$THRESHOLD"/"
	fi

	mkdir -p $OUTPUT_DIR"/"
	
	for file in `ls $2`
		do
			let i=$i+1;
			echo "Detectando comunidades para o ego: $i"
			INPUT_FILE=$2$file
			TYPE_GRAPH=$4

			oslom $INPUT_FILE $OUTPUT_DIR $TYPE_GRAPH $THRESHOLD $file

		done
	echo
	echo -n "Script Finalizado!"
}
	
oslom()
{
#USAGE: ./oslom_undir -f network.dat -uw(-w)
#-uw must be used if you want to use the unweighted null model; -w otherwise.
#network.dat is the list of edges. Please look at ReadMe.pdf for more details.
#
#***************************************************************************************************************************************************
#OPTIONS
#  [-r R]:			sets the number of runs for the first hierarchical level, bigger this value, more accurate the output (of course, it takes more). Default value is 10.
#  [-hr R]:			sets the number of runs  for higher hierarchical levels. Default value is 50 (the method should be faster since the aggregated network is usually much smaller).
#  [-seed m]:			sets m equal to the seed for the random number generator. (instead of reading from time_seed.dat)
#  [-hint filename]:		takes a partition from filename. The file is expected to have the nodes belonging to the same cluster on the same line.
#  [-load filename]:		takes modules from a tp file you already got in a previous run.
#  [-t T]:			sets the threshold equal to T, default value is 0.1
#  [-singlet]:			 finds singletons. If you use this flag, the program generally finds a number of nodes which are not assigned to any module. the program will assign each node with at least one not homeless neighbor. This only applies to the lowest hierarchical level.
#  [-cp P]:			sets a kind of resolution parameter equal to P. This parameter is used to decide if it is better to take some modules or their union. Default value is 0.5. Bigger value leads to bigger clusters. P must be in the interval (0, 1).
#  [-fast]:			is equivalent to "-r 1 -hr 1" (the fastest possible execution).
#  [-infomap runs]:		calls infomap and uses its output as a starting point. runs is the number of times you want to call infomap.
#  [-copra runs]:		same as above using copra.
#  [-louvain runs]:		same as above using louvain method.
#Please look at ReadMe.pdf for a more detailed explanation.
##############################################################################################################
	echo
	echo
	echo "INPUT_FILE: $1"
	echo "OUTPUT_DIR: $2$5"_oslo_files/""
	echo "TYPE_GRAPH: $3"
	echo "THRESHOLD: $4"

	if [ $3 == "U" ]; then
		`pwd`
		/home/amaury/algoritmos/LocalExpansion/OSLOM2/oslom_undir -f $1 -w -r $4
	else
		/home/amaury/algoritmos/LocalExpansion/OSLOM2/oslom_dir -f $1 -w -r $4
	fi
	mv $1"_oslo_files" $2
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