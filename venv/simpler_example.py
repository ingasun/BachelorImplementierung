from tkinter import*
import random
from networkx.drawing.nx_agraph import graphviz_layout
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.optimize import minimize
import pygraphviz as pgv

root = Tk()
root.title('Nur Graphsachen')

frame = LabelFrame(root, text='This is my frame', padx=50, pady=50)
frame.pack(padx=10, pady=10)

button = Button(frame, text='Wow')
button.pack()

state_list = ['a', 'b', 'c', 'd']
label_list_states = ['a', 'b', 'c', 'd']
label_node_state = dict(zip(state_list, label_list_states))
upper_closure_list_a = [('a', 'b', 'c', 'd'), ('a', 'b', 'd'), ('a', 'b'), ('a', 'b', 'c')]
label_list_a = [('a', 'b', 'c', 'd'), ('a', 'b', 'd'), ('a', 'b'), ('a', 'b', 'c')]
label_dict_a = dict(zip(upper_closure_list_a, label_list_a))
upper_closure_list_b = [('a', 'b', 'c', 'd'), ('b', 'c', 'd'), ('b', 'c'), ('a', 'b', 'c')]
label_liste = [('a', 'b', 'c', 'd'), ('b', 'c', 'd'), ('b', 'c'), ('a', 'b', 'c')]
label_node = dict(zip(upper_closure_list_b, label_liste))
edge_list_b = [('b', ('a', 'b', 'c')), ('b', ('b', 'c')), ('b', ('b', 'c', 'd')), ('b', ('a', 'b', 'c', 'd')), (('b', 'c', 'd'), 'c'), (('b', 'c', 'd'), ('d')), (('a', 'b', 'c'), 'd')]
edge_list_a = [('a', ('a', 'b', 'c', 'd')), ('a', ('a', 'b', 'd')), ('a', ('a', 'b')), ('a', ('a', 'b', 'c')), ('b', ('a', 'b', 'c')), ('b', ('b', 'c')), ('b', ('b', 'c', 'd')), ('b', ('a', 'b', 'c', 'd'))]

G = nx.DiGraph()  # or DiGraph, MultiGraph, MultiDiGraph, etc

# G.add_nodes_from(['s2', 't2', '{t2}', '{s2, t2}', 's3'])
# also man kann einen Graph mit label direkt aus der edge list zeichnen
# K3 = nx.DiGraph(edge_list_a)
# K3.add_node('{bla }')
# man könnte mit zwei for schleifen jeweils die Knoten aus Zustandsliste und upperclosureListe hinzufügen mit add..
#G.add_node('s3')
# G.add_edges_from([('s2', '{t2}'), ('s2', '{s2, t2}'), ('{t2}', 't2'), ('{s2, t2}', 't2')])

G.add_nodes_from(state_list)
G.add_nodes_from(upper_closure_list_a)
G.add_nodes_from(upper_closure_list_b)
G.add_edges_from(edge_list_a)
G.add_edges_from(edge_list_b)


# G = nx.DiGraph([(s2), (t2), ({t2}), ({s2, t2})])
# #G.add_nodes_from([(s2), (t2), ({t2}), ({s2, t2})])
# G.add_edges_from([(s2, {t2}), (s2, {s2, t2}), ({t2}, t2), ({s2, t2}, t2)])
# das layout muss nachdem alle Knoten und edges hinzugefügt wurden und bevor der graph gezeichnet wird gesetzt werden
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
# pos = nx.kamada_kawai_layout(G)
f = plt.figure(figsize=(5, 5))
canvas = FigureCanvasTkAgg(f, root)

# with_label funktioniert so nicht
# nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes), node_color='r', node_size=50, ax=ax),
# nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes, in_nodes + out_nodes),
nx.draw_networkx_nodes(G, pos=pos, nodelist=state_list, node_size=1500)
nx.draw_networkx_nodes(G, pos=pos, nodelist=upper_closure_list_a, node_size=25)
nx.draw_networkx_nodes(G, pos=pos, nodelist=upper_closure_list_b, node_size=25)
nx.draw_networkx_edges(G, pos=pos, edgelist=edge_list_b)
nx.draw_networkx_edges(G, pos=pos, edgelist=edge_list_a)
nx.draw_networkx_labels(G, pos=pos, labels=label_node_state, font_size=7, font_family='sans-serif')
nx.draw_networkx_labels(G, pos=pos, labels=label_dict_a, font_size=7, font_family='sans-serif')
nx.draw_networkx_labels(G, pos=pos, labels=label_node_state, font_size=7, font_family='sans-serif')
# nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))

# K3 Graph zeichnen
#nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))

#plt.show()
canvas.get_tk_widget().pack()

root.mainloop()