# import upper_closure as uc
import calculate_uc_dynamically as ucd
import process_input as pi
import algorithm as alg
from tkinter import *
from tkinter import ttk, messagebox
# import random
# from PIL import ImageTk, Image
# import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
# from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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


list_with_all_uc_entries_2 = []

# diese Funktion bauche ich auch für den zweiten NHF
def store_all_upper_closures_2():
    global list_with_all_uc_stuff_2
    global state_list_2
    state_list_2 = input_states_2.get().split(' ')
    print(state_list_2)
    print(len(state_list_2))

    list_with_uc_content_2 = []
    for entry in list_with_all_uc_entries_2:
        list_with_uc_content_2.append(entry.get())
    print(list_with_uc_content_2)
    list_with_all_uc_stuff_2 = pi.process_input(list_with_uc_content_2)

def get_values_to_create_boxes():
    global sys_1, sys_2
    try:
        sys_1_ = int(input_entries_1.get())
        sys_2_ = int(input_entries_2.get())
    except ValueError:
        messagebox.showerror('Fehler', 'Bitte nur Ganzzahlen eingeben')
    else:
        sys_1 = int(input_entries_1.get())
        sys_2 = int(input_entries_2.get())


# Input was integers, continue as normal


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

num_1 = IntVar(frame_1, value=1)
num_2 = IntVar(frame_2, value=1)

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
v2 = StringVar(frame_1, value="u1: u1")
# noch nicht gesetzt
v3 = StringVar(frame_1, value="{}")
# eingabefelder für graph 1
input_states_text = Label(frame_1, text='Zustände für Graph 1 angeben, bitte mit Leerzeichen trennen', padx=20, pady=10)
input_states = Entry(frame_1, borderwidth=5, textvariable=default_state_string)
input_uc_text = Label(frame_1, text='Zustände mit upper closures angeben', padx=20, pady=10)
input_description = Label(frame_1, text='Dazu Zustand mit Doppelpunkt von seiner upper closure trennen', padx=20, pady=10)
input_description_line_2 = Label(frame_1, text='Mehrere upper closures mit Semicolon voneinander trennen', padx=20, pady=10)
input_example = Label(frame_1, text='z.B s1: s1, t1; u1, v1', padx=20, pady=10)

label_uc = Label(frame_1, text='Zustand mit seiner Upward Closure', pady=20)
for x in range(3, (int(number_of_states_with_uc_1) + 3)):
    uc_input = Entry(frame_1, borderwidth=5)  # , textvariable=v
    uc_input.grid(row=x, column=1, pady=5, padx=5)
    list_with_all_uc_entries.append(uc_input)


input_states_text.grid(row=0, column=0)
input_states.grid(row=0, column=1)
input_uc_text.grid(row=3, column=0, sticky='w')
input_description.grid(row=4, column=0, sticky='w')
input_description_line_2.grid(row=5, column=0, sticky='w')
input_example.grid(row=6, column=0, sticky='w')
label_uc.grid(row=2, column=1)

input_confirm_button = Button(frame_1, text='Eingabe bestätigen', command=lambda: store_all_upper_closures())
input_confirm_button.grid(row=20, pady=20)

# Eingabefelder Graph2 neu

default_state_string_2 = StringVar(frame_2, value="s2 t2")
v2 = StringVar(frame_1, value="s2: t2, t1")

# eingabefelder für graph 2
input_states_text_2 = Label(frame_2, text='Zustände für Graph 2 angeben, bitte mit Leerzeichen trennen', padx=20, pady=10)
input_states_2 = Entry(frame_2, borderwidth=5, textvariable=default_state_string_2)
input_uc_text_2 = Label(frame_2, text='Zustände mit upper closures angeben, Eingabe soll so aussehen: s1: s1, t1; u1, v1', pady=10)

