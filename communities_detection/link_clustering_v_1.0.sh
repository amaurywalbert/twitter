#!/bin/bash
######################################################################################################################################################################
##		Status - Versão 1 - Rodar o algoritmo de detecção de comunidades LinkCommunity para cada rede-ego
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
	clear
	echo "###############################################################"
	echo "																					"
	echo " Algoritmo de Detecção de Comunidades Link Community (Clustering)	"
	echo "																					"
	echo "###############################################################"
	echo
	echo "Threshold to cut the dendrogram"
	echo	
	echo -n "Informe um valor para o threshold (optional): "
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

			if [ -z $THRESHOLD ]; then
				OUTPUT_FILES=$3"default/"$file
			else
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
#    usage = "usage: python %prog [options] filename"
#    description = """The link communities method of Ahn, Bagrow, and Lehmann, Nature, 2010:
#    www.nature.com/nature/journal/v466/n7307/full/nature09182.html (doi:10.1038/nature09182)
#    """
#    epilog = """
#    
#Input:
#  An edgelist file where each line represents an edge:
#    node_i <delimiter> node_j <newline>
#  if unweighted, or
#    node_i <delimiter> node_j <delimiter> weight_ij <newline>
#  if weighted.
#    
#Output: 
#  Three text files with extensions .edge2comm.txt, .comm2edges.txt,
#  and .comm2nodes.txt store the communities.
# 
#  edge2comm, an edge on each line followed by the community
#  id (cid) of the edge's link comm:
#    node_i <delimiter> node_j <delimiter> cid <newline>
#  
#  comm2edges, a list of edges representing one community per line:
#    cid <delimiter> ni,nj <delimiter> nx,ny [...] <newline>
#
#  comm2nodes, a list of nodes representing one community per line:
#    cid <delimiter> ni <delimiter> nj [...] <newline>
#  
#  The output filename contains the threshold at which the dendrogram
#  was cut, if applicable, or the threshold where the maximum
#  partition density was found, and the value of the partition 
#  density.
#  
#  If no threshold was given to cut the dendrogram, a file ending with
#  `_thr_D.txt' is generated, containing the partition density as a
#  function of clustering threshold.
#
#  If the dendrogram option was given, two files are generated. One with
#  `.cid2edge.txt' records the id of each edge and the other one with
#  `.linkage.txt' stores the linkage structure of the hierarchical 
#  clustering. In the linkage file, the edge in the first column is 
#  merged with the one in the second at the similarity value in the 
#  third column.
#"""
#    parser = MyParser(usage, description=description,epilog=epilog)
#    parser.add_option("-d", "--delimiter", dest="delimiter", default="\t",
#                      help="delimiter of input & output files [default: tab]")
#    parser.add_option("-t", "--threshold", dest="threshold", type="float", default=None,
#                      help="threshold to cut the dendrogram (optional)")
#    parser.add_option("-w", "--weighted", dest="is_weighted", action="store_true", default=False,
#                    help="is the network weighted?")
#    parser.add_option("-r", "--record-dendrogram", dest="dendro_flag", action="store_true", 
#                      default=False, help="recording the whole dendrogram (optional)")
##############################################################################################################
	echo
	echo
	echo "INPUT_FILE: $1"
	echo "OUTPUT_DIR: $2"

	if [ -z $THRESHOLD ]; then
		echo "Sem THRESHOLD definido..."
		if [ $3 == "D" ]; then
			echo "TYPE_GRAPH: DIRECTED - $3"
			python /home/amaury/algoritmos/LinkCommunity/link_clustering.py -w $1
		else
			echo "TYPE_GRAPH: UNDIRECTED - $3"
			python /home/amaury/algoritmos/LinkCommunity/link_clustering.py -w $1 ## ESTUDAR O ALGORITMO PRA VER A QUESTÃO DO PESO E DIFERENÇA ENTRE DIRECIONADO E NÃO DIRECIONADO

		fi
	else
		echo "THRESHOLD: $4"
		if [ $3 == "D" ]; then
			echo "TYPE_GRAPH: DIRECTED - $3"
			python /home/amaury/algoritmos/LinkCommunity/link_clustering.py -t -w $1
		else
			echo "TYPE_GRAPH: UNDIRECTED - $3"			
			python /home/amaury/algoritmos/LinkCommunity/link_clustering.py -t -w $1 ## ESTUDAR O ALGORITMO PRA VER A QUESTÃO DO PESO E DIFERENÇA ENTRE DIRECIONADO E NÃO DIRECIONADO
		fi
	fi
	echo
	echo		 
}

echo "###############################################################"
echo "																					"
echo " Algoritmo de Detecção de Comunidades Link Community (Clustering)	"
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
	OUTPUT_DIR=/home/amaury/communities/n1/link/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

02)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Retweets"
	INPUT_DIR=/home/amaury/graphs/n2/graphs/
	OUTPUT_DIR=/home/amaury/communities/n2/link/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

03)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Likes"
	INPUT_DIR=/home/amaury/graphs/n3/graphs/
	OUTPUT_DIR=/home/amaury/communities/n3/link/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

04)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Mentions"
	INPUT_DIR=/home/amaury/graphs/n4/graphs/
	OUTPUT_DIR=/home/amaury/communities/n4/link/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

05)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Follow"
	INPUT_DIR=/home/amaury/graphs/n5/graphs/
	OUTPUT_DIR=/home/amaury/communities/n5/link/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

06)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Retweets"
	INPUT_DIR=/home/amaury/graphs/n6/graphs/
	OUTPUT_DIR=/home/amaury/communities/n6/link/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

07)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Likes"
	INPUT_DIR=/home/amaury/graphs/n7/graphs/
	OUTPUT_DIR=/home/amaury/communities/n7/link/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

08)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Mentions"
	INPUT_DIR=/home/amaury/graphs/n8/graphs/
	OUTPUT_DIR=/home/amaury/communities/n8/link/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

09)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Followers"
	INPUT_DIR=/home/amaury/graphs/n9/graphs/
	OUTPUT_DIR=/home/amaury/communities/n9/link/
	TYPE_GRAPH="D"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

10)clear
	###############################################################  LINHAS A SEREM MODIFICADAS DE ACORDO COM A REDE-EGO
	DESCRIPTION="Co-Followers"
	INPUT_DIR=/home/amaury/graphs/n10/graphs/
	OUTPUT_DIR=/home/amaury/communities/n10/link/
	TYPE_GRAPH="U"
	###############################################################
	instructions $DESCRIPTION $INPUT_DIR $OUTPUT_DIR $TYPE_GRAPH
	;;

*) echo
	echo "Opção Inválida! Saindo do script..."
	echo
	;;
esac