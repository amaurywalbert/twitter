#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades CFinder-2.0.6--1448 para cada rede-ego
##								
## # INPUT:
##		- Redes-ego
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

op=0
clear

instructions()
{
	#PARÂMETROS
	# $1 == $DESCRIPTION
	# $2 == $INPUT_DIR
	# $3 == $OUTPUT_DIR
	# $4 == $TYPE_GRAPH
	# $5 == $Lower_Link_Weight_Threshold		
	echo "###############################################################"
	echo "																					"
	echo " Algoritmo de Detecção de Comunidades CFinder-2.0.6--1448		"
	echo "																					"
	echo "###############################################################"
	echo
	if [ ! -d $3 ]; then
		mkdir -p $3
	fi
	echo "Detectando comunidades para a rede $1"
	echo
	echo "Os arquivos serão armazenados em: \"$3\""
	i=0
	for file in `ls $2`
		do
			let i=$i+1;
			echo "Detectando comunidades para o ego: $i"
			#Passar argumentos para a função: input_file,output_dir,type_graph (-D ou -U)
			LOWER_LINK=$5
			INPUT_FILE=$2$file
			OUTPUT_FILES=$3"/"$LOWER_LINK"/"$file
			TYPE_GRAPH=$4
			cfinder $INPUT_FILE $OUTPUT_FILES $TYPE_GRAPH $LOWER_LINK
		done
	echo
	echo -n "Script Finalizado!"
}
	
cfinder()
{
# Usage : ./CFinder_commandline64 -i input_file 
#         by default the results will be written to an output
#         directory named after the input file with a '_files' suffix.
# Options: 
#  -i  specify input file.                       (Mandatory)
#  -l  specify licence file with full path.      (Optional)
#  -o  specify output directory.                 (Optional)
###########################################################	AJUSTAR DE ACORDO COM A QUANTIDADE DE MEMÓRIA DISPONÍVEL...
#  -w  specify lower link weight threshold.      (Optional)
#  -W  specify upper link weight threshold.      (Optional)
###########################################################
#  -d  specify number of digits when creating
#      the name of the default output directory
#      of the link weight thresholded input.     (Optional)
#  -t  specify maximal time allowed for 
#      clique search per node.                   (Optional)
###########################################################
#	TYPE_GRPAH
#  -D  search with directed method.              (Optional)
#  -U  search with un-directed method.           (Default)
#      (Declare explicitly the input and the 
#      modules to be un-directed.)
###########################################################
#  -I  search with intensity method and specify
#      the lower link weight intensity threshold
#      for the k-cliques.                        (Optional)
#  -k  specify the k-clique size.                (Optional)
#      (Advised to use it only when a 
#      link weight intensity threshold is set.)
#  -h  help. More details about these options.

	/home/amaury/algoritmos/CFinder-2.0.6--1448/CFinder_commandline64 -i $1 -o $2 $3 -l /home/amaury/algoritmos/CFinder-2.0.6--1448/licence.txt -w $4
}

echo "###############################################################"
echo "																					"
echo " Algoritmo de Detecção de Comunidades CFinder-2.0.6--1448		"
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
	OUTPUT_DIR=/home/amaury/communities/n1/cfinder/
	TYPE_GRAPH="-D"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

02)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Retweets"
	INPUT_DIR=/home/amaury/graphs/n2/graphs/
	OUTPUT_DIR=/home/amaury/communities/n2/cfinder/
	TYPE_GRAPH="-D"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

03)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Likes"
	INPUT_DIR=/home/amaury/graphs/n3/graphs/
	OUTPUT_DIR=/home/amaury/communities/n3/cfinder/
	TYPE_GRAPH="-D"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

04)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Mentions"
	INPUT_DIR=/home/amaury/graphs/n4/graphs/
	OUTPUT_DIR=/home/amaury/communities/n4/cfinder/
	TYPE_GRAPH="-D"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

05)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Follow"
	INPUT_DIR=/home/amaury/graphs/n5/graphs/
	OUTPUT_DIR=/home/amaury/communities/n5/cfinder/
	TYPE_GRAPH="-U"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

06)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Retweets"
	INPUT_DIR=/home/amaury/graphs/n6/graphs/
	OUTPUT_DIR=/home/amaury/communities/n6/cfinder/
	TYPE_GRAPH="-U"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

07)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Likes"
	INPUT_DIR=/home/amaury/graphs/n7/graphs/
	OUTPUT_DIR=/home/amaury/communities/n7/cfinder/
	TYPE_GRAPH="-U"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

08)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Mentions"
	INPUT_DIR=/home/amaury/graphs/n8/graphs/
	OUTPUT_DIR=/home/amaury/communities/n8/cfinder/
	TYPE_GRAPH="-U"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

09)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Followers"
	INPUT_DIR=/home/amaury/graphs/n9/graphs/
	OUTPUT_DIR=/home/amaury/communities/n9/cfinder/
	TYPE_GRAPH="-D"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

10)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Followers"
	INPUT_DIR=/home/amaury/graphs/n10/graphs/
	OUTPUT_DIR=/home/amaury/communities/n10/cfinder/
	TYPE_GRAPH="-U"
	###############################################################
	echo "Informe um valor para o Lower_Link_Weight_Threshold: "
	read Lower_Link_Weight_Threshold
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH $Lower_Link_Weight_Threshold
	;;

*) echo
	echo "Opção Inválida! Saindo do script..."
	echo
	;;
esac