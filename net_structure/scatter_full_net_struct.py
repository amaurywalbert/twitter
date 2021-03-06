# -*- coding: latin1 -*-
################################################################################################
import sys, os, os.path
import plotly.graph_objs as go
import plotly
# Create random data with numpy
import numpy as np

data_labels_full = ["NODES","EDGES","DENSITY","CLOSE CENTR","DIAMETER","CLUSTERING_COEF","NUMBER_CONNECTED_COMP","AVG_LEN_CONNECTED_COMP"]

follow_1_full = [1600.770,268773.300,0.068,0.408,4.932,0.490,1.000,1.000]
co_follow_1_full = [803.163,543688.600,0.398,0.859,2.717,0.920,1.005,0.998]
followers_1_full = [3018.188,196868.600,0.021,0.192,7.700,0.437,1.000,1.000]
co_followers_1_full = [1254.338,1097725.000,0.487,0.980,2.103,0.987,1.004,0.993]
retweets_1_full = [525.474,17073.120,0.055,0.276,7.332,0.431,1.000,1.000]
co_retweets_1_full = [469.500,45495.740,0.133,0.536,4.876,0.608,1.516,0.837]
likes_1_full = [801.842,34898.040,0.053,0.328,5.996,0.419,1.000,1.000]
co_likes_1_full = [723.854,106876.600,0.137,0.547,4.732,0.622,1.502,0.850]
mentions_1_full = [246.082,3745.432,0.057,0.261,5.728,0.518,1.000,1.000]
co_mentions_1_full = [218.878,39273.580,0.350,0.793,2.946,0.862,1.008,0.996]

follow_2_full = [1573.778,266153.600,0.067,0.345,7.250,0.418,1.302,0.892]
co_follow_2_full = [802.150,542913.600,0.398,0.858,2.746,0.919,1.007,0.997]
followers_2_full = [2490.900,193851.400,0.026,0.237,7.832,0.344,5.244,0.456]
co_followers_2_full = [1253.342,1096563.000,0.488,0.979,2.078,0.986,1.004,0.993]
retweets_2_full = [507.350,16705.880,0.057,0.256,9.086,0.355,1.190,0.932]
co_retweets_2_full = [467.774,42279.290,0.133,0.534,4.996,0.606,1.612,0.815]
likes_2_full = [784.610,34403.700,0.054,0.312,7.510,0.381,1.062,0.974]
co_likes_2_full = [721.562,106575.800,0.137,0.546,4.798,0.621,1.562,0.837]
mentions_2_full = [230.862,3615.890,0.061,0.218,7.274,0.418,1.222,0.919]
co_mentions_2_full = [218.468,39228.940,0.350,0.792,2.968,0.861,1.010,0.995]

######################################################################################## Somente Nós e Arestas
data_labels_basics = ["NODES","EDGES"]
follow_1_basics = [1600.770,268773.300]
co_follow_1_basics = [803.163,543688.600]
followers_1_basics = [3018.188,196868.600]
co_followers_1_basics = [1254.338,1097725.000]
retweets_1_basics = [525.474,17073.120]
co_retweets_1_basics = [469.500,45495.740,]
likes_1_basics = [801.842,34898.040]
co_likes_1_basics = [723.854,106876.600]
mentions_1_basics = [246.082,3745.432]
co_mentions_1_basics = [218.878,39273.580]

follow_2_basics = [1573.778,266153.600]
co_follow_2_basics = [802.150,542913.600]
followers_2_basics = [2490.900,193851.400]
co_followers_2_basics = [1253.342,1096563.000]
retweets_2_basics = [507.350,16705.880]
co_retweets_2_basics = [467.774,42279.290]
likes_2_basics = [784.610,34403.700]
co_likes_2_basics = [721.562,106575.800]
mentions_2_basics = [230.862,3615.890]
co_mentions_2_basics = [218.468,39228.940]

######################################################################################### Sem Nós e Arestas
data_labels = ["DENSITY","CLOSE CENTR","DIAMETER","CLUSTERING_COEF","NUMBER_CONNECTED_COMP","AVG_LEN_CONNECTED_COMP"]

follow_1 = [0.068,0.408,4.932,0.490,1.000,1.000]
co_follow_1 = [0.398,0.859,2.717,0.920,1.005,0.998]
followers_1 = [0.021,0.192,7.700,0.437,1.000,1.000]
co_followers_1 = [0.487,0.980,2.103,0.987,1.004,0.993]
retweets_1 = [0.055,0.276,7.332,0.431,1.000,1.000]
co_retweets_1 = [0.133,0.536,4.876,0.608,1.516,0.837]
likes_1 = [0.053,0.328,5.996,0.419,1.000,1.000]
co_likes_1 = [0.137,0.547,4.732,0.622,1.502,0.850]
mentions_1 = [0.057,0.261,5.728,0.518,1.000,1.000]
co_mentions_1 = [0.350,0.793,2.946,0.862,1.008,0.996]

follow_2 = [0.067,0.345,7.250,0.418,1.302,0.892]
co_follow_2 = [0.398,0.858,2.746,0.919,1.007,0.997]
followers_2 = [0.026,0.237,7.832,0.344,5.244,0.456]
co_followers_2 = [0.488,0.979,2.078,0.986,1.004,0.993]
retweets_2 = [0.057,0.256,9.086,0.355,1.190,0.932]
co_retweets_2 = [0.133,0.534,4.996,0.606,1.612,0.815]
likes_2 = [0.054,0.312,7.510,0.381,1.062,0.974]
co_likes_2 = [0.137,0.546,4.798,0.621,1.562,0.837]
mentions_2 = [0.061,0.218,7.274,0.418,1.222,0.919]
co_mentions_2 = [0.350,0.792,2.968,0.861,1.010,0.995]


