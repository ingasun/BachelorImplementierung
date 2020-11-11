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
score_label = ttk.Label(root, text='Hier wird angezeigt, ob was bisimular ist')
smart_remarks_label = ttk.Label(root, text='Hier wird angezeigt, ob unnötig verloren, bzw schlecht gespielt')

input_confirm_button_1 = ttk.Button(root, text='Okay!', command=get_input_spoiler)
input_confirm_button_2 = ttk.Button(root, text='Okay!', command=get_input_duplicator)
exit_game_button = ttk.Button(root, text='Exit Game')

# content Sachen

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




        # todo hier muss nur geschaut werden, ob wieder beide NH usw.

        # if (state_in_NH_1, state_in_NH_2) in bisimulation:
        #     print('hey')
        #     instruction_label.config(text="Ja, die sind bisimular, das Spiel geht weiter")
        #     # bringt nichts
        #     # sleep(5)
        #     if list_with_recently_picked_states == all_states:
        #         instruction_label.config(text="Spieler 2 kann alle Zustände matchen und hat gewonnen")
        #         break
        #     else:
        #         # todo hier könnte man einfach state_in_nH1 und 2 auf state 1 und 2 setzen und continue ab dem punkt
        #         continue
        # else:
        #     instruction_label.config(text="Nicht bisimular, Spieler 1 hat gewonnen")
        #     break

root.mainloop()
