Exemplo COM GROUND TRUTH :
	NAO ACERTA SE ARQUIVOS FOREM IGUAIS E DÁ VALORES DIFERENTES SE VARIAR A THREAD - mpirun -np 1 ./mpimetric 1 ../dataset/ground_truth1.dat ../dataset/communities1.dat

	NAO ACERTA SE ARQUIVOS FOREM IGUAIS ./pthreadmetric 4 1 ../dataset/ground_truth1.dat ../dataset/communities1.dat


Exemplo SEM GROUND TRUTH:

	VALORES INCONSISTENTES SE ALTERAR O NÚMERO DE THREADS - mpirun -np 2 ./mpimetric 0 ../dataset/15498928_communities_hashmap_copra_full_n2_2.txt ../dataset/15498928_graphs_hashmap_copra_full_n2_2.txt 0 0 	
	
	OK - ./pthreadmetric 4 0 ../dataset/15498928_communities_hashmap_copra_full_n2_2.txt ../dataset/15498928_graphs_hashmap_copra_full_n2_2.txt 0 0
