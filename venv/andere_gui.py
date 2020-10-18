from tkinter import *
from tkinter import ttk
import random
#from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title('Spiel')
root.geometry('900x900')


def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children)!=0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap,
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=150, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

#frame sachen
title = ttk.Label(frame, text='Bisimulation Game for NHF')
chose_player_label = ttk.Label(frame, text='Choose player')
player_chose_spoiler = ttk.Radiobutton(frame, text='Spoiler')
player_chose_duplicator = ttk.Radiobutton(frame, text='Duplicator')
start_game_button = ttk.Button(frame, text='Start Game')
reset_game_button = ttk.Button(frame, text='Reset Game')
exit_game_button = ttk.Button(frame, text='Exit Game')

# content Sachen
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")


content.grid(column=0, row=0, columnspan=3, rowspan= 2, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)
title.grid(row=0, padx=20, pady=20)
chose_player_label.grid(row=1, column=0, padx=20, pady=20, sticky='W')
player_chose_duplicator.grid(row=2, column=0, padx=20, sticky='W')
player_chose_spoiler.grid(row=3, column=0, padx=20, sticky='W')
start_game_button.grid(row=4, column=0, pady=20, padx=20, sticky='W')
reset_game_button.grid(row=4, column=1, pady=20, padx=20, sticky='E')
exit_game_button.grid(row=5, pady=20, padx=20, sticky='NEWS')


root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=3)
content.columnconfigure(4, weight=3)
content.rowconfigure(1, weight=1)

G = nx.DiGraph()
G.add_edges_from([(1,2), (1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9), (4,10),
                  (5,11), (5,12), (6,13)])

f = plt.figure(figsize=(5, 5))
canvas = FigureCanvasTkAgg(f, content)
nx.draw_networkx(G, with_label=True, node_color='green', pos=hierarchy_pos(G, 1))
#plt.show()
canvas.get_tk_widget().grid()

root.mainloop()