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