#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades Greedy Clique Expansion para cada rede-ego
##								
## # INPUT:
##		- Redes-ego
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

op=0
clear
algorithm="gce"

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
	echo "#Community finder. Processes graph in undirected, unweighted form. Edgelist must be two values separated with non digit character."
	echo	
	echo "Detectando comunidades para a rede $1"
	echo
	echo "Os arquivos serão armazenados em: \"$3\""
	i=0

	OUTPUT_DIR=$3"default/"
	mkdir -p $OUTPUT_DIR"/"
	
	for file in `ls $2`
		do
			let i=$i+1;
			echo "Detectando comunidades para o ego: $i"
			INPUT_FILE=$2$file
			TYPE_GRAPH=$4
			
			gce $INPUT_FILE $OUTPUT_DIR $TYPE_GRAPH $file
		done
	echo
	echo -n "Script Finalizado!"
}
	
gce()
{
#Greedy Clique Expansion Community Finder
#Community finder. Requires edge list of nodes. Processes graph in undirected, unweighted form. Edgelist must be two values separated with non digit character.
#
#Use with either full (if specify all 5) or default (specify just graph file) parameters:
#Full parameters are:

# 1 - The name of the file to load
# 2 - The minimum size of cliques to use as seeds. Recommend 4 as default, unless particularly small communities are required (in which case use 3).
# 3 - The minimum value for one seed to overlap with another seed before it is considered sufficiently overlapping to be discarded (eta). 1 is complete overlap. However smaller values may be used to prune seeds more aggressively. A value of 0.6 is recommended.
# 4 - The alpha value to use in the fitness function greedily expanding the seeds. 1.0 is recommended default. Values between .8 and 1.5 may be useful. As the density of edges increases, alpha may need to be increased to stop communities expanding to engulf the whole graph. If this occurs, a warning message advising that a higher value of alpha be used, will be printed.
# 5 - The proportion of nodes (phi) within a core clique that must have already been covered by other cliques, for the clique to be 'sufficiently covered' in the Clique Coveage Heuristic
#
#Usage: ./GCECommunityFinderUbuntu910 graphfilename minimumCliqueSizeK overlapToDiscardEta fitnessExponentAlpha CCHthresholdPhi
#
#Usage (with defaults): ./GCECommunityFinderUbuntu910 graphfilename
#This will run with the default values of: minimumCliqueSizeK 4, overlapToDiscardEta 0.6, fitnessExponentAlpha 1.0, CCHthresholdPhi .75
#Communities will be output, one community per line, with the same numbering as the original nodes were provided.

##############################################################################################################
	echo
	echo
	echo "OUTPUT_DIR: $2"
	echo "TYPE_GRAPH: $3"
	cd /home/amaury/algoritmos/LocalExpansion/GCECommunityFinder/
	./GCECommunityFinderUbuntu910 $1 4 0.6 1.5 0.75 > $2$file".communities"
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