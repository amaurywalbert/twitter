#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades OSLOM para cada rede-ego
##
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
		THRESHOLD=10	
	fi

	i=0
	OUTPUT_DIR=$3$THRESHOLD"/"
	mkdir -p $OUTPUT_DIR

	
	for file in `ls $2`
		do
			let i=$i+1;		
			IFS="." read -a file_temp <<<"$file"					# Renomear (temp) o arquivo "97197087.edge_list" para 97197087
			FILE=${file_temp[0]}	
						
			if [ -e $OUTPUT_DIR$FILE"/tp" ]; then
				echo "Arquivo $OUTPUT_DIR$FILE"/tp" já existe. Continuando..."
			else	
				echo "Detectando comunidades para o ego: $i"
				INPUT_FILE=$2$file
				TYPE_GRAPH=$4			
				
				oslom $INPUT_FILE $OUTPUT_DIR $TYPE_GRAPH $THRESHOLD $file $FILE
			fi
		done
	echo -n "Script Finalizado!"
	echo
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
	echo "OUTPUT_DIR: $2$6"
	echo "TYPE_GRAPH: $3"
	echo "THRESHOLD: $4"
	echo "file: $5"
	echo "FILE: $6"
	
	if [ $3 == "U" ]; then
		`pwd`
		/home/amaury/algoritmos/LocalExpansion/OSLOM2/oslom_undir -f $1 -w -r $4
	else
		/home/amaury/algoritmos/LocalExpansion/OSLOM2/oslom_dir -f $1 -w -r $4
	fi

	mv $1"_oslo_files" $2$6
	mv time_seed.dat $2$6
	rm tp
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
	NET="n1_3_5k"
	;;

02)DESCRIPTION="Retweets"
	TYPE_GRAPH="D"	
	NET="n2_3_5k"
	;;

03)DESCRIPTION="Likes"
	TYPE_GRAPH="D"	
	NET="n3_3_5k"
	;;

04)DESCRIPTION="Mentions"
	TYPE_GRAPH="D"
	NET="n4_3_5k"
	;;

05)DESCRIPTION="Co-Follow"
	TYPE_GRAPH="U"
	NET="n5_3_5k"
	;;

06)DESCRIPTION="Co-Retweets"
	TYPE_GRAPH="U"	
	NET="n6_3_5k"
	;;

07)DESCRIPTION="Co-Likes"
	TYPE_GRAPH="U"	
	NET="n7_3_5k"
	;;

08)DESCRIPTION="Co-Mentions"
	TYPE_GRAPH="U"
	NET="n8_3_5k"
	;;

09)DESCRIPTION="Followers"
	TYPE_GRAPH="D"
	NET="n9_3_5k"
	;;

10)DESCRIPTION="Co-Followers"
	TYPE_GRAPH="U"
	NET="n10_3_5k"
	;;

*) echo
	echo "Opção Inválida! Saindo do script..."
	echo
	;;
esac
INPUT_DIR=/home/amaury/graphs_hashmap_acima_3_5_k_alters/$NET/$GRAPH/
OUTPUT_DIR=/home/amaury/communities_hashmap_acima_3_5_k_alters/$GRAPH/$algorithm/raw/$NET/

#Execução do algoritmo...
###############################################################
instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
