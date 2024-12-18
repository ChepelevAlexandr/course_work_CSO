import networkx as nx

# Загрузка графа
file_path = "dolphins.gml"
dolphins_graph = nx.read_gml(file_path)

# Основные характеристики графа
num_nodes = dolphins_graph.number_of_nodes()
num_edges = dolphins_graph.number_of_edges()

# Расчет центральности
degree_centrality = nx.degree_centrality(dolphins_graph)
betweenness_centrality = nx.betweenness_centrality(dolphins_graph)

# Топ узлов по центральности
top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

# Кластеры и компоненты
clusters = nx.number_connected_components(dolphins_graph)
largest_cluster = max(nx.connected_components(dolphins_graph), key=len)
largest_cluster_size = len(largest_cluster)

# Вывод результатов
print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Top nodes by degree centrality:", top_degree)
print("Top nodes by betweenness centrality:", top_betweenness)
print("Number of clusters:", clusters)
print("Size of the largest cluster:", largest_cluster_size)
