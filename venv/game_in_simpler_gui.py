import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import algorithm as alg
from time import time, sleep


def get_input_spoiler():
    global spoiler_input
    spoiler_input = input_spoiler.get()
    input_spoiler.delete("0", "end")
    print('in funktion', spoiler_input)
    var_1.set(1)


def get_input_duplicator():
    global duplicator_input
    duplicator_input = input_duplicator.get()
    input_duplicator.delete("0", "end")
    print('in funktion', duplicator_input)
    var_2.set(1)


# Spiel
root = tk.Tk()
root.title('Spiel')
root.geometry('900x900')
var_1 = tk.IntVar()
var_2 = tk.IntVar()

label_input_player_1 = ttk.Label(root, text='Eingabe Spoiler')
input_spoiler = ttk.Entry(root)
label_input_player_2 = ttk.Label(root, text='Eingabe Duplicator')
input_duplicator = ttk.Entry(root)
instruction_label = ttk.Label(root, text='Hier werden gleich Anweisungen stehen')

input_confirm_button_1 = ttk.Button(root, text='Okay!', command=get_input_spoiler)
input_confirm_button_2 = ttk.Button(root, text='Okay!', command=get_input_duplicator)
exit_game_button = ttk.Button(root, text='Exit Game')

# content Sachen

label_input_player_1.grid(row=4, column=0, padx=20, sticky='W')
label_input_player_2.grid(row=4, column=1, pady=20, padx=20, sticky='E')
input_spoiler.grid(row=5, column=0, padx=20, sticky='W')
input_duplicator.grid(row=5, column=1, padx=20, sticky='E')
instruction_label.grid(row=7, padx=20, sticky='EW')

input_confirm_button_1.grid(row=8, column=0, pady=20, padx=20, sticky='W')
input_confirm_button_2.grid(row=8, column=1, pady=20, padx=20, sticky='E')
exit_game_button.grid(row=9, pady=20, padx=20, sticky='NEWS')

uc_dict = {'s1': [['t1'], ['u1', 'v1']], 'u1': [['u1']], 's2': [['t2']]}
all_states = ['s1', 't1', 'u1', 'v1', 's2', 't2']
bisimulation = alg.calculate_bisimulation(uc_dict, all_states)

print(bisimulation)
list_with_recently_picked_states = []


# todo auch Nh aus uc zulassen
# spiel endet, wenn duplicator nicht mit bisimularen zustand antworten kann oder Spieler 1 keinen zug machen kann
#
while all_states != list_with_recently_picked_states:
    instruction_label.config(text="Spoiler bitte Zustand wählen")
    while True:
        input_confirm_button_1.wait_variable(var_1)
        state_1 = spoiler_input
        if state_1 not in all_states:
            print('hello')
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
    with_nh, without_nh = alg.get_list_with_without_neighbourhoods(uc_dict, all_states)
    if state_1 in with_nh and state_2 in without_nh:
        instruction_label.config(text="Nicht bisimular, Spoiler hat gewonnen")
        break
    if state_1 in without_nh and state_2 in with_nh:
        instruction_label.config(text="Ja, die sind bisimular, Duplicator hat gewonnen")
        break
    if state_1 in without_nh and state_2 in without_nh:
        instruction_label.config(text="Ja, die sind bisimular, Duplicator hat gewonnen")
        break
    # todo bis hier das könnte besser in extra funktion
    if state_1 in with_nh and state_2 in with_nh:
        instruction_label.config(text="jetzt NH wählen Spieler 1")
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
        instruction_label.config(text="jetzt NH wählen Duplicator")
        while True:
            input_confirm_button_2.wait_variable(var_2)
            nh_2__ = duplicator_input
            nh_2_ = nh_2__.lstrip().split(', ')
            nh_2 = nh_2_[0]
            print(nh_2_)
            # hier muss wahrscheinlich der input noch angepasst werden, vielleicht mit list()
            if nh_2_ not in uc_dict.get(state_2):
                instruction_label.config(text="Das ist kein NH des gewählten Zustandes")
                # print('Das ist kein NH des gewählten Zustandes')
                continue # hier wird nur die for-Schleife beendet bis jetzt
            else:
                break
        # jetz muss Spieler 1 in den Nh von Spieler 2 wechseln

        # hier mit for Schleife überprüfen, ob die Zustände bisimular sind bis Spieler 2 keinen mehr wählen kann
        # todo das muss noch geändert werden gemäß der Definition vom Spiel
        # i = 0
        #for i in range(len(nh_2) - 1):
        #    i = i+1
        instruction_label.config(text="Spieler 1: wähle Zustand aus NH von Spieler 2")
        while True:
            input_confirm_button_1.wait_variable(var_1)
            state_in_NH_1 = spoiler_input
            if state_in_NH_1 not in nh_2_:
                instruction_label.config(text="Der Zustand is da nicht drin, nochmal ")
                continue
            else:
                list_with_recently_picked_states.append(state_in_NH_1)
                break
        instruction_label.config(text="Spieler 2: wähle Zustand aus NH von Spieler 1, der dazu bisimular ist ")
        while True:
            input_confirm_button_2.wait_variable(var_2)
            state_in_NH_2 = duplicator_input
            if state_in_NH_2 not in nh_1_:
                instruction_label.config(text="Der Zustand is da nicht drin, nochmal ")
                continue
            else:
                break
        # todo hier muss nur geschaut werden, ob wieder beide NH usw.
        # todo wird nicht als tupel erkannt

        if (state_in_NH_1, state_in_NH_2) in bisimulation:
            print('hey')
            instruction_label.config(text="Ja, die sind bisimular, das Spiel geht weiter")
            if list_with_recently_picked_states == all_states:
                instruction_label.config(text="Spieler 2 kann alle Zustände matchen und hat gewonnen")
                break
            else:
                continue
        else:
            instruction_label.config(text="Nicht bisimular, Spieler 1 hat gewonnen")
            # hier kann dann abgebrochen werden
            break