label_uc_2 = Label(frame_2, text='Zustand mit seiner Upward Closure', pady=20)
for x in range(3, (int(number_of_states_with_uc_2) + 3)):
    uc_input_ = Entry(frame_2, borderwidth=5, textvariable=v2)
    uc_input_.grid(row=x, column=1, pady=5, padx=5)
    list_with_all_uc_entries_2.append(uc_input_)


input_states_text_2.grid(row=0, column=0)
input_states_2.grid(row=0, column=1)
input_uc_text_2.grid(row=3, column=0, sticky='ew')
label_uc_2.grid(row=2, column=1)

input_confirm_button_2 = Button(frame_2, text='Eingabe bestätigen', command=lambda: store_all_upper_closures_2())
input_confirm_button_2.grid(row=20, pady=20)
switch_to_next_window_button = Button(frame_2, text='Spiel starten', command=close_window)
switch_to_next_window_button.grid(row=6, column=1, pady=20)
# input_confirm_button2 = Button(frame_2, text='Eingabe bestätigen')
root.mainloop()


# hier jetzt die gesamtlisten der edges und nodes erstellen

intermediate_node_list, edgelist_main_states, label_intermediate_states, label_node_main_state = ucd.get_all_graph_stuff_for_system(state_list, list_with_all_uc_stuff) # vorher uc_input...
print(intermediate_node_list, edgelist_main_states, label_intermediate_states, label_node_main_state)
# hier wird noch mal die Funktion für den zweiten NHF aufrufen
intermediate_node_list_2, edgelist_main_states_2, label_intermediate_states_2, label_node_main_state_2 = ucd.get_all_graph_stuff_for_system(state_list_2, list_with_all_uc_stuff_2) # vorher uc_input...
print(intermediate_node_list_2, edgelist_main_states_2, label_intermediate_states_2, label_node_main_state_2)
# print('edgelist fertig', edgelist_main_states)
# print('zwischenzustände', intermediate_node_list)
# print('label', label_intermediate_states)
# print('edged from intermediate', edges_from_intermediate_states)
# todo ich brauche noch das dictionary mit zuständen und deren ucs für das Spiel
# todo hier jetzt noch die sachen für spiel dynamisch erzeugen
# dictionarys müssen gemerged werden
# merged_dict = uc_dict.update(uc_dict_2)
# ok, jetzt hab ich die Graphsachen und kann mit dem nächsten Fenster weitermachen

def get_input_spoiler():
    global spoiler_input
    spoiler_input = input_spoiler.get()
    input_spoiler.delete("0", "end")
    # print('in funktion', spoiler_input)
    var_1.set(1)


def get_input_duplicator():
    global duplicator_input
    duplicator_input = input_duplicator.get()
    input_duplicator.delete("0", "end")
    # print('in funktion', duplicator_input)
    var_2.set(1)


# die bauche ich gerade nicht
def corresponds_to_defintion(state_1_, state_2_):
    # erstmal checken, ob die Zustände beide NH haben
    with_nh, without_nh = alg.get_list_with_without_neighbourhoods(uc_dict, all_states)
    if state_1_ in with_nh and state_2_ in without_nh:
        # todo wird nicht angezeigt
        return 'spoiler won'
    if (state_1_ in without_nh and state_2_ in with_nh) or (state_1_ in without_nh and state_2_ in without_nh):
        return 'duplicator won'
    if state_1_ in with_nh and state_2_ in with_nh:
        return True


def pick_new_state(bool):
    instruction_label.config(text="Spoiler bitte neuen Zustand wählen")
    while True:
        input_confirm_button_1.wait_variable(var_1)
        state_1_ = spoiler_input
        if state_1_ not in all_states:
            instruction_label.config(text="Ungültiger Zustand, nochmal Zustand wählen Spieler 1")
            continue
        else:
            break
    instruction_label.config(text="Duplicator bitte neuen Zustand wählen")
    while True:
        input_confirm_button_2.wait_variable(var_2)
        state_2_ = duplicator_input
        if state_2_ not in all_states:
            instruction_label.config(text="Ungültiger Zustand, nochmal Zustand wählen Duplicator")
            continue
        else:
            break
    bool = False
    return state_1_, state_2_


