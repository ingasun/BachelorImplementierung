from tkinter import*
import random
from networkx.drawing.nx_agraph import graphviz_layout
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from grave import plot_network
from grave.style import use_attributes
from scipy.optimize import minimize
import pygraphviz as pgv


root = Tk()
root.title('Nur Graphsachen')

frame = LabelFrame(root, text='This is my frame', padx=50, pady=50)
frame.pack(padx=10, pady=10)

button = Button(frame, text='Wow')
button.pack()

state_list = ['s', 't', 'u', 'v']
label_list_states = ['s', 't', 'u', 'v']
label_node_state = dict(zip(state_list, label_list_states))
# upper_closure_list_a = [('a', 'b', 'c', 'd'), ('a', 'b', 'd'), ('a', 'b'), ('a', 'b', 'c')]
# label_list_a = [('a', 'b', 'c', 'd'), ('a', 'b', 'd'), ('a', 'b'), ('a', 'b', 'c')]
# label_dict_a = dict(zip(upper_closure_list_a, label_list_a))
# upper_closure_list_b = [('a', 'b', 'c', 'd'), ('b', 'c', 'd'), ('b', 'c'), ('a', 'b', 'c')]
# label_liste = [('a', 'b', 'c', 'd'), ('b', 'c', 'd'), ('b', 'c'), ('a', 'b', 'c')]
# label_node = dict(zip(upper_closure_list_b, label_liste))
# print(label_node)
# edge_list_b = [('b', ('a', 'b', 'c')), ('b', ('b', 'c')), ('b', ('b', 'c', 'd')), ('b', ('a', 'b', 'c', 'd')), (('b', 'c', 'd'), 'c'), (('b', 'c', 'd'), ('d')), (('a', 'b', 'c'), 'd')]
# edge_list_a = [('a', ('a', 'b', 'c', 'd')), ('a', ('a', 'b', 'd')), ('a', ('a', 'b')), ('a', ('a', 'b', 'c')), ('b', ('a', 'b', 'c')), ('b', ('b', 'c')), ('b', ('b', 'c', 'd')), ('b', ('a', 'b', 'c', 'd'))]
intermediate_states = [('s', 't', 'u'), ('t', 'v'), ('s', 't', 'v'), ('t', 'u'), ('t',), ('s', 't', 'u', 'v'), ('t', 'u', 'v'), ('s', 'u', 'v'), ('s', 't'), ('u', 'v'), ('s', 't', 'u'), ('t', 'u'), ('s', 't', 'u', 'v'), ('u',), ('s', 'u'), ('s', 'u', 'v'), ('t', 'u', 'v'), ('u', 'v')]
edge_main_states = [('s', ('s', 't', 'u')), ('s', ('t', 'v')), ('s', ('s', 't', 'v')), ('s', ('t', 'u')), ('s', ('t',)), ('s', ('s', 't', 'u', 'v')), ('s', ('t', 'u', 'v')), ('s', ('s', 'u', 'v')), ('s', ('s', 't')), ('s', ('u', 'v')), ('u', ('s', 't', 'u')), ('u', ('t', 'u')), ('u', ('s', 't', 'u', 'v')), ('u', ('u',)), ('u', ('s', 'u')), ('u', ('s', 'u', 'v')), ('u', ('t', 'u', 'v')), ('u', ('u', 'v'))]
label_intermediate = {('t',): '{t}', ('s', 't'): '{s, t}', ('u', 'v'): '{u, v}', ('s', 'u', 'v'): '{s, u, v}', ('s', 't', 'u'): '{s, t, u}', ('t', 'u'): '{t, u}', ('t', 'v'): '{t, v}', ('s', 't', 'u', 'v'): '{s, t, u, v}', ('t', 'u', 'v'): '{t, u, v}', ('s', 't', 'v'): '{s, t, v}', ('u',): '{u}', ('s', 'u'): '{s, u}'}
# edged_from_intermediate = [(('s', 't', 'u'), 't'), (('t', 'v'), 't'), (('s', 't', 'v'), 't'), (('t', 'u'), 't'), (('t',), 't'), (('s', 't', 'u', 'v'), 't'), (('t', 'u', 'v'), 't'), (('s', 't'), 't'), (('s', 't', 'u'), 'u'), (('t', 'u'), 'u'), (('s', 't', 'u', 'v'), 'u'), (('t', 'u', 'v'), 'u'), (('s', 'u', 'v'), 'u'), (('u', 'v'), 'u'), (('t', 'v'), 'v'), (('s', 't', 'v'), 'v'), (('s', 't', 'u', 'v'), 'v'), (('t', 'u', 'v'), 'v'), (('s', 'u', 'v'), 'v'), (('u', 'v'), 'v'), (('s', 't', 'u'), 's'), (('s', 't', 'u', 'v'), 's'), (('s', 'u'), 's'), (('s', 'u', 'v'), 's'), (('s', 't', 'u'), 't'), (('t', 'u'), 't'), (('s', 't', 'u', 'v'), 't'), (('t', 'u', 'v'), 't'), (('s', 't', 'u', 'v'), 'v'), (('s', 'u', 'v'), 'v'), (('t', 'u', 'v'), 'v'), (('u', 'v'), 'v')]

