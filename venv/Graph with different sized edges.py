import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

A = [[0, 1.51, 0, 1.71, 0],
     [0, 0, 2.11, 1.81, 2.31],
     [0, 0, 0, 1.31, 1.41],
     [0, 0, 0, 0, 1.11],
     [0, 0, 0, 0, 0]]

G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.DiGraph)

layout = nx.kamada_kawai_layout(G)
labels = nx.get_edge_attributes(G, "weight")


# a list of the node labels in the right order
raw_labels = ["A1", "K2", "D3", "E4", "Z30"]
lab_node = dict(zip(G.nodes, raw_labels))
print(lab_node)

print("Degree centrality weight")
d = G.degree(weight='weight')
print(d)

large = []
small = []
for node in G:
    if d[node] > 4:
        large.append(node)
    else:
        small.append(node)

print("Small", small)
print("Large", large)

nx.draw_networkx_edges(G, layout)
nx.draw_networkx_nodes(G, layout, nodelist=large, node_size=100)
nx.draw_networkx_nodes(G, layout, nodelist=small, node_size=1500)
nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)
nx.draw_networkx_labels(G, layout, labels=lab_node, font_size=10, font_family='sans-serif')
plt.axis("off")
plt.show()