def close_window():
    root.destroy()

root = Tk()
root.title('Spiel')
root.geometry('900x900')

# content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(root, borderwidth=5, relief="sunken", width=150, height=100)



var_1 = IntVar()
var_2 = IntVar()

label_input_player_1 = ttk.Label(frame, text='Eingabe Spoiler')
input_spoiler = ttk.Entry(frame)
label_input_player_2 = ttk.Label(frame, text='Eingabe Duplicator')
input_duplicator = ttk.Entry(frame)
instruction_label = ttk.Label(frame, text='Hier werden gleich Anweisungen stehen')
score_label = ttk.Label(frame, text='Hier wird angezeigt, ob was bisimular ist')
smart_remarks_label = ttk.Label(frame, text='Hier wird angezeigt, ob unnötig verloren, bzw schlecht gespielt')

input_confirm_button_1 = ttk.Button(frame, text='Okay!', command=get_input_spoiler)
input_confirm_button_2 = ttk.Button(frame, text='Okay!', command=get_input_duplicator)
exit_game_button = ttk.Button(frame, text='Exit Game')

frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky='S')
label_input_player_1.grid(row=4, column=0, padx=20, sticky='W')
label_input_player_2.grid(row=4, column=1, pady=20, padx=20, sticky='E')
input_spoiler.grid(row=5, column=0, padx=20, sticky='W')
input_duplicator.grid(row=5, column=1, padx=20, sticky='E')
instruction_label.grid(row=7, padx=20, sticky='EW')
score_label.grid(row=10, padx=20, sticky='EW')
smart_remarks_label.grid(row=11, padx=20, sticky='EW')

input_confirm_button_1.grid(row=8, column=0, pady=20, padx=20, sticky='W')
input_confirm_button_2.grid(row=8, column=1, pady=20, padx=20, sticky='E')
exit_game_button.grid(row=9, pady=20, padx=20, sticky='NEWS')

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
canvas_2.get_tk_widget().grid(column=1, row=10, sticky='s')

# todo das muss noch dynamisch gemacht werden
uc_dict = {'s1': [['t1'], ['u1', 'v1']], 'u1': [['u1']], 's2': [['t2']]}
all_states = ['s1', 't1', 'u1', 'v1', 's2', 't2']
bisimulation = alg.calculate_bisimulation(uc_dict, all_states)

print(bisimulation)
list_with_recently_picked_states = []


# todo auch Nh aus uc zulassen
# spiel endet, wenn duplicator nicht mit bisimularen zustand antworten kann oder Spieler 1 keinen zug machen kann

# while all_states != list_with_recently_picked_states:
instruction_label.config(text="Spoiler bitte Zustand wählen")
while True:
    input_confirm_button_1.wait_variable(var_1)
    state_1 = spoiler_input
    if state_1 not in all_states:
        instruction_label.config(text="Ungültiger Zustand, nochmal Zustand wählen Spieler 1")
        continue
    else:
        break
instruction_label.config(text="Duplicator bitte Zustand wählen")
while True:
    input_confirm_button_2.wait_variable(var_2)
    state_2 = duplicator_input
    if state_2 not in all_states:
        instruction_label.config(text="Ungültiger Zustand, nochmal Zustand wählen Duplicator")
        continue
    else:
        break
list_with_recently_picked_states.append(state_1)
    # erstmal checken, ob die Zustände beide NH haben

states_need_to_be_picked_again = False
while all_states != list_with_recently_picked_states:
    if states_need_to_be_picked_again:
        print('bin hier')
        # todo wird nicht angezeigt
        # score_label.config(text="Ja, die waren bisimular")
        # instruction_label.config(text="bin jetzt hier drin")
        pick_new_state(states_need_to_be_picked_again)
        state_1, state_2 = pick_new_state(states_need_to_be_picked_again)
    with_nh, without_nh = alg.get_list_with_without_neighbourhoods(uc_dict, all_states)
    # mache es glaube ich ohne funktion
    # corresponds_to_defintion(state_1, state_2)
    if state_1 in without_nh and state_2 in without_nh:
        # todo hier könnte dann noch das aktuelle paar und die anderen als historie angezeigt werden in einer box oder so
        # text_var = tk.StringVar
        score_label.config(text="Ja, die sind bisimular, Duplicator hat für das Paar x y gewonnen")
        # flag auf true setzen
        states_need_to_be_picked_again = True
        continue
    if (state_1 in with_nh and state_2 in without_nh) or (state_1 in without_nh and state_2 in with_nh):
        # print(state_in_NH_1, state_in_NH_2)
        input_confirm_button_1["state"] = "disabled"
        input_confirm_button_2["state"] = "disabled"
        score_label.config(text="Nicht bisimular, Spoiler hat gewonnen")
        # hier wird geprüft, ob Dublicator hätte gewinnen können
        if (state_in_NH_1, state_in_NH_2) in bisimulation:
            print('hey')
            smart_remarks_label.config(text='Die Zustände waren eigentlich bisimular!')
        # break ist hier richtig - nicht wegmachen
        break
    # macht doch keinen Sinn, weil die einfach nicht bisimular sind
    # if (state_1 in without_nh and state_2 in with_nh):
    #     print(state_in_NH_1, state_in_NH_2)
    #     score_label.config(text="Spoiler kann nicht mehr wählen, Dublicator hat gewonnen")
    #     if (state_in_NH_1, state_in_NH_2) in bisimulation:
    #         smart_remarks_label.config(text='Die Zustände waren eigentlich bisimular!')
    #
    #     break

    if state_1 in with_nh and state_2 in with_nh:
        instruction_label.config(text="jetzt NH Spoiler, sind mehrere Zustände darin, diese bitte mit Komma trennen")
        while True:
            input_confirm_button_1.wait_variable(var_1)
            nh_1__ = spoiler_input
            nh_1_ = nh_1__.lstrip().split(', ')
            nh_1 = nh_1_[0]
            print(nh_1_)
            if nh_1_ not in uc_dict.get(state_1):
                instruction_label.config(text="Das ist kein NH des gewählten Zustandes, nochmal")
                continue
            else:
                break

        # hier wird direkt abgebrochen wenn die erste uc nicht dem NH entspricht
        # for item in uc_dict.get(state_1):
        #     print('item', item)
        #     if nh_1 not in item:
        #         print('Das ist kein NH des gewählten Zustandes')
        #         break
        instruction_label.config(text="jetzt NH wählen Duplicator, sind mehrere Zustände darin, diese bitte mit Komma trennen")
        while True:
            input_confirm_button_2.wait_variable(var_2)
            nh_2__ = duplicator_input
            nh_2_ = nh_2__.lstrip().split(', ')
            nh_2 = nh_2_[0]
            # print(nh_2_)
            # hier muss wahrscheinlich der input noch angepasst werden, vielleicht mit list()
            if nh_2_ not in uc_dict.get(state_2):
                instruction_label.config(text="Das ist kein NH des gewählten Zustandes")
                continue
            else:
                break
        # jetz muss Spieler 1 in den Nh von Spieler 2 wechseln
        instruction_label.config(text="Spieler 1: wähle Zustand aus NH von Spieler 2")
        while True:
            input_confirm_button_1.wait_variable(var_1)
            state_in_NH_1 = spoiler_input
            if state_in_NH_1 not in nh_2_:
                instruction_label.config(text="Der Zustand ist da nicht drin, nochmal ")
                continue
            else:
                list_with_recently_picked_states.append(state_in_NH_1)
                break
        instruction_label.config(text="Spieler 2: wähle Zustand aus NH von Spieler 1, der dazu bisimular ist ")
        while True:
            input_confirm_button_2.wait_variable(var_2)
            state_in_NH_2 = duplicator_input
            if state_in_NH_2 not in nh_1_:
                instruction_label.config(text="Der Zustand ist da nicht drin, nochmal ")
                continue
            else:
                break
    state_1 = state_in_NH_1
    # print('state1 neu gesetzt', state_1)
    list_with_recently_picked_states.append(state_1)
    state_2 = state_in_NH_2
    continue


# G = nx.DiGraph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
#
#
#
# G.add_nodes_from(state_list)
# G.add_edges_from(edgelist_main_states)
# G.add_nodes_from(intermediate_node_list)
#
# # das layout muss nachdem alle Knoten und edges hinzugefügt wurden und bevor der graph gezeichnet wird gesetzt werden
# pos = nx.nx_agraph.graphviz_layout(G, prog='circo')
# # pos = nx.kamada_kawai_layout(G)
# f = plt.figure(figsize=(5, 5))
# canvas = FigureCanvasTkAgg(f, root)
#
# # with_label funktioniert so nicht
# # nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes), node_color='r', node_size=50, ax=ax),
# # nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes, in_nodes + out_nodes),
# nx.draw_networkx_nodes(G, pos=pos, nodelist=state_list, node_size=1000)
# nx.draw_networkx_nodes(G, pos=pos, nodelist=intermediate_node_list, node_size=25)
# nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist_main_states)
# # nx.draw_networkx_edges(G, pos=pos, edgelist=edged_from_intermediate)
# # raise text positions
# # pos_nodes = nx.spring_layout(G)
# nx.draw_networkx_labels(G, pos=pos, labels=label_node_main_state, font_size=7, font_family='sans-serif')
# pos_attrs = {}
# for node, coords in pos.items():
#     pos_attrs[node] = (coords[0], coords[1] - 2)
# nx.draw_networkx_labels(G, pos=pos_attrs, labels=label_intermediate_states, font_size=7, font_family='sans-serif')
# # nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))
#
# # K3 Graph zeichnen
# #nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))
#
# #plt.show()
# canvas.get_tk_widget().grid(column=0, row=10)
#
# # hier jetzt die Sachen für den 2. Graph:
#
# G_2 = nx.DiGraph()
#
#
# G_2.add_nodes_from(state_list_2)
# G_2.add_edges_from(edgelist_main_states_2)
# G_2.add_nodes_from(intermediate_node_list_2)
#
# # das layout muss nachdem alle Knoten und edges hinzugefügt wurden und bevor der graph gezeichnet wird gesetzt werden
# pos = nx.nx_agraph.graphviz_layout(G_2, prog='circo')
# # pos = nx.kamada_kawai_layout(G)
# f_2 = plt.figure(figsize=(5, 5))
# canvas_2 = FigureCanvasTkAgg(f_2, root)
#
#
# nx.draw_networkx_nodes(G_2, pos=pos, nodelist=state_list_2, node_size=1000)
# nx.draw_networkx_nodes(G_2, pos=pos, nodelist=intermediate_node_list_2, node_size=25)
# nx.draw_networkx_edges(G_2, pos=pos, edgelist=edgelist_main_states_2)
#
# nx.draw_networkx_labels(G_2, pos=pos, labels=label_node_main_state_2, font_size=7, font_family='sans-serif')
# pos_attrs = {}
# for node, coords in pos.items():
#     pos_attrs[node] = (coords[0], coords[1] - 2)
# nx.draw_networkx_labels(G_2, pos=pos_attrs, labels=label_intermediate_states_2, font_size=7, font_family='sans-serif')
# # nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))
#
# # K3 Graph zeichnen
# #nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))
#
# #plt.show()
# canvas_2.get_tk_widget().grid(column=1, row=10)


root.mainloop()

