import calculate_uc_dynamically as ucd
import process_input as pi
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import algorithm as alg
from time import time, sleep

# system 1 :
intermediate_node_list = [('s1', 't1', 'v1'), ('s1', 'u1', 'v1'), ('s1', 't1'), ('u1', 'v1'), ('s1', 't1', 'u1'), ('s1', 't1', 'u1', 'v1'), ('t1', 'u1', 'v1'), ('s1', 'u1', 'v1'), ('s1', 'u1'), ('t1', 'u1'), ('u1',), ('u1', 'v1'), ('s1', 't1', 'u1'), ('s1', 't1', 'u1', 'v1'), ('t1', 'u1', 'v1')]
edgelist_main_states = [('s1', ('s1', 't1', 'v1')), ('s1', ('s1', 'u1', 'v1')), ('s1', ('s1', 't1')), ('s1', ('u1', 'v1')), ('s1', ('s1', 't1', 'u1')), ('s1', ('s1', 't1', 'u1', 'v1')), ('s1', ('t1', 'u1', 'v1')), ('u1', ('s1', 'u1', 'v1')), ('u1', ('s1', 'u1')), ('u1', ('t1', 'u1')), ('u1', ('u1',)), ('u1', ('u1', 'v1')), ('u1', ('s1', 't1', 'u1')), ('u1', ('s1', 't1', 'u1', 'v1')), ('u1', ('t1', 'u1', 'v1'))]
label_intermediate_states = {('s1', 't1', 'v1'): '{s1, t1, v1}', ('s1', 'u1', 'v1'): '{s1, u1, v1}', ('s1', 't1'): '{s1, t1}', ('u1', 'v1'): '{u1, v1}', ('s1', 't1', 'u1'): '{s1, t1, u1}', ('s1', 't1', 'u1', 'v1'): '{s1, t1, u1, v1}', ('t1', 'u1', 'v1'): '{t1, u1, v1}', ('s1', 'u1'): '{s1, u1}', ('t1', 'u1'): '{t1, u1}', ('u1',): '{u1}'}
label_node_main_state = {'s1': 's1', 't1': 't1', 'u1': 'u1', 'v1': 'v1'}
state_list = ['s1', 't1', 'u1', 'v1']
# syste2 :
intermediate_node_list_2 = [('t2',), ('s2', 't2')]
edgelist_main_states_2 = [('s2', ('t2',)), ('s2', ('s2', 't2'))]
label_intermediate_states_2 = {('t2',): '{t2}', ('s2', 't2'): '{s2, t2}'}
label_node_main_state_2 = {'s2': 's2', 't2': 't2'}
state_list_2 = ['s2', 't2']

root = Tk()
block = BooleanVar(root, False)
root.title('Spiel')
root.geometry('900x900')

uc_dict = {'s1': [['t1'], ['u1', 'v1']], 'u1': [['u1']], 's2': [['t2']]}
all_states = ['s1', 't1', 'u1', 'v1', 's2', 't2']
bisimulation = alg.calculate_bisimulation(uc_dict, all_states)
list_with_recently_picked_states = []

while all_states != list_with_recently_picked_states:

    def spoiler_data():
        global user_input
        user_input = input_state_player_1.get()
        instruction_label.config(text="new text")
        # wird für eine sekunde angezeigt
        root.update_idletasks()
        sleep(5)
        block.set(False)

    def dublicator_data():
        global user_input_2
        user_input_2 = input_state_player_2.get()
        instruction_label.config(text="new text")
        # wird für eine sekunde angezeigt
        root.update_idletasks()
        sleep(5)
        block.set(False)

    # hier wird glaube ich immer der gleiche Wert benutzt
    # um an die daten zu kommen muss hier der wert vom button aufgerufen werden
    # geht aber nicht direkt ohne button zu klicken
    # der code wird so durchlaufen ohne auf immer neue werte zu warten
    state_1 = user_input
    if state_1 not in all_states:
        print('Ungültiger Zustand')
        break
    state_2 = user_input_2
    if state_2 not in all_states:
        print('Ungültiger Zustand')
        break
    list_with_recently_picked_states.append(state_1)
    # erstmal checken, ob die Zustände beide NH haben
    with_nh, without_nh = alg.get_list_with_without_neighbourhoods(uc_dict, all_states)
    if (state_1 in with_nh and state_2 in without_nh) or (state_1 in without_nh and state_2 in with_nh):
        print('Nicht bisimular, weitermachen')
    if state_1 in without_nh and state_2 in without_nh:
        print('Ja, die sind bisimular, weitermachen')
    if state_1 in with_nh and state_2 in with_nh:
        print('jetzt NH wählen Spieler 1: ')
        nh_1__ = user_input
        nh_1_ = nh_1__.lstrip().split(', ')
        nh_1 = nh_1_[0]
        print(nh_1_)
        if nh_1_ not in uc_dict.get(state_1):
            print('Das ist kein NH des gewählten Zustandes')

        # hier wird direkt abgebrochen wenn die erste uc nicht dem NH entspricht
        # for item in uc_dict.get(state_1):
        #     print('item', item)
        #     if nh_1 not in item:
        #         print('Das ist kein NH des gewählten Zustandes')
        #         break
        print('jetzt NH wählen Spieler 2: ')
        nh_2__ = input('jetzt NH wählen Spieler 2: ')
        nh_2_ = nh_2__.lstrip().split(', ')
        nh_2 = nh_2_[0]
        print(nh_2_)
        # hier muss wahrscheinlich der input noch angepasst werden, vielleicht mit list()

        if nh_2_ not in uc_dict.get(state_2):
            print('Das ist kein NH des gewählten Zustandes')
            break # hier wird nur die for-Schleife beendet bis jetzt
        # jetz muss Spieler 1 in den Nh von Spieler 2 wechseln

        # hier mit for Schleife überprüfen, ob die Zustände bisimular sind bis Spieler 2 keinen mehr wählen kann
        i = 0
        for i in range(len(nh_2) - 1):
            i = i+1
            test = True
            while test:
                state_in_NH_1 = input('Spieler 1: wähle Zustand aus NH von Spieler 2 ')
                if state_in_NH_1 not in nh_2_:
                    print('Der Zustand is da nicht drin, nochmal')
                    continue
                state_in_NH_2 = input('Spieler 2: wähle Zustand aus NH von Spieler 1, der dazu bisimular ist ')
                if state_in_NH_2 not in nh_1_:
                    print('Der Zustand is da nicht drin, nochmal')
                    continue
                else:
                    test = False
            if (state_in_NH_1, state_in_NH_2) in bisimulation:
                print('Ja sind bisimular')
                continue
            else:
                print('Nicht bisimular, Spieler 1 hat gewonnen')
                continue

        # das müsste außerhalb der while Schleife stehen, wenn nach einem Zustandspaar wirklich Schluss sein soll
        print('Spiel ist zuende')
        list_with_recently_picked_states.append(state_in_NH_1)
        if list_with_recently_picked_states == all_states:
            print('Spieler 2 kann alle Zustände matchen und hat gewonnen')

