from bitarray import bitarray
import numpy as np

# state_list = input('Zustände eingeben und mit leerzeichen trennen: ').split()
state_list = ['s', 't', 'u', 'v']

# zustandsliste, dann aus länge der zustandsliste bitarray generieren
k = len(state_list)
bit_array = np.array([list(np.binary_repr(x, k)) for x in range(2**k)], dtype=int)
# print(bit_array)

# positionen der Zustände in dictionary speichern:
# position_list_dict = {state_list for state in range(len(state_list))}
position_list = dict(enumerate(state_list))
print(position_list)
position_list_dict = dict((v, k) for k, v in position_list.items())
print(position_list_dict)

# jetzt upper closure berechnen

# geht nur für eine gerade, ok, also nur für ein uc element, am besten das alles in for Schleife packen
input_upper_closure_ = input('Welche upper closure hat der Zustand? Bitte mehrere mit Leerzeichen trennen ')
input_upper_closure = input_upper_closure_.split(' ')
final_input_list_upper_closure = y = [list(item) for item in input_upper_closure]
print('uc_list', final_input_list_upper_closure)

#rausbekommen an welcher position die 1sen stehen müssen
positions_for_array = []
for uc in final_input_list_upper_closure:
    for item in uc:
        for key in position_list_dict.keys():
            if item == key:
                positions_for_array.append(position_list_dict[key])

print('pos', positions_for_array)
# bitarray bilden, wo die zustände als bits gesetzt sind
# erstmal initialisieren
initialize_array = np.zeros(len(state_list), dtype=np.int)
print('init', initialize_array)

# flip bit on certain index with xor
for position in positions_for_array:
    initialize_array[position] ^= 1
# arr[idx] ^= 1
print('flipped', initialize_array)

uc_list_bit = []
# jetzt dieses array mit allen aus powerset verunden
for array_ in bit_array:
    if ((array_ & initialize_array) == initialize_array).all():
        uc_list_bit.append(array_)

# print(uc_list_bit)

# liste für graph bilden
# erstmal positionen ermitteln, die im array 1 sind
uc_position_list = []
for array_ in uc_list_bit:
    pos = np. where(array_ == 1)
    # print(len(pos))
    uc_position_list.append(pos)
    # result = np. where(arr == 15)
print('uc_position_list', uc_position_list)

# ohne komisches komma
position_list_schön = []
for item in uc_position_list:
    for i in item:
        # print(i)
        position_list_schön.append(i)
# print(position_list_schön)

# jetzt die nummern durch namen der zustände austauschen
list_for_graph = []
for array_ in position_list_schön:
    tuple_for_graph = []
    for pos in array_:
        # print(pos)
        # print(position_list.get(pos))
        tuple_for_graph.append(position_list.get(pos))
    list_for_graph.append(tuple(tuple_for_graph))

print(list_for_graph)
sublist = [['s'], [['s'], ['s', 't']]]

# jetzt mal als Methode, die brauch statelist und uc von states, vielleicht irgendwann  als dictionary
# todo das funktioniert so nicht
def calculate_uc_for_states(state_list, sublist_with_state_upper_closures):
    # rausfinden für welchen zustand die uc ist
    state__ = sublist_with_state_upper_closures[0]
    print(state__)
    state_ = state__[0]
    input_upper_closure__ = sublist_with_state_upper_closures[1]
    print(input_upper_closure__)

    # erstmal Eingabe verarbeiten
    # input_upper_closure_ = input(f'Welche upper closure hat der Zustand {state_}? Bitte mehrere mit Leerzeichen trennen ')
    # input_upper_closure = input_upper_closure_.split(' ')
    # final_input_list_upper_closure = [list(item) for item in input_upper_closure]
    # print(final_input_list_upper_closure)
    # zustandsliste, dann aus länge der zustandsliste bitarray generieren
    k = len(state_list)
    bit_array = np.array([list(np.binary_repr(x, k)) for x in range(2 ** k)], dtype=int)
    # print(bit_array)

    # positionen der Zustände in dictionary speichern:
    # position_list_dict = {state_list for state in range(len(state_list))}
    position_list = dict(enumerate(state_list))
    # print(position_list)
    position_list_dict = dict((v, k) for k, v in position_list.items())
    # print(position_list_dict)

    # jetzt upper closure berechnen mit sublist
    # geht nur für eine gerade
    # input_upper_closure_ = input('Welche upper closure hat der Zustand? Bitte mehrere mit Leerzeichen trennen ')
    # input_upper_closure = input_upper_closure_.split(' ')
    # final_input_list_upper_closure  = [list(item) for item in input_upper_closure]
    # print(final_input_list_upper_closure)

    # rausbekommen an welcher position die 1sen stehen müssen, ToDo das muss für mehrere ne list of list sein
    positions = []
    for uc in input_upper_closure__:
        positions_for_array = []
        for item in uc:
            for key in position_list_dict.keys():
                if item == key:
                    positions_for_array.append(position_list_dict[key])
        positions.append(positions_for_array)
    print('positions', positions)
    # print(positions_for_array)
    # bitarray bilden, wo die zustände als bits gesetzt sind
    # erstmal initialisieren
    initialize_array = np.zeros(len(state_list), dtype=np.int)
    # print(initialize_array)

    # flip bit on certain index with xor
    list_for_this = []
    uc_list_bit = []
    for _ in positions:
        for position in positions_for_array:
            initialize_array[position] ^= 1
        # uc_list_bit = []
        # jetzt dieses array mit allen aus powerset verunden
        for array_ in bit_array:
            if ((array_ & initialize_array) == initialize_array).all():
                uc_list_bit.append(array_)

    # arr[idx] ^= 1


    # uc_list_bit = []
    # # jetzt dieses array mit allen aus powerset verunden
    # for array_ in bit_array:
    #     if ((array_ & initialize_array) == initialize_array).all():
    #         uc_list_bit.append(array_)

    print('uclistbit', uc_list_bit) # sieht gut aus bis hier, vielleicht schonmal doppelte eliminieren

    # liste für graph bilden
    # erstmal positionen ermitteln, die im array 1 sind
    uc_position_list = []
    for array_ in uc_list_bit:
        pos = np.where(array_ == 1)
        # print(len(pos))
        uc_position_list.append(pos)
        # result = np. where(arr == 15)
    print('uc_position_list', uc_position_list)

    # ohne komisches komma
    position_list_schön = []
    for item in uc_position_list:
        for i in item:
            # print(i)
            position_list_schön.append(i)
    # print(position_list_schön)

    # jetzt die nummern durch namen der zustände austauschen
    list_for_graph = []
    for array_ in position_list_schön:
        tuple_for_graph = []
        for pos in array_:
            # print(pos)
            # print(position_list.get(pos))
            tuple_for_graph.append(position_list.get(pos))
        list_for_graph.append(tuple(tuple_for_graph))

    # ok jetz ist die uc liste für den Graph fertig, jetzt noch die label und so
    return list_for_graph


print('liste aus funktion', calculate_uc_for_states(state_list, sublist))


# ich glaube es wäre besser alles in der funktion so zu lassen und die sublist mit for schleifen und dann funktion auf
# einzelne uc elemente anwenden
uc_for_a_state = []
sublist = [['s'], [['s'], ['s', 't']]]


def function_to_calculate_uc_for_single_uc_elements(state_list, uc):
    k = len(state_list)
    bit_array = np.array([list(np.binary_repr(x, k)) for x in range(2 ** k)], dtype=int)
    # print(bit_array)

    # positionen der Zustände in dictionary speichern:
    # position_list_dict = {state_list for state in range(len(state_list))}
    position_list = dict(enumerate(state_list))
    print(position_list)
    position_list_dict = dict((v, k) for k, v in position_list.items())
    print(position_list_dict)

    # jetzt upper closure berechnen

    # geht nur für eine gerade, ok, also nur für ein uc element, am besten das alles in for Schleife packen
    # input_upper_closure_ = input('Welche upper closure hat der Zustand? Bitte mehrere mit Leerzeichen trennen ')
    # input_upper_closure = input_upper_closure_.split(' ')
    # final_input_list_upper_closure = y = [list(item) for item in input_upper_closure]
    # print('uc_list', final_input_list_upper_closure)

    # rausbekommen an welcher position die 1sen stehen müssen
    positions_for_array = []
    # for uc in final_input_list_upper_closure:
    for item in uc:
        for key in position_list_dict.keys():
            if item == key:
                positions_for_array.append(position_list_dict[key])

    print('pos', positions_for_array)
    # bitarray bilden, wo die zustände als bits gesetzt sind
    # erstmal initialisieren
    initialize_array = np.zeros(len(state_list), dtype=np.int)
    print('init', initialize_array)

    # flip bit on certain index with xor
    for position in positions_for_array:
        initialize_array[position] ^= 1
    # arr[idx] ^= 1
    print('flipped', initialize_array)

    uc_list_bit = []
    # jetzt dieses array mit allen aus powerset verunden
    for array_ in bit_array:
        if ((array_ & initialize_array) == initialize_array).all():
            uc_list_bit.append(array_)

    # print(uc_list_bit)

    # liste für graph bilden
    # erstmal positionen ermitteln, die im array 1 sind
    uc_position_list = []
    for array_ in uc_list_bit:
        pos = np.where(array_ == 1)
        # print(len(pos))
        uc_position_list.append(pos)
        # result = np. where(arr == 15)
    # print('uc_position_list', uc_position_list)

    # ohne komisches komma
    position_list_without_comma = []
    for item in uc_position_list:
        for i in item:
            # print(i)
            position_list_without_comma.append(i)
    # print(position_list_without_comma)

    # jetzt die nummern durch namen der zustände austauschen
    list_for_graph = []
    for array_ in position_list_without_comma:
        tuple_for_graph = []
        for pos in array_:
            # print(pos)
            # print(position_list.get(pos))
            tuple_for_graph.append(position_list.get(pos))
        list_for_graph.append(tuple(tuple_for_graph))

    return list_for_graph
    sublist = [['s'], [['s'], ['s', 't']]]
