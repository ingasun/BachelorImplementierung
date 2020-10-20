# import upper_closure as uc
import calculate_uc_dynamically as ucd
import process_input as pi
from tkinter import *
from tkinter import ttk
import random
#from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from PIL import ImageTk, Image


# Funktionen um an Eingaben zu kommen
def get_state_list():
    global state_list
    state_list = input_states.get().split(' ')
    print(state_list)
    # return ist unnötig
    # return state_list
#
#
# def get_uc_1():
#     global uc_1
#     uc_1_ = input_uc_1.get().split('=')
#     uc_1 = []
#     for item in uc_1_:
#         without_leading_whitespace = item.lstrip()
#         uc_1__ = without_leading_whitespace.split()
#         uc_1.append(uc_1__)
#     return uc_1
#
#
# def get_uc_2():
#     global uc_2
#     uc_2_ = input_uc_2.get().split('=')
#     uc_2 = []
#     for item in uc_2_:
#         without_leading_whitespace = item.lstrip()
#         uc_2__ = without_leading_whitespace.split()
#         uc_2.append(uc_2__)
#     return uc_2
#
#
# def get_uc_3():
#     global uc_3
#     uc_3 = input_uc_3.get()


list_with_all_uc_entries = []


def store_all_upper_closures():
    global list_with_all_uc_stuff
    global state_list
    state_list = input_states.get().split(' ')
    print(state_list)
    print(len(state_list))

    list_with_uc_content = []
    for entry in list_with_all_uc_entries:
        list_with_uc_content.append(entry.get())
    print(list_with_uc_content)
    list_with_all_uc_stuff = pi.process_input(list_with_uc_content)



# def store_all_upper_closures():
#     get_state_list()
#     get_uc_1()
#     get_uc_2()
#     get_uc_3()
#     # state_uc_dict = {}
#     # state_uc_dict.update({uc_1[0]: uc_1[1]})
#     # state_uc_dict[uc_1[0]] = uc_1[1]
#     # state_uc_dict[uc_2[0]] = uc_2[1]
#     print(uc_1)
#     #print(state_uc_dict)
#     print(uc_2)
#     list_with_all_uc_input.append(uc_1)
#     list_with_all_uc_input.append(uc_2)
#     print(list_with_all_uc_input)
#     return list_with_all_uc_input
def get_values_to_create_boxes():
    global sys_1, sys_2
    sys_1 = input_entries_1.get()
    sys_2 = input_entries_2.get()


def close_window():
    root.destroy()


# Fenster zur Bestimmung wie viele entry boxes
root = Tk()
root.title('Wieviele Zustände sind upward closed?')
root.geometry('400x400')
frame_1 = LabelFrame(root, text='Eingabe Graph 1', font=11, padx=130, pady=80)
frame_2 = LabelFrame(root, text='Eingabe Graph 2', font=11, padx=130, pady=80)
frame_1.grid(row=0, sticky='ew')
frame_2.grid(row=1, sticky='ew')

num_1 = IntVar(frame_1, value=5)
num_2 = IntVar(frame_2, value=4)

input_label_1 = Label(frame_1, text='Wieviele Zustände mit uc hat system 1?', padx=20, pady=10)
input_entries_1 = Entry(frame_1, borderwidth=5, textvariable=num_1)
input_label_2 = Label(frame_2, text='Wieviele Zustände mit uc hat system 2', padx=20, pady=10)
input_entries_2 = Entry(frame_2, borderwidth=5, textvariable=num_2)
input_confirm_button2 = Button(frame_2, text='Eingabe bestätigen', command=lambda: get_values_to_create_boxes())
switch_to_next_window_button = Button(frame_2, text='Weiter zur nächsten Eingabe', command=close_window)

input_label_1.grid(row=0, column=0)
input_entries_1.grid(row=1, column=0)
input_label_2.grid(row=2, column=0)
input_entries_2.grid(row=3, column=0)
input_confirm_button2.grid(row=6, column=0, pady=20)
switch_to_next_window_button.grid(row=7, column=0, pady=20)

root.mainloop()

number_of_states_with_uc_1 = sys_1
number_of_states_with_uc_2 = sys_2


# Eingabeseite für Graphsachen
root = Tk()
root.title('Eingabemaske Graphen')
frame_1 = LabelFrame(root, text='Eingabe Graph 1', font=11, padx=130, pady=80)
frame_2 = LabelFrame(root, text='Eingabe Graph 2', font=11, padx=130, pady=80)
frame_1.grid(row=0, sticky='ew')
frame_2.grid(row=1, sticky='ew')
root.geometry('900x850')

# 2 frames für die Eingaben
frame_1 = LabelFrame(root, text='Eingabe Graph 1', font=11, padx=130, pady=80)
frame_2 = LabelFrame(root, text='Eingabe Graph 2', font=11, padx=130, pady=80)
frame_1.grid(row=0, sticky='ew')
frame_2.grid(row=1, sticky='ew')

