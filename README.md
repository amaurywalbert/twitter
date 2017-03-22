# twitter
Coleta e manipulação de dados no Twitter
# ego_collect
Scripts para coleta de egos a partir de uma lista de seeds (coletados a partir dos trend topics). Uma lista (txt) é gerada com os ids dos egos - usuários que atendem aos requisitos mínimos para o projeto. Foram feitas duas coletas de trend topics. Além do arquivo com os ids dos egos, os scripts também geram arquivos com as listas desses usuários. Os arquivos estão no BOX. ego_collection.tar.bz2 e ego_list_collected.tar.bz2
# lists_members_collect
Scripts para coleta dos membros das listas especificadas a partir da coleta dos egos. São gerados arquivos binários identificados pelo id da lista, contendo os ids dos seus membros.
# lists_subscrbers_collect
Scripts para coleta dos inscritos das listas especificadas a partir da coleta dos egos. São gerados arquivos binários identificados pelo id da lista, contendo os ids dos seus membros.
# n1
Requisitos necessários para a criação da rede de amizade (N1). Scripts para a coleta dos amigos dos egos (que formam o conjunto de alters), e amigos dos alters. São gerados arquivos binários identificados pelos ids dos usuários. Como se tratam de um mesmo tipo de requisição (friends) todos os arquivos, dos egos e dos alters, ficam no mesmo diretório para facilitar a verificação de duplicidade durante a coleta. O distinção pode ser feita a partir da lista de egos gerados pelos scripts do diretório ego_collect. Assim, primeiro é feita a coleta dos amigos dos egos, o conjunto de arquivos gerados é copiado para um outro diretório (dos amigos dos alters) e só depois é iniciada a coleta dos amigos dos alters. Isso é feito porque o conjunto de arquivos dos amigos dos egos serão usados posteriormente na construção de outras redes.
# n2

# n3
Requisitos necessários para a criação da rede de likes (N3). Scripts para coleta dos tweets que os usuários favoritaram. Primeiramente coletemos os tweets favoritados pelo ego e depois fazemos o mesmo processo para o tweets favoritados pelos alters. Também copiamos os arquivos dos egos para a pasta dos arquivos dos alters para evitar duplicidade de coleta. Os arquivos contém os últimos 3200 tweets em formato JSON.
# n4

# n5
Requisitos necessários para a criação da rede de co-amizade (N5). Scripts para coleta dos seguidores dos alters. A partir do conjunto de amigos dos alters coletados pelos scripts do diretório n1, usamos os arquivos para servir como indices de coleta dos seguidores do alters. O conjunto de alters também será usado para a criação desta rede. São gerados arquivos binários contendo a lista de seguidores para cada alter.
# n6

# n7

# n8

# seeds_collect
Coleta dos seeds iniciais, definidos como os 100 tweets retornados pela requisição de trend topics. Os autores desses tweets são considerados como sementes para o ínício da busca dos egos (usuários que atendem certos critérios definidos pela pesquisa).
# testes
Script de testes usados durante a construção dos scripts de coleta.
# timeline_collect
Scripts para coleta dos últimos 3200 tweets postados pelos usuários. Retweets estão incluidos nesse conjunto. Inicialmente coletamos a timeline dos egos e depois faremos a coleta de acordo com o necessário. Esta tarefa passou a ser feita pelo servidor na nuvem Amazon a partir do dia 23-03-2017.