######################################################################################### - Normalized Values
data_labels_norm = ["DENSITY","CLOSE CENTR","CLUSTERING_COEF","AVG_LEN_CONNECTED_COMP"]

follow_1_norm = [0.068,0.408,0.490,1.000]
co_follow_1_norm = [0.398,0.859,0.920,0.998]
followers_1_norm = [0.021,0.192,0.437,1.000]
co_followers_1_norm = [0.487,0.980,0.987,0.993]
retweets_1_norm = [0.055,0.276,0.431,1.000]
co_retweets_1_norm = [0.133,0.536,0.608,0.837]
likes_1_norm = [0.053,0.328,0.419,1.000]
co_likes_1_norm = [0.137,0.547,0.622,0.850]
mentions_1_norm = [0.057,0.261,0.518,1.000]
co_mentions_1_norm = [0.350,0.793,0.862,0.996]

follow_2_norm = [0.067,0.345,0.418,0.892]
co_follow_2_norm = [0.398,0.858,0.919,0.997]
followers_2_norm = [0.026,0.237,0.344,0.456]
co_followers_2_norm = [0.488,0.979,0.986,0.993]
retweets_2_norm = [0.057,0.256,0.355,0.932]
co_retweets_2_norm = [0.133,0.534,0.606,0.815]
likes_2_norm = [0.054,0.312,0.381,0.974]
co_likes_2_norm = [0.137,0.546,0.621,0.837]
mentions_2_norm = [0.061,0.218,0.418,0.919]
co_mentions_2_norm = [0.350,0.792,0.861,0.995]

#########################################################################################

# Create traces  - WITH EGO - NORM
title = "Propriedades estruturais das redes-ego em cada modelo - COM o EGO"
trace1 = go.Scatter(x = data_labels_norm,y = follow_1_norm,mode = 'lines+markers',name = 'follow')
trace2 = go.Scatter(x = data_labels_norm,y = co_follow_1_norm,mode = 'lines+markers',name = 'co_follow')
trace3 = go.Scatter(x = data_labels_norm,y = followers_1_norm,mode = 'lines+markers',name = 'followers')
trace4 = go.Scatter(x = data_labels_norm,y = co_followers_1_norm,mode = 'lines+markers',name = 'co_followers')
trace5 = go.Scatter(x = data_labels_norm,y = retweets_1_norm,mode = 'lines+markers',name = 'retweets')
trace6 = go.Scatter(x = data_labels_norm,y = co_retweets_1_norm,mode = 'lines+markers',name = 'co_retweets')
trace7 = go.Scatter(x = data_labels_norm,y = likes_1_norm,mode = 'lines+markers',name = 'likes')
trace8 = go.Scatter(x = data_labels_norm,y = co_likes_1_norm,mode = 'lines+markers',name = 'co_likes')
trace9 = go.Scatter(x = data_labels_norm,y = mentions_1_norm,mode = 'lines+markers',name = 'mentions')
trace10 = go.Scatter(x = data_labels_norm,y = co_mentions_1_norm,mode = 'lines+markers',name = 'co_mentions')

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]

layout= go.Layout(title = title,hovermode= 'closest',xaxis= dict(title= 'Métricas',ticklen= 5,zeroline= False,gridwidth=2,),yaxis=dict(title= 'Valores',ticklen= 5,gridwidth= 2,))

fig = dict(data=data, layout=layout)	
plotly.offline.plot(fig, filename="/home/amaury/Dropbox/net_structure_hashmap_statistics/scatter_full_net_struct_with_ego.html",auto_open=False)


#########################################################################################
# Create traces - WITHOUT EGO - NORM
title = "Propriedades estruturais das redes-ego em cada modelo - SEM o EGO"
trace1 = go.Scatter(x = data_labels_norm,y = follow_2_norm,mode = 'lines+markers',name = 'follow')
trace2 = go.Scatter(x = data_labels_norm,y = co_follow_2_norm,mode = 'lines+markers',name = 'co_follow')
trace3 = go.Scatter(x = data_labels_norm,y = followers_2_norm,mode = 'lines+markers',name = 'followers')
trace4 = go.Scatter(x = data_labels_norm,y = co_followers_2_norm,mode = 'lines+markers',name = 'co_followers')
trace5 = go.Scatter(x = data_labels_norm,y = retweets_2_norm,mode = 'lines+markers',name = 'retweets')
trace6 = go.Scatter(x = data_labels_norm,y = co_retweets_2_norm,mode = 'lines+markers',name = 'co_retweets')
trace7 = go.Scatter(x = data_labels_norm,y = likes_2_norm,mode = 'lines+markers',name = 'likes')
trace8 = go.Scatter(x = data_labels_norm,y = co_likes_2_norm,mode = 'lines+markers',name = 'co_likes')
trace9 = go.Scatter(x = data_labels_norm,y = mentions_2_norm,mode = 'lines+markers',name = 'mentions')
trace10 = go.Scatter(x = data_labels_norm,y = co_mentions_2_norm,mode = 'lines+markers',name = 'co_mentions')

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]

layout= go.Layout(title = title,hovermode= 'closest',xaxis= dict(title= 'Métricas',ticklen= 5,zeroline= False,gridwidth=2,),yaxis=dict(title= 'Valores',ticklen= 5,gridwidth= 2,))

fig = dict(data=data, layout=layout)	
plotly.offline.plot(fig, filename="/home/amaury/Dropbox/net_structure_hashmap_statistics/scatter_full_net_struct_without_ego.html",auto_open=False)