default_state_string = StringVar(frame_1, value="s1 t1 u1 v1")
v = StringVar(frame_1, value="s1: s1, t1; u1, v1")
v2 = StringVar(frame_1, value="u = u")
# noch nicht gesetzt
v3 = StringVar(frame_1, value="{}")
# eingabefelder für graph 1
input_states_text = Label(frame_1, text='Zustände für Graph 1 angeben, bitte mit Leerzeichen trennen', padx=20, pady=10)
input_states = Entry(frame_1, borderwidth=5, textvariable=default_state_string)
input_uc_text = Label(frame_1, text='Zustände mit upper closures angeben, Eingabe soll so aussehen: s1: s1, t1; u1, v1', pady=10)

label_uc = Label(frame_1, text='Zustand mit seiner Upward Closure', pady=20)
for x in range(3, (int(number_of_states_with_uc_1) + 3)):
    uc_input = Entry(frame_1, borderwidth=5, textvariable=v)
    uc_input.grid(row=x, column=1, pady=5, padx=5)
    list_with_all_uc_entries.append(uc_input)


input_states_text.grid(row=0, column=0)
input_states.grid(row=0, column=1)
input_uc_text.grid(row=3, column=0, sticky='ew')
label_uc.grid(row=2, column=1)

input_confirm_button = Button(frame_1, text='Eingabe bestätigen', command=lambda: store_all_upper_closures())
input_confirm_button.grid(row=20, pady=20)

# Eingabefelder Graph2
default_state_string_2 = StringVar(frame_1, value="s2 t2")
v22 = StringVar(frame_2, value="s2 = t2")
v3 = StringVar(frame_2, value="{}")
v4 = StringVar(frame_2, value="{}")
input_states_text2 = Label(frame_2, text='Zustände für Graph 1 angeben, bitte mit Leerzeichen trennen', padx=20, pady=10)
input_states2 = Entry(frame_2, borderwidth=5, textvariable=default_state_string_2)
input_uc_text2 = Label(frame_2, text='Upper Closure der Zustände angeben', pady=10)
label_states2 = Label(frame_2, text='Zustand', pady=20)
label_uc2 = Label(frame_2, text='Upward Closure', pady=20)
input_uc_1_2 = Entry(frame_2, borderwidth=5, textvariable=v22)
input_uc_2_2 = Entry(frame_2, borderwidth=5, textvariable=v3)
input_uc_3_2 = Entry(frame_2, borderwidth=5, textvariable=v4)
input_uc_state_1_2 = Entry(frame_2, width=7, borderwidth=5)
input_uc_state_2_2 = Entry(frame_2, width=7, borderwidth=5)
input_uc_state_3_2 = Entry(frame_2, width=7, borderwidth=5)

input_confirm_button2 = Button(frame_2, text='Eingabe bestätigen')
switch_to_next_window_button = Button(frame_2, text='Spiel starten', command=close_window)


input_states_text2.grid(row=0, column=0)
input_states2.grid(row=0, column=1)
input_uc_text2.grid(row=1, column=0, sticky='ew')
label_states2.grid(row=2, column=0)
label_uc2.grid(row=2, column=1)
input_uc_1_2.grid(row=3, column=1)
input_uc_2_2.grid(row=4, column=1)
input_uc_3_2.grid(row=5, column=1)
input_uc_state_1_2.grid(row=3, column=0)
input_uc_state_2_2.grid(row=4, column=0)
input_uc_state_3_2.grid(row=5, column=0)
input_confirm_button2.grid(row=6, column=0, pady=20)
switch_to_next_window_button.grid(row=6, column=1, pady=20)


# # das wird ausgeführt bevor das Fenster zu sehen ist, muss irgenwo anders hin oder in einen Thread
# state_list = get_state_list()
# print(state_list)
# # hier anstatt die Funktion aufzurufen die Sachen von return in Variable speichern
# all_upper_closures = list_with_all_uc_input
# print('was ist hier drin', all_upper_closures)
# # all_upper_closures = store_all_upper_closures()
# # hier jetzt die gesamtlisten der edges und intermediate nodes erstellen
#
# intermediate_node_list = []
# edgelist_main_states = []
# label_intermediate_states = {}
# edges_from_intermediate_states = []
#
# for sublist in all_upper_closures:
#     intermediate_node_list_sub, edgelist_main_states_sub, label_intermediate_states_sub, edges_from_intermediate_states_sub = uc.get_upper_closure_for_states(state_list, sublist)
#     # intermediate_node_list.append(intermediate_node_list_sub)
#     intermediate_node_list += intermediate_node_list_sub
#     edgelist_main_states += edgelist_main_states_sub
#     label_intermediate_states.update(label_intermediate_states_sub)
#     edges_from_intermediate_states += edges_from_intermediate_states_sub
#
# print('edgelist fertig', edgelist_main_states)
# print('zwischenzustände', intermediate_node_list)
# print('label', label_intermediate_states)
# print('edged from intermediate', edges_from_intermediate_states)

root.mainloop()


# hier jetzt die gesamtlisten der edges und nodes erstellen

