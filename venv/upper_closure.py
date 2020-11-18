# import json
# import ast
# Zustände eingeben:
# def get_states():
#     state_list = input('Zustände eingeben und mit leerzeichen trennen: ').split()
#     return state_list

# upper_closure_dict = {'s ': ' {{s}, {s, t}}'}
#
# for k, v in upper_closure_dict.items():
#     state = k.strip()
#     uc = v.strip().replace("{", "[").replace("}", "]")
#     #list_ = json.loads(uc)
#     # list_ = json.loads("[[1,2,3],[4,5,6],[7,8,9]]")
#     print(uc)
#     #m = ast.literal_eval(uc)
#     print(type(uc))
#     print(state)
#     print(uc)
#



# potenzmenge mit bitmap
# def powerset(s):
#     x = len(s)
#     global list_
#     list_ = []
#     for i in range(1 << x):
#         list_.append([s[j] for j in range(x) if (i & (1 << j))])
#
#
# powerset([4,5,6])
# print(list_)

# Potenzmenge ausrechen
def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result


# jetzt upper closure für einen Zustand ausrechnen, besser wäre hier statt statelist nur einen Zustand einzugeben
# eingabe eine sublist mit zustand und upper closures und die liste mit allen zuständen
def get_upper_closure_for_states(state_list, sublist_with_state_upper_closures):

    state__ = sublist_with_state_upper_closures[0]
    state_ = state__[0]
    input_upper_closure = sublist_with_state_upper_closures[1]

    # erstmal Eingabe verarbeiten
    # input_upper_closure_ = input(f'Welche upper closure hat der Zustand {state_}? Bitte mehrere mit Leerzeichen trennen ')
    # input_upper_closure = input_upper_closure_.split(' ')
    final_input_list_upper_closure = [list(item) for item in input_upper_closure]
    # print(final_input_list_upper_closure)

    # jetzt die upper closure berechnen
    powerset_ = list_powerset(state_list)
    upper_closure_list_with_duplicates = []
    for input_ in final_input_list_upper_closure:

        if len(input_) == 3:
            for sublist in powerset_:
                if input_[0] in sublist and input_[1] in sublist and input_[2] in sublist:
                    upper_closure_list_with_duplicates.append(sublist)
        if len(input_) == 2:
            for sublist in powerset_:
                if input_[0] in sublist and input_[1] in sublist:
                    upper_closure_list_with_duplicates.append(sublist)
        if len(input_) == 1:
            for sublist in powerset_:
                if input_[0] in sublist:
                    upper_closure_list_with_duplicates.append(sublist)
        if len(input_) == 0:
            break

    # print('liste mit duplicaten')
    # print(upper_closure_list_with_duplicates)
    # print('das ist die upper closure liste')
    # jetzt als set um duplicate zu eliminieren
    set_of_tuples = set(tuple(x) for x in upper_closure_list_with_duplicates)
    # jetzt wieder als Liste
    final_upper_closure_list = list(set_of_tuples)
    # print(final_upper_closure_list)
    edge_list_of_a_state = [(state_, e) for e in final_upper_closure_list]
    # print('das ist die edgelist')
    # print(edge_list_of_a_state)

    #jetzt die Label auch hier rein
    label_list = []
    for tuple_ in final_upper_closure_list:
        label_string_without_comma = ''
        for element in tuple_:
            label_string_without_comma = label_string_without_comma + element

        label_string = ', '.join(label_string_without_comma)
        final_label = f'{{{label_string}}}'
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

    return final_upper_closure_list, edge_list_of_a_state, label_node_dict  # edge_list_intermediate_states
    # upperClosureList, edgelist = get_upper_closure_for_states(state_) Reihenfolge wichtig


#print(get_upper_closure_for_states('a'))
# ausprobieren die elemente in der upper closure list als so zu bekommen, dass sie als nodes eingegeben werden können
#     for tuple_ in final_upper_closure_list:
#         print(tuple_)

state_list = ['s', 't', 'u', 'v']
sublist = [['s'], [['s'], ['s', 't']]]

print(get_upper_closure_for_states(state_list, sublist))
# labelliste mit schönen labels für Zwischenzustände machen: könnte man vielleicht direkt in der anderen Funktion machen
def create_nice_lable_intermediate_state():
    ask_which_state = input('für welchen zustand die label? ')
    intermediate_state_list = get_upper_closure_for_states(ask_which_state)
    label_list = []
    for tuple_ in intermediate_state_list:
        label_string_without_comma = ''
        for element in tuple_:
            label_string_without_comma = label_string_without_comma + element

        label_string = ', '.join(label_string_without_comma)
        final_label = f'{{{label_string}}}'
        label_list.append(final_label)
    label_node_dict = dict(zip(intermediate_state_list, label_list))
    return label_node_dict


#label_list_ = create_nice_lable_intermediate_state()
#print(label_list_)


# hier wäre es gut alle intermediate states, die keine upper closure haben in einer Liste zu haben,
# im Beispiel hat ja eh nur ein zustand eine upper closure
# hier wird als parameter noch der zustand gebraucht
def get_edgelist_for_intermediate_states(state_list_, input_upper_closure, final_upper_closure_list_):

    new_state_list = []
    for state in state_list_:
        # wenn der Zustand nicht der Zustand ist, für den upper closure berechnet wurde
        # if state not state
        if state is not state_:
            new_state_list.append(state)

    edge_list_intermediate_states = []
    for state in new_state_list:
        for tuple_ in final_upper_closure_list_:
            if state in tuple_:
                edge = (tuple_, state)
                edge_list_intermediate_states.append(edge)

    return edge_list_intermediate_states


#another_egde_list = get_edgelist_for_intermediate_states(state_list, input_upper_closure_, final_upper_closure_list)
#print(another_egde_list)