# content = ttk.Frame(root, padding=(3, 3, 12, 12))
frame = ttk.Frame(root, borderwidth=5, relief="sunken", width=150, height=100)

# frame sachen

title = ttk.Label(frame, text='Bisimulation Game for NHF')
chose_player_label = ttk.Label(frame, text='Choose player')
player_chose_spoiler = ttk.Radiobutton(frame, text='Spoiler')
player_chose_duplicator = ttk.Radiobutton(frame, text='Duplicator')
label_input_player_1 = ttk.Label(frame, text='Eingabe Spoiler')
input_state_player_1 = ttk.Entry(frame)
input_nh_player_1 = ttk.Entry(frame)
label_input_player_2 = ttk.Label(frame, text='Eingabe Duplicator')
input_state_player_2 = ttk.Entry(frame)
input_nh_player_2 = ttk.Entry(frame)
instruction_label = ttk.Label(frame, text='Hier werden Anweisungen stehen')

input_confirm_button_1 = ttk.Button(frame, text='Okay!', command=spoiler_data())
input_confirm_button_2 = ttk.Button(frame, text='Okay!', command=dublicator_data())
exit_game_button = ttk.Button(frame, text='Exit Game')

# content Sachen
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
title.grid(row=0, padx=20, pady=20)
chose_player_label.grid(row=1, column=0, padx=20, pady=20, sticky='W')
player_chose_duplicator.grid(row=2, column=0, padx=20, sticky='W')
player_chose_spoiler.grid(row=3, column=0, padx=20, sticky='W')
label_input_player_1.grid(row=4, column=0, padx=20, sticky='W')
label_input_player_2.grid(row=4, column=1, pady=20, padx=20, sticky='E')
input_state_player_1.grid(row=5, column=0, padx=20, sticky='W')
input_state_player_2.grid(row=5, column=1, padx=20, sticky='E')
input_nh_player_1.grid(row=6, column=0, padx=20, sticky='W')
input_state_nh_2.grid(row=6, column=1, padx=20, sticky='E')
instruction_label.grid(row=7, padx=20, sticky='EW')

input_confirm_button_1.grid(row=8, column=0, pady=20, padx=20, sticky='W')
input_confirm_button_2.grid(row=8, column=1, pady=20, padx=20, sticky='E')
exit_game_button.grid(row=9, pady=20, padx=20, sticky='NEWS')


root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

G = nx.DiGraph()  # or DiGraph, MultiGraph, MultiDiGraph, etc

G.add_nodes_from(state_list)
G.add_edges_from(edgelist_main_states)
G.add_nodes_from(intermediate_node_list)

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
canvas.get_tk_widget().grid(column=0, row=10)

# hier jetzt die Sachen für den 2. Graph:

G_2 = nx.DiGraph()


G_2.add_nodes_from(state_list_2)
G_2.add_edges_from(edgelist_main_states_2)
G_2.add_nodes_from(intermediate_node_list_2)

# das layout muss nachdem alle Knoten und edges hinzugefügt wurden und bevor der graph gezeichnet wird gesetzt werden
pos = nx.nx_agraph.graphviz_layout(G_2, prog='circo')
# pos = nx.kamada_kawai_layout(G)
f_2 = plt.figure(figsize=(5, 5))
canvas_2 = FigureCanvasTkAgg(f_2, root)


nx.draw_networkx_nodes(G_2, pos=pos, nodelist=state_list_2, node_size=1000)
nx.draw_networkx_nodes(G_2, pos=pos, nodelist=intermediate_node_list_2, node_size=25)
nx.draw_networkx_edges(G_2, pos=pos, edgelist=edgelist_main_states_2)

nx.draw_networkx_labels(G_2, pos=pos, labels=label_node_main_state_2, font_size=7, font_family='sans-serif')
pos_attrs = {}
for node, coords in pos.items():
    pos_attrs[node] = (coords[0], coords[1] - 2)
nx.draw_networkx_labels(G_2, pos=pos_attrs, labels=label_intermediate_states_2, font_size=7, font_family='sans-serif')
# nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))

# K3 Graph zeichnen
#nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))

#plt.show()
canvas_2.get_tk_widget().grid(column=1, row=10)


root.mainloop()