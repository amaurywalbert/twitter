#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades COPRA para cada rede-ego
##								
## # INPUT:
##		- Redes-ego
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

op=0
clear
algorithm="copra"

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
	echo "Sets the v parameter (the maximum number of communities per vertex) of the COPRA algorithm to v. Default: v=1."
	echo "Repeats the execution r times for best modularity. Default: r=1."
	echo	
	echo -n "Informe um valor para o parâmetro v (optional): "
	read THRESHOLD
	echo -n "Informe um valor para o parâmetro r (optional): "
	read REPEAT
	echo
	echo "Detectando comunidades para a rede $1"
	echo
	echo "Os arquivos serão armazenados em: \"$3\""
	i=0

	if [ -z $THRESHOLD ]; then
		OUTPUT_DIR=$3"default/"
		THRESHOLD=1
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
			
			if [ -z $REPEAT ]; then
				REPEAT=1
			fi
			copra $INPUT_FILE $OUTPUT_DIR $TYPE_GRAPH $THRESHOLD $REPEAT $file
		done
	echo
	echo -n "Script Finalizado!"
}
	
copra()
{
#In general, to run the COPRA program:
#
#java -cp copra.jar COPRA filename [options]
#
#where options include:
#-bi filename is a bipartite network. Each edge listed in the file contains a mode-1 vertex name followed by a mode-2 vertex name, followed possibly by a weight (which will be ignored). Mode-1 and mode-2 vertices are disjoint even if they have the same names. E.g., an edge {a,a} is allowed and is not a self-edge. This option may not be used in conjunction with the “-w” option. Default: the network is unipartite; self-edges will be ignored, with a warning message.
#-w filename is a weighted network. If there are actually no weights in the file, or if all edges have the same weight (the default weight of an edge is 1), a warning message will be printed. Otherwise, the weights will be used in the clustering process and may affect the result. This option may not be used in conjunction with the “-bi” option. Default: the network is unweighted; edge weights may still appear in the file but will be ignored.
#-v v Sets the v parameter (the maximum number of communities per vertex) of the COPRA algorithm to v. Default: v=1.
#-vs v 1 v 2 Executes the COPRA algorithm with the v parameter set to v 1 , v 1 +1, ..., v 2 . If used in conjunction with the “-repeat” option, the execution is performed for each value of v.
#-prop p Limits the maximum number of iterations to p. The propagation will end as soon as the termination condition is satisfied, even if this happens after less than p iterations. Default: no limit, so the propagation will continue until the termination condition is satisfied.
#-repeat r Repeats the execution r times. If used in conjunction with the “-vs” option, for each value of v, the execution will be repeated r times. If r>1, the screen display will show the averages of the statistics, as well as the standard deviation and maximum of the modularity. Default: r=1.
#-mo Compute the overlap modularity (Nicosia et al.) of each solution. It is displayed on the screen, and used to decide which is the best solution to keep when “-repeat” is used. This is optional because the overlap modularity measure can be expensive to compute for large networks.
#-nosplit Do not split discontiguous communities into contiguous subsets. If this option is selected, the “communities” in the solution will not be valid communities.
#-extrasimplify Simplify the solution (by removing communities that are subsets of others) again after splitting discontiguous communities. This is always done anyway before the splitting, but splitting can create new communities which are subsumed by others. By default these are not removed, but they are when this option is selected. This operation is optional because its complexity is O(n 2 ), but in practice it is usually very fast and worthwhile.
#-q Do not display the description of the parameters and the network when the program starts.
##############################################################################################################
	echo
	echo
	echo "INPUT_FILE: $1"
	echo "OUTPUT_DIR: $2"
	echo "TYPE_GRAPH: $3"
	echo "THRESHOLD: $4"
	echo "REPEAT: $5"
	java -cp /home/amaury/algoritmos/LabelPropagation/COPRA/copra.jar COPRA $1 -w -v $4 -repeat $5
	mv "clusters-"$6 $2
	mv "best-clusters-"$6 $2
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