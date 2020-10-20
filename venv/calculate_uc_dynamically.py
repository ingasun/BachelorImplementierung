import numpy as np


def calculate_uc_for_single_uc_elements(state_list, uc):
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
    # print('uc', uc)
    for item in uc:
        for element in item:
            # print('item', item)
            for key in position_list_dict.keys():
                if element == key:
                    positions_for_array.append(position_list_dict[key])

    # print('pos', positions_for_array)
    # bitarray bilden, wo die zustände als bits gesetzt sind
    # erstmal initialisieren
    initialize_array = np.zeros(len(state_list), dtype=np.int)
    # print('init', initialize_array)

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

    print('uc_list_bit', uc_list_bit)

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


#state_list = ['s1', 't1', 'u1', 'v1']
#sublist = [['s1'], [['s1'], ['s1', 't1']]]


def get_complete_graph_stuff_for_a_state(state_list, sublist):

    uc_for_a_state = []
    state__ = sublist[0]
    state_ = state__[0]
    print('sublist[1]', sublist[1])
    for uc in sublist[1]:
        list_ = calculate_uc_for_single_uc_elements(state_list, uc)
        uc_for_a_state.append(list_)

    # print('fertige liste', uc_for_a_state)
    # erstmal liste aus list of list
    flat_list = [item for sublist in uc_for_a_state for item in sublist]
    # jetzt doppelte elemente eliminieren
    # jetzt als set um duplicate zu eliminieren
    set_of_tuples = set(tuple(x) for x in flat_list)
    # jetzt wieder als Liste
    final_upper_closure_list = list(set_of_tuples)
    # das ist richtig
    print('final upper closure', final_upper_closure_list)
    edge_list_of_a_state = [(state_, e) for e in final_upper_closure_list]
    # print('das ist die edgelist')
    # print(edge_list_of_a_state)

    #jetzt die Label auch hier rein
    # hier stimmt was nicht das geht so nicht
    # label_list = []
    # for tuple_ in final_upper_closure_list:
    #     label_string_without_comma = ''
    #     for element in tuple_:
    #         label_string_without_comma = label_string_without_comma + element
    #
    #     label_string = ', '.join(label_string_without_comma)
    #     final_label = f'{{{label_string}}}'
    #     label_list.append(final_label)
    # label_node_dict = dict(zip(final_upper_closure_list, label_list))
    label_list = []
    tuple_to_string = [', '.join(map(str, x)) for x in final_upper_closure_list]
    for item in tuple_to_string:
        final_label = f'{{{item}}}'
        label_list.append(final_label)

    label_node_dict = dict(zip(final_upper_closure_list, label_list))




    # und noch die edgelist von intermediate zu hauptzuständen
    # wird nicht gebraucht
    new_state_list = []
    for state in state_list:
        # wenn der Zustand nicht der Zustand ist, für den upper closure berechnet wurde
        # if state not state
        if state is not state_:
            new_state_list.append(state)

    edge_list_intermediate_states = []
    for state in new_state_list:
        for tuple_ in final_upper_closure_list:
            if state in tuple_:
                edge = (tuple_, state)
                edge_list_intermediate_states.append(edge)

    # nicht hier
    # label_list_states = state_list
    # label_node_state = dict(zip(state_list, label_list_states))

    return final_upper_closure_list, edge_list_of_a_state, label_node_dict  # edge_list_intermediate_states
    # upperClosureList, edgelist = get_upper_closure_for_states(state_) Reihenfolge wichtig


# print('complete graph stuff', get_complete_graph_stuff_for_a_state(state_list, sublist))

list_with_all_input = [[['s1'], [[['s1', 't1']], [['u1', 'v1']]]]]
# for item in list_with_all_input:
#     for thing in item[1]:
#         for string in thing:
#             splitted_str = string.split(',')
#             print(splitted_str)

states = ['s1', 't1', 'u1', 'v1']
bla = ([('u1',), ('s1',), ('s1', 'u1'), ('s1', 't1'), ('s1', 't1', 'v1'), ('s1', 'u1', 'v1'), ('s1', 'v1'), ('s1', 't1', 'u1'), ('t1', 'v1'), (), ('u1', 'v1'), ('v1',), ('t1', 'u1'), ('s1', 't1', 'u1', 'v1'), ('t1', 'u1', 'v1'), ('t1',), ('u1',), ('s1', 't1', 'v1'), ('s1', 't1'), ('s1', 'u1'), ('s1', 'u1', 'v1'), ('s1', 't1', 'u1'), ('t1', 'v1'), ('u1', 'v1'), ('t1', 'u1'), ('s1', 't1', 'u1', 'v1'), ('t1', 'u1', 'v1'), ('t1',)], [('s1', ('u1',)), ('s1', ('s1',)), ('s1', ('s1', 'u1')), ('s1', ('s1', 't1')), ('s1', ('s1', 't1', 'v1')), ('s1', ('s1', 'u1', 'v1')), ('s1', ('s1', 'v1')), ('s1', ('s1', 't1', 'u1')), ('s1', ('t1', 'v1')), ('s1', ()), ('s1', ('u1', 'v1')), ('s1', ('v1',)), ('s1', ('t1', 'u1')), ('s1', ('s1', 't1', 'u1', 'v1')), ('s1', ('t1', 'u1', 'v1')), ('s1', ('t1',)), ('t1', ('u1',)), ('t1', ('s1', 't1', 'v1')), ('t1', ('s1', 't1')), ('t1', ('s1', 'u1')), ('t1', ('s1', 'u1', 'v1')), ('t1', ('s1', 't1', 'u1')), ('t1', ('t1', 'v1')), ('t1', ('u1', 'v1')), ('t1', ('t1', 'u1')), ('t1', ('s1', 't1', 'u1', 'v1')), ('t1', ('t1', 'u1', 'v1')), ('t1', ('t1',))], {('u1',): '{u1}', ('s1',): '{s1}', ('s1', 'u1'): '{s1, u1}', ('s1', 't1'): '{s1, t1}', ('s1', 't1', 'v1'): '{s1, t1, v1}', ('s1', 'u1', 'v1'): '{s1, u1, v1}', ('s1', 'v1'): '{s1, v1}', ('s1', 't1', 'u1'): '{s1, t1, u1}', ('t1', 'v1'): '{t1, v1}', (): '{}', ('u1', 'v1'): '{u1, v1}', ('v1',): '{v1}', ('t1', 'u1'): '{t1, u1}', ('s1', 't1', 'u1', 'v1'): '{s1, t1, u1, v1}', ('t1', 'u1', 'v1'): '{t1, u1, v1}', ('t1',): '{t1}'}, {'s1': 's1', 't1': 't1', 'u1': 'u1', 'v1': 'v1'})
def get_all_graph_stuff_for_system(state_list, list_with_all_uc_input):
    intermediate_node_list = []
    edgelist_main_states = []
    label_intermediate_states = {}
    edges_from_intermediate_states = []
    all_upper_closures = list_with_all_uc_input

    for sublist in all_upper_closures:
        # print(sublist)
        # return final_upper_closure_list, edge_list_of_a_state, label_node_dict, label_node_state
        # return final_upper_closure_list, edge_list_of_a_state, label_node_dict  # edge_list_intermediate_states
        # undynamisch intermediate_node_list_sub, edgelist_main_states_sub, label_intermediate_states_sub, edges_from_intermediate_states_sub = uc.get_upper_closure_for_states(state_list, sublist)
        intermediate_node_list_sub, edgelist_main_states_sub, label_intermediate_states_sub = get_complete_graph_stuff_for_a_state(state_list, sublist)
        # intermediate_node_list.append(intermediate_node_list_sub)
        intermediate_node_list += intermediate_node_list_sub
        edgelist_main_states += edgelist_main_states_sub
        label_intermediate_states.update(label_intermediate_states_sub)
        # das brauche ich nicht
        # edges_from_intermediate_states += edges_from_intermediate_states_sub
        label_list_states = state_list
        label_node_main_state = dict(zip(state_list, label_list_states))
    return intermediate_node_list, edgelist_main_states, label_intermediate_states, label_node_main_state



# eprint(get_all_graph_stuff_for_system(states, list_with_all_input))