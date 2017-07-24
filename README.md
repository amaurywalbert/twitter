# twitter
Coleta e manipulação de dados no Twitter
# create_folds
Arquivos temporarios contendo 03 subconjuntos dos egos coletados, usados para testes estatísticos (KS-test).

# ego_collect
Scripts para coleta de egos a partir de uma lista de seeds (coletados a partir dos trend topics). Uma lista (txt) é gerada com os ids dos egos - usuários que atendem aos requisitos mínimos para o projeto. Foram feitas duas coletas de trend topics. Além do arquivo com os ids dos egos, os scripts também geram arquivos com as LISTAS desses usuários. Os arquivos estão no BOX. ego_collection.tar.bz2 e ego_list_collected.tar.bz2
# graphs
scripts para criação dos grafos das redes.
# lists_members_collect
# ground_truth
scripts para organizar as listas dos usuários egos. 
Scripts para coleta dos membros das listas especificadas a partir da coleta dos egos. São gerados arquivos binários identificados pelo id da lista, contendo os ids dos seus membros.
# lists_subscrbers_collect
Scripts para coleta dos inscritos das listas especificadas a partir da coleta dos egos. São gerados arquivos binários identificados pelo id da lista, contendo os ids dos seus membros.
# n1
Requisitos necessários para a criação da rede de amizade (N1). Scripts para a coleta dos amigos dos egos (que formam o conjunto de alters), e amigos dos alters. São gerados arquivos binários identificados pelos ids dos usuários. Como se tratam de um mesmo tipo de requisição (friends) todos os arquivos, dos egos e dos alters, ficam no mesmo diretório para facilitar a verificação de duplicidade durante a coleta. O distinção pode ser feita a partir da lista de egos gerados pelos scripts do diretório ego_collect. Assim, primeiro é feita a coleta dos amigos dos egos, o conjunto de arquivos gerados deve ser copiado MANUALMENTE para um outro diretório (dos amigos dos alters) e só depois é iniciada a coleta dos amigos dos alters. Isso é feito porque o conjunto de arquivos dos amigos dos egos serão usados posteriormente na construção de outras redes.
# n2
Neste diretório estão os scripts necessários para a coleta da timeline dos alters da rede N2. Os alters são formados pelos autores de retweets presentes na timeline do ego. Após identificar os retweets e extrair os autores (alters), iniciamos a coleta da timeline dos alters. A entrada do script são os JSON com a timeline dos egos. Para economizar espaço, após a coleta da timeline dos alters, identificamos os retweets dos alters e a saída do script são arquivos binários contendo o ids do autores dos retweets encontrados na timeline dos alters.
# n3
Requisitos necessários para a criação da rede de likes (N3). Scripts para coleta dos tweets que os usuários favoritaram. Primeiramente coletemos os tweets favoritados pelo ego e depois fazemos o mesmo processo para o tweets favoritados pelos alters. Inicialmente coletamos tweets favoritados pelos primeiros 10.000 egos da primeira remessa (seeds) em formato JSON. Os arquivos são enormes e então separamos em outro diretório os arquivos dos 50 egos do protótipo e criamos um outro script para coletar os tweets favoritados pelos autores dos tweets que estão na lista dos egos (que na realizadade nada mais são do que o conjunto de alters da rede n3). Neste último script são gerados arquivos binários contendo apenas o id do tweet e o id do autor. Os arquivos contém os últimos 3200 tweets de cada usuário buscado.
# n4
Scripts que coletam a timeline dos alters (que são usuários mencionados pelos egos - extraídos da timeline dos egos) e identificam as menções feitas pelos alters. O conjunto de usuários extraídos dessas menções são armazenados em arquivos binários com o id do tweet que eles foram encontrados, o id do autor do tweet, e uma flag indicando se o tweet é um retweet.
# n5
Requisitos necessários para a criação da rede de co-amizade (N5). Scripts para coleta dos seguidores dos alters. A partir do conjunto de amigos dos alters coletados pelos scripts do diretório n1, usamos os arquivos para servir como indices de coleta dos seguidores do alters. O conjunto de alters também será usado para a criação desta rede. São gerados arquivos binários contendo a lista de seguidores para cada alter.
# n6
Usa-se o conjunto de seguidores dos amigos dos egos (obtidos da rede N5) para formar o conjunto de alters da rede N6 - rede de co-retweets. Coletamos então a timeline dos alters e extraimos os retweets presententes ali. Arquivos binários são gerados contendo o id do tweet (não é o id do retweet - usamos a identificação do tweet original) e o id do autor. 
# n7
Usa-se o conjunto de seguidores dos amigos dos egos (obtidos da rede N5) para formar o conjunto de alters da rede N7 - rede de co-favorites. Coletamos todos os favoritos dos alters e salvamos o id do tweet e o id do autor em arquivos binários.
# n8
Não é necessária nenhuma coleta (pelo menos por enquanto). A formação da rede N8 se dá a partir do dados já coletados para a rede N4.
# seeds_collect
Coleta dos seeds iniciais, definidos como os 100 tweets retornados pela requisição de trend topics. Os autores desses tweets são considerados como sementes para o ínício da busca dos egos (usuários que atendem certos critérios definidos pela pesquisa).
# testes
Script de testes usados durante a construção dos scripts de coleta. Também pode conter arquivos usados para verificação da integridade e estatística dos arquivos gerados. Manipulação dos arquivos coletados para facilitar o trabalho de coleta de outros scripts ou até mesmo para separar os arquivos usados pelo protótipo.
# threshold
Contem a lista de egos depois da poda com trheshold k=10 e também a lista com uma sequencia aleatória dos indices e dos IDs dos egos. Apenas os 500 primeiros egos aleatórios serão usados para a construção das redes.
# timeline_collect
Scripts para coleta dos últimos 3200 tweets postados pelos usuários. Retweets estão incluidos nesse conjunto. Inicialmente coletamos a timeline dos egos e depois faremos a coleta de acordo com o necessário. Esta tarefa passou a ser feita pelo servidor na nuvem Amazon a partir do dia 23-03-2017. A coleta foi transferida para um novo PC no LAB 255 a partir de 04-2017.
