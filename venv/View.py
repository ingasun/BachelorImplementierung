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

def main():
    list_with_all_uc_entries = []


    def store_all_upper_closures():
        global list_with_all_uc_stuff
        global state_list
        global uc_dict
        global nh_state_list
        state_list = input_states.get().split(' ')
        # print(state_list)
        # print(len(state_list))

        list_with_uc_content = []
        # print('was ist in der liste?', list_with_all_uc_entries)
        for entry in list_with_all_uc_entries:
            if entry.get() is '':
                return messagebox.showwarning('Warnung', 'Die Eingabe darf nicht leer sein')
            else:
                list_with_uc_content.append(entry.get())
                list_with_all_uc_stuff, uc_dict, nh_state_list = pi.process_input(list_with_uc_content)
        # print(list_with_uc_content)



    list_with_all_uc_entries_2 = []

    # diese Funktion bauche ich auch für den zweiten NHF
    def store_all_upper_closures_2():
        global list_with_all_uc_stuff_2
        global state_list_2
        global uc_dict_2
        global nh_state_list_2
        try:
            state_list_2 = input_states_2.get().split(' ')
        except Exception:
            messagebox.showerror('Fehlerhafte Eingabe!')
        else:
            state_list_2 = input_states_2.get().split(' ')
        list_with_uc_content_2 = []
        for entry in list_with_all_uc_entries_2:
            if entry.get() is '':
                return messagebox.showwarning('Warnung', 'Die Eingabe darf nicht leer sein')
            else:
                list_with_uc_content_2.append(entry.get())
                list_with_all_uc_stuff_2, uc_dict_2, nh_state_list_2 = pi.process_input(list_with_uc_content_2)

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

    intermediate_node_list, edgelist_main_states, label_intermediate_states, label_node_main_state, dict_to_chose = ucd.get_all_graph_stuff_for_system(state_list, list_with_all_uc_stuff) # vorher uc_input...
    # print(intermediate_node_list, edgelist_main_states, label_intermediate_states, label_node_main_state)
    final_intermediate_list = [(e) for e in intermediate_node_list if e not in nh_state_list]
    # hier wird noch mal die Funktion für den zweiten NHF aufrufen
    intermediate_node_list_2, edgelist_main_states_2, label_intermediate_states_2, label_node_main_state_2, dict_to_chose_2 = ucd.get_all_graph_stuff_for_system(state_list_2, list_with_all_uc_stuff_2) # vorher uc_input...
    # print(intermediate_node_list_2, edgelist_main_states_2, label_intermediate_states_2, label_node_main_state_2)
    final_intermediate_list_2 = [(e) for e in intermediate_node_list_2 if e not in nh_state_list_2]

    # neue andersfarbige Zustände machen:
    uc_dict.values()


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
    exit_game_button = ttk.Button(frame, text='Exit Game', command=close_window)

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
    G.add_nodes_from(final_intermediate_list)
    G.add_nodes_from(nh_state_list)

    # das layout muss nachdem alle Knoten und edges hinzugefügt wurden und bevor der graph gezeichnet wird gesetzt werden
    pos = nx.nx_agraph.graphviz_layout(G, prog='circo')
    # pos = nx.kamada_kawai_layout(G)
    f = plt.figure(figsize=(5, 5))
    canvas = FigureCanvasTkAgg(f, root)

    # with_label funktioniert so nicht
    # nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes), node_color='r', node_size=50, ax=ax),
    # nx.draw_networkx_nodes(G, pos, nodelist=range(in_nodes, in_nodes + out_nodes),
    nx.draw_networkx_nodes(G, pos=pos, nodelist=state_list, node_size=1000)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=final_intermediate_list, node_size=25)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=nh_state_list, node_color='pink', node_size=25)
    nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist_main_states)
    # nx.draw_networkx_edges(G, pos=pos, edgelist=edged_from_intermediate)
    # raise text positions
    # pos_nodes = nx.spring_layout(G)
    nx.draw_networkx_labels(G, pos=pos, labels=label_node_main_state, font_size=7, font_family='sans-serif')
    pos_attrs = {}
    for node, coords in pos.items():
        pos_attrs[node] = (coords[0], coords[1] - 5)
    nx.draw_networkx_labels(G, pos=pos_attrs, labels=label_intermediate_states, font_size=9, font_family='sans-serif')
    # nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))

    # K3 Graph zeichnen
    #nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))

    #plt.show()
    canvas.get_tk_widget().grid(column=0, row=20, sticky='s')

    # hier jetzt die Sachen für den 2. Graph:

    G_2 = nx.DiGraph()


    G_2.add_nodes_from(state_list_2)
    G_2.add_edges_from(edgelist_main_states_2)
    G_2.add_nodes_from(final_intermediate_list_2)
    G_2.add_nodes_from(nh_state_list_2)

    # das layout muss nachdem alle Knoten und edges hinzugefügt wurden und bevor der graph gezeichnet wird gesetzt werden
    pos = nx.nx_agraph.graphviz_layout(G_2, prog='dot')
    # pos = nx.kamada_kawai_layout(G)
    f_2 = plt.figure(figsize=(5, 5))
    canvas_2 = FigureCanvasTkAgg(f_2, root)


    nx.draw_networkx_nodes(G_2, pos=pos, nodelist=state_list_2, node_size=1000)
    nx.draw_networkx_nodes(G_2, pos=pos, nodelist=final_intermediate_list_2, node_size=25)
    nx.draw_networkx_nodes(G_2, pos=pos, nodelist=nh_state_list_2, node_color='pink', node_size=25)
    nx.draw_networkx_edges(G_2, pos=pos, edgelist=edgelist_main_states_2)

    nx.draw_networkx_labels(G_2, pos=pos, labels=label_node_main_state_2, font_size=7, font_family='sans-serif')
    pos_attrs = {}
    for node, coords in pos.items():
        pos_attrs[node] = (coords[0], coords[1] - 2)
    nx.draw_networkx_labels(G_2, pos=pos_attrs, labels=label_intermediate_states_2, font_size=9, font_family='sans-serif')
    # nx.draw_networkx(G, with_label=True, node_color='green', pos=nx.spring_layout(G))

    # K3 Graph zeichnen
    #nx.draw_networkx(K3, with_label=True, node_color='green', pos=nx.spring_layout(K3))

    #plt.show()
    canvas_2.get_tk_widget().grid(column=1, row=20, sticky='s')

    # uc_dict = {'s1': [['t1'], ['u1', 'v1']], 'u1': [['u1']], 's2': [['t2']]}
    # print(uc_dict)
    # print(uc_dict_2)
    # print('werte aus uc_dict', uc_dict.values())
    # werte aus uc_dict dict_values([[['s1', 't1']]])
    uc_dict.update(uc_dict_2)
    dict_to_chose.update(dict_to_chose_2)
    # print(uc_dict)
    # print('merged', uc_dict)
    # print('alt', uc_dict)
    total_state_space = state_list + state_list_2
    # print('state_space', total_state_space)
    bisimulation = alg.calculate_bisimulation(uc_dict, total_state_space)

    # print(bisimulation)

    while True:
        input_confirm_button_1["state"] = "enabled"
        instruction_label.config(text="Spoiler: lege zunächst Zustände fest, auf denen gespielt werden soll.")
        while True:
            input_confirm_button_1.wait_variable(var_1)
            initial_tuple = spoiler_input.split(', ')
            # print('Länge', len(initial_tuple))
            if len(initial_tuple) != 2:
                instruction_label.config(text="Es müssen genau zwei initiale Zustände angegeben werden, bitte diese mit Komma trennen")
                continue
            if (initial_tuple[0] in total_state_space) and (initial_tuple[1] in total_state_space):
                break
            else:
                continue

        instruction_label.config(text="Spoiler bitte Zustand aus Starttupel wählen")
        while True:
            input_confirm_button_2["state"] = "disabled"
            input_confirm_button_1.wait_variable(var_1)
            state_1 = spoiler_input
            if state_1 not in total_state_space:
                instruction_label.config(text="Ungültiger Zustand, nochmal Zustand wählen Spieler 1")
                continue
            else:
                break
        # todo das erübrigt sich jetzt eigentlich, aber egal
        input_confirm_button_2["state"] = "enabled"
        instruction_label.config(text="Duplicator bitte den anderen Zustand aus Starttupel wählen")
        while True:
            input_confirm_button_1["state"] = "disabled"
            input_confirm_button_2.wait_variable(var_2)
            state_2 = duplicator_input
            if state_2 not in total_state_space:
                instruction_label.config(text="Ungültiger Zustand, nochmal einen Zustand wählen Duplicator")
                continue
            else:
                break
        input_confirm_button_1["state"] = "enabled"

        while True:
            # if states_need_to_be_picked_again:
            #     print('bin hier')
            #     # score_label.config(text="Ja, die waren bisimular")
            #     # instruction_label.config(text="bin jetzt hier drin")
            #     pick_new_state(states_need_to_be_picked_again)
            #     state_1, state_2 = pick_new_state(states_need_to_be_picked_again)
            with_nh, without_nh = alg.get_list_with_without_neighbourhoods(uc_dict, total_state_space)
            # mache es glaube ich ohne funktion
            # corresponds_to_defintion(state_1, state_2)
            if state_1 in without_nh and state_2 in without_nh:
                # text_var = tk.StringVar
                input_confirm_button_1["state"] = "disabled"
                input_confirm_button_2["state"] = "disabled"
                score_label.config(text="Ja, die sind bisimular, Duplicator hat für das Paar x y gewonnen")
                # flag auf true setzen
                # states_need_to_be_picked_again = True
                # hier kann direkt abgebrochen werden, da Dublicator gewonnen hat
                break
            if state_1 in with_nh and state_2 in without_nh:  #  or (state_1 in without_nh and state_2 in with_nh):
                # print(state_in_NH_1, state_in_NH_2)
                input_confirm_button_1["state"] = "disabled"
                input_confirm_button_2["state"] = "disabled"
                score_label.config(text="Nicht bisimular, Spoiler hat gewonnen")
                # hier wird geprüft, ob Dublicator hätte gewinnen können
                # hier brauche ich die initialen Zustände
                if (initial_tuple[0], initial_tuple[1]) in bisimulation:
                    smart_remarks_label.config(text='Die Zustände waren eigentlich bisimular!')
                # break ist hier richtig - nicht wegmachen
                break
            # macht doch keinen Sinn, weil die einfach nicht bisimular sind
            if (state_1 in without_nh and state_2 in with_nh):
                print(state_in_NH_1, state_in_NH_2)
                # todo hier noch prüfen ob wirklich bisimular
                score_label.config(text="der Spoiler kann nicht mehr wählen, Dublicator hat gewonnen")
                if (initial_tuple[0], initial_tuple[1]) not in bisimulation:
                    smart_remarks_label.config(text='Die Zustände waren eigentlich nicht bisimular!')
                # if (state_in_NH_1, state_in_NH_2) in bisimulation:
                #     smart_remarks_label.config(text='Die Zustände waren aber eigentlich nicht bisimular!')

                break

            if state_1 in with_nh and state_2 in with_nh:
                instruction_label.config(text="jetzt NH wählen Spoiler, sind mehrere Zustände darin, diese bitte mit Komma trennen")
                while True:
                    input_confirm_button_1.wait_variable(var_1)
                    nh_1__ = spoiler_input
                    nh_1_ = nh_1__.lstrip().split(', ')
                    print('so sieht ein element im Nh aus', nh_1_)

                    print('final dict', dict_to_chose)
                    nh_1 = nh_1_[0]
                    if nh_1_ not in uc_dict.get(state_1) and nh_1_ not in dict_to_chose.get(state_1):
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
                    if nh_2_ not in uc_dict.get(state_2) and nh_2_ not in dict_to_chose.get(state_2):
                        instruction_label.config(text="Das ist kein NH des gewählten Zustandes, nochmal")
                        continue
                    else:
                        break
                # jetz muss Spieler 1 in den Nh von Spieler 2 wechseln
                instruction_label.config(text="Spieler 1: wähle Zustand aus NH von Spieler 2")
                while True:
                    input_confirm_button_1.wait_variable(var_1)
                    state_in_NH_1 = spoiler_input
                    if state_in_NH_1 not in nh_2_:
                        instruction_label.config(text="Der Zustand ist da nicht drin, nochmal")
                        continue
                    else:
                        break
                instruction_label.config(text="Spieler 2: wähle Zustand aus NH von Spoiler, der dazu bisimular ist ")
                while True:
                    input_confirm_button_2.wait_variable(var_2)
                    state_in_NH_2 = duplicator_input
                    if state_in_NH_2 not in nh_1_:
                        instruction_label.config(text="Der Zustand ist da nicht drin, nochmal ")
                        continue
                    else:
                        break
            state_1 = state_in_NH_1
            state_2 = state_in_NH_2
            continue

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

if __name__ == "__main__":
    # execute only if run as a script
    main()