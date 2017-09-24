#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades iLCD para cada rede-ego
##								
## # INPUT:
##		- Redes-ego
## # OUTPUT:
##		- Comunidades
######################################################################################################################################################################

op=0
clear
algorithm="iLCD"

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
	echo "Size of the minimal community. Default : 3"
	echo "NOT DIRECTED - NOT WEIGHTED"
	echo	
	echo -n "Informe um valor para o tamanho mínimo da comunidade - parâmetro s (optional): "
	read THRESHOLD
	echo
	echo "Detectando comunidades para a rede $1"
	echo
	echo "Os arquivos serão armazenados em: \"$3\""
	i=0

	if [ -z $THRESHOLD ]; then
		OUTPUT_DIR=$3"default/"
		THRESHOLD=3
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

			cp $INPUT_FILE $INPUT_FILE".ncol"
			INPUT_FILE_tmp=$INPUT_FILE".ncol"

			ilcd $INPUT_FILE_tmp $OUTPUT_DIR $TYPE_GRAPH $THRESHOLD $file

			rm	$INPUT_FILE_tmp
		done
	echo
	echo -n "Script Finalizado!"
}
	
ilcd()
{
#java SampleMain [options...] arguments...
# -bThreshold N    : threshold of belonging. Default : 0.5 
# -debug           : display some debug dialogs. Default : false
# -fRatio N        : fusion of community ratio. Default : 0.5
# -i VAL           : input file
# -inputDateF VAL  : select your date formating. Default : YYYYMMDD. possibilities : YYYYMMDDHHMMSS, YYYYMMDD, NONE
# -o VAL           : file to write the output in, without extention. If not specified, same name as input file
# -outputDateF VAL : select your date formating. Default : YYYYMMDD. possibilities : YYYYMMDDHHMMSS, YYYYMMDD, NONE
# -s N             : size of the minimal community. Default : 3
# -staticN         : if true, the provided network will considered as static.
# -verbose         : display basic dialogs (number of line processed...) Default : true
##############################################################################################################
	echo
	echo
	echo "INPUT_FILE: $1"
	echo "OUTPUT_FILE: $2$5"
	echo "TYPE_GRAPH: $3"
	echo "THRESHOLD: $4"
	java -jar /home/amaury/algoritmos/LocalExpansion/iLCD/iLCD.jar -i $1 -o $2$5".tcom" -s $4
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