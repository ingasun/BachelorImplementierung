import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

A = [[0, 1.51, 0, 1.71, 0],
     [0, 0, 2.11, 1.81, 2.31],
     [0, 0, 0, 1.31, 1.41],
     [0, 0, 0, 0, 1.11],
     [0, 0, 0, 0, 0]]

G = nx.from_numpy_matrix(np.matrix(A), create_using=nx.DiGraph)

#layout = nx.spring_layout(G)

nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))
plt.show()