import networkx as nx
from networkx.algorithms.centrality import degree_centrality, betweenness_centrality
from networkx.algorithms.community import greedy_modularity_communities

# Loading Facebook graph
file_path = "Graph Method/facebook_combined.txt"
graph = nx.read_edgelist(file_path, nodetype=int)

# Main characteristics of the graph
num_nodes = graph.number_of_nodes()
num_edges = graph.number_of_edges()

# Calculate centralities
degree_cent = degree_centrality(graph)
betweenness_cent = betweenness_centrality(graph)

# Top nodes by centrality
top_degree = sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)[:5]
top_betweenness = sorted(betweenness_cent.items(), key=lambda x: x[1], reverse=True)[:5]

# Clustering using modularity method
communities = list(greedy_modularity_communities(graph))
num_clusters = len(communities)
largest_cluster_size = max(len(cluster) for cluster in communities)

# Output results
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Top nodes by degree centrality:", top_degree)
print("Top nodes by betweenness centrality:", top_betweenness)
print(f"Number of clusters: {num_clusters}")
print(f"Size of the largest cluster: {largest_cluster_size}")
