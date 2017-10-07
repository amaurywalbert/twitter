#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades COPRA
##					para cada rede-ego usando parametros AUTOMATICOS de 1 ate 10
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
	echo " Algoritmo de Detecção de Comunidades $algorithm - versão BATCH"
	echo "																					"
	echo "###############################################################"
	echo
	echo " - Sets the v parameter - the maximum number of communities per vertex of the COPRA algorithm."
	echo " - Nesta versão o algoritmo irá rodar num laço com threshold variando de 1 até v. Default = 10."
	echo	
	echo -n "Informe um valor para o parâmetro v (v>1): "
	read V

	echo
	echo "Detectando comunidades para a rede $1"
	echo
	echo "Os arquivos serão armazenados em: \"$3\""
	if [ -z $V ]; then
		V=10	
	fi

	for ((THRESHOLD=1; THRESHOLD<=$V; THRESHOLD++)); do 	
		i=0

		OUTPUT_DIR=$3$THRESHOLD"/"
		mkdir -p $OUTPUT_DIR"/"
	
		for file in `ls $2`
			do
				let i=$i+1;
				echo "Detectando comunidades para o ego: $i"
				INPUT_FILE=$2$file
				TYPE_GRAPH=$4
				copra $INPUT_FILE $OUTPUT_DIR $TYPE_GRAPH $THRESHOLD $file
			done
		echo
	done	
	echo -n "Script Finalizado!"
	echo
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

	java -cp /home/amaury/algoritmos/LabelPropagation/COPRA/copra.jar COPRA $1 -w -v $4 -extrasimplify
	mv "clusters-"$5 $2
#	mv "best-clusters-"$5 $2 ## Usar apenas se a opção -extrasimplify não for usada.
	echo
	echo		 
}

echo "###############################################################"
echo "																					"
echo " Algoritmo de Detecção de Comunidades $algorithm - versão BATCH"
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
OUTPUT_DIR=/home/amaury/Dropbox/communities/$algorithm/$NET/$GRAPH/

#Execução do algoritmo...
###############################################################
instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