G = nx.DiGraph()  # or DiGraph, MultiGraph, MultiDiGraph, etc

# G.add_nodes_from(['s2', 't2', '{t2}', '{s2, t2}', 's3'])
# also man kann einen Graph mit label direkt aus der edge list zeichnen
# K3 = nx.DiGraph(edge_list_a)
# K3.add_node('{bla }')
# man könnte mit zwei for schleifen jeweils die Knoten aus Zustandsliste und upperclosureListe hinzufügen mit add..
#G.add_node('s3')
# G.add_edges_from([('s2', '{t2}'), ('s2', '{s2, t2}'), ('{t2}', 't2'), ('{s2, t2}', 't2')])

G.add_nodes_from(state_list)
G.add_edges_from(edge_main_states)
# G.add_nodes_from(intermediate_states)
# G.add_edges_from(edged_from_intermediate)

# G = nx.DiGraph([(s2), (t2), ({t2}), ({s2, t2})])
# #G.add_nodes_from([(s2), (t2), ({t2}), ({s2, t2})])
# G.add_edges_from([(s2, {t2}), (s2, {s2, t2}), ({t2}, t2), ({s2, t2}, t2)])
# das layout muss nachdem alle Knoten und edges hinzugefügt wurden und bevor der graph gezeichnet wird gesetzt werden
pos = nx.nx_agraph.graphviz_layout(G, prog='circo')
# pos = nx.kamada_kawai_layout(G)
f = plt.figure(figsize=(5, 5))

canvas = FigureCanvasTkAgg(f, root)

# with_label funktioniert so nicht
# nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes), node_color='r', node_size=50, ax=ax),
# nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes, in_nodes + out_nodes),
nx.draw_networkx_nodes(G, pos=pos, nodelist=state_list, node_size=1000)
nx.draw_networkx_nodes(G, pos=pos, nodelist=intermediate_states, node_size=25)
nx.draw_networkx_edges(G, pos=pos, edgelist=edge_main_states)
# nx.draw_networkx_edges(G, pos=pos, edgelist=edged_from_intermediate)
# raise text positions
# pos_nodes = nx.spring_layout(G)
nx.draw_networkx_labels(G, pos=pos, labels=label_node_state, font_size=7, font_family='sans-serif')
pos_attrs = {}
for node, coords in pos.items():
    pos_attrs[node] = (coords[0], coords[1] - 2)
nx.draw_networkx_labels(G, pos=pos_attrs, labels=label_intermediate, font_size=7, font_family='sans-serif')
# nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))

# K3 Graph zeichnen
#nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))

# plt.show()
canvas.get_tk_widget().pack()

root.mainloop()