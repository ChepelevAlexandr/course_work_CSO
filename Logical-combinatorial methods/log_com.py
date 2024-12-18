import networkx as nx

# Loading the graph
file_path = "Logical-combinatorial methods/dolphins.gml"
dolphins_graph = nx.read_gml(file_path)

# Main characteristics of the graph
num_nodes = dolphins_graph.number_of_nodes()
num_edges = dolphins_graph.number_of_edges()

# Centrality calculation
degree_centrality = nx.degree_centrality(dolphins_graph)
betweenness_centrality = nx.betweenness_centrality(dolphins_graph)

# Top nodes by centrality
top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5]

# Clusters and components
clusters = nx.number_connected_components(dolphins_graph)
largest_cluster = max(nx.connected_components(dolphins_graph), key=len)
largest_cluster_size = len(largest_cluster)

# Output results
print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Top nodes by degree centrality:", top_degree)
print("Top nodes by betweenness centrality:", top_betweenness)
print("Number of clusters:", clusters)
print("Size of the largest cluster:", largest_cluster_size)