intermediate_node_list, edgelist_main_states, label_intermediate_states, label_node_main_state = ucd.get_all_graph_stuff_for_system(state_list, list_with_all_uc_stuff) # vorher uc_input...

# print('edgelist fertig', edgelist_main_states)
# print('zwischenzustände', intermediate_node_list)
# print('label', label_intermediate_states)
# print('edged from intermediate', edges_from_intermediate_states)

# ok, jetzt hab ich die Graphsachen und kann mit dem nächsten Fenster weitermachen
# mal sehen wie ich die Daten da erstmal rein kriege
root = Tk()
root.title('Spiel')
root.geometry('900x900')

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
# state_list = ['s', 't', 'u', 'v']
# label_list_states = ['s', 't', 'u', 'v']
# label_node_state = dict(zip(state_list, label_list_states))
# upper_closure_list_a = [('a', 'b', 'c', 'd'), ('a', 'b', 'd'), ('a', 'b'), ('a', 'b', 'c')]
# label_list_a = [('a', 'b', 'c', 'd'), ('a', 'b', 'd'), ('a', 'b'), ('a', 'b', 'c')]
# label_dict_a = dict(zip(upper_closure_list_a, label_list_a))
# upper_closure_list_b = [('a', 'b', 'c', 'd'), ('b', 'c', 'd'), ('b', 'c'), ('a', 'b', 'c')]
# label_liste = [('a', 'b', 'c', 'd'), ('b', 'c', 'd'), ('b', 'c'), ('a', 'b', 'c')]
# label_node = dict(zip(upper_closure_list_b, label_liste))
# print(label_node)
# edge_list_b = [('b', ('a', 'b', 'c')), ('b', ('b', 'c')), ('b', ('b', 'c', 'd')), ('b', ('a', 'b', 'c', 'd')), (('b', 'c', 'd'), 'c'), (('b', 'c', 'd'), ('d')), (('a', 'b', 'c'), 'd')]
# edge_list_a = [('a', ('a', 'b', 'c', 'd')), ('a', ('a', 'b', 'd')), ('a', ('a', 'b')), ('a', ('a', 'b', 'c')), ('b', ('a', 'b', 'c')), ('b', ('b', 'c')), ('b', ('b', 'c', 'd')), ('b', ('a', 'b', 'c', 'd'))]
# intermediate_states = [('s', 't', 'u'), ('t', 'v'), ('s', 't', 'v'), ('t', 'u'), ('t',), ('s', 't', 'u', 'v'), ('t', 'u', 'v'), ('s', 'u', 'v'), ('s', 't'), ('u', 'v'), ('s', 't', 'u'), ('t', 'u'), ('s', 't', 'u', 'v'), ('u',), ('s', 'u'), ('s', 'u', 'v'), ('t', 'u', 'v'), ('u', 'v')]
# edge_main_states = [('s', ('s', 't', 'u')), ('s', ('t', 'v')), ('s', ('s', 't', 'v')), ('s', ('t', 'u')), ('s', ('t',)), ('s', ('s', 't', 'u', 'v')), ('s', ('t', 'u', 'v')), ('s', ('s', 'u', 'v')), ('s', ('s', 't')), ('s', ('u', 'v')), ('u', ('s', 't', 'u')), ('u', ('t', 'u')), ('u', ('s', 't', 'u', 'v')), ('u', ('u',)), ('u', ('s', 'u')), ('u', ('s', 'u', 'v')), ('u', ('t', 'u', 'v')), ('u', ('u', 'v'))]
# label_intermediate = {('t',): '{t}', ('s', 't'): '{s, t}', ('u', 'v'): '{u, v}', ('s', 'u', 'v'): '{s, u, v}', ('s', 't', 'u'): '{s, t, u}', ('t', 'u'): '{t, u}', ('t', 'v'): '{t, v}', ('s', 't', 'u', 'v'): '{s, t, u, v}', ('t', 'u', 'v'): '{t, u, v}', ('s', 't', 'v'): '{s, t, v}', ('u',): '{u}', ('s', 'u'): '{s, u}'}
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
G.add_edges_from(edgelist_main_states)
G.add_nodes_from(intermediate_node_list)
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
nx.draw_networkx_nodes(G, pos=pos, nodelist=intermediate_node_list, node_size=25)
nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist_main_states)
# nx.draw_networkx_edges(G, pos=pos, edgelist=edged_from_intermediate)
# raise text positions
# pos_nodes = nx.spring_layout(G)
nx.draw_networkx_labels(G, pos=pos, labels=label_node_main_state, font_size=7, font_family='sans-serif')
pos_attrs = {}
for node, coords in pos.items():
    pos_attrs[node] = (coords[0], coords[1] - 2)
nx.draw_networkx_labels(G, pos=pos_attrs, labels=label_intermediate_states, font_size=7, font_family='sans-serif')
# nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))

# K3 Graph zeichnen
#nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))

#plt.show()
canvas.get_tk_widget().grid()


root.mainloop()

