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

state_list = ['s', 't']
label_list_states = ['s', 't']
label_node_state = dict(zip(state_list, label_list_states))
upper_closure_list_a = [('t, '), ('s', 't')]
label_liste = ['{t}', '{s, t}']
label_node_intermediate = dict(zip(upper_closure_list_a, label_liste))
# mit edgelist kann theoretsich der graph komplett gezeichnet werden
print(label_node_intermediate)
edge_list_s = [('s', ('t, ')), ('s', ('s', 't'))]
edge_list_intermediate = [(('t, '), 't'), (('s', 't'), 't')]
edge_list_t = [('t', ('t, '))]

G = nx.DiGraph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_nodes_from(state_list)
G.add_nodes_from(upper_closure_list_a)
G.add_edges_from(edge_list_s)
G.add_edges_from(edge_list_intermediate)
#G.add_edges_from(edge_list_t)
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')

f = plt.figure(figsize=(5, 5))
canvas = FigureCanvasTkAgg(f, root)

# nx.draw_networkx_edges(G, pos=pos)
nx.draw_networkx_nodes(G, pos=pos, nodelist=state_list, node_size=1500)
nx.draw_networkx_nodes(G, pos=pos, nodelist=upper_closure_list_a, node_size=25)
nx.draw_networkx_edges(G, pos=pos)
nx.draw_networkx_edges(G, pos=pos, edgelist=edge_list_intermediate)
nx.draw_networkx_labels(G, pos=pos, labels=label_node_state, font_size=7, font_family='sans-serif')
nx.draw_networkx_labels(G, pos=pos, labels=label_node_intermediate, font_size=7, font_family='sans-serif')
#nx.draw_networkx(G, pos=pos, with_labels=True)
# plt.show()
canvas.get_tk_widget().pack()

root.mainloop()