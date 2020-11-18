from copy import deepcopy
import itertools

state_list_1= {'s1', 't1', 'u1', 'v1'}
state_list_2 = {'s2', 't2'}
all_states = state_list_1.union(state_list_2)
# uc_dict = {}
# upper closures der Zustände
# vielleicht als dictionary
upper_closure_list_sytem_1 = [[['s1'], [['t1'], ['u1', 'v1']]], [['u1'], [['u1']]]]
upper_closure_list_sytem_2 = [[['s2'], [['t2']]]]
all_closures = upper_closure_list_sytem_1 + upper_closure_list_sytem_2
# print(all_closures)
# make dict for state and its uc
uc_dictionary = {}
for item in all_closures:
    for val in item[0]:
        uc_dictionary[val] = item[1]
print(uc_dictionary)
# print(all_closures)


def get_uc_dict_and_list_of_states(states_1, states_2, list_with_processed_input):
    pass


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


def calculate_coarsest_relation(states_1, states_2):
    # Mengen vereinigen
    all_states = states_1.union(states_2)
    all_states_ = states_2.union(states_1)
    r_0 = ((x, y) for x, y in itertools.product(all_states, all_states_))
    return list(r_0)


test_relation = calculate_coarsest_relation(state_list_1, state_list_2)


def get_equivalence_classes(current_relation, states):
    # die Funktion darf nur die aktuelle relation bekommen
    # eq_relation, all_states = calculate_coarsest_relation(state_list_1, state_list_2)
    equivalence_classes_list = []
    seen = set()
    for state in states:
        classes = []
        for tuple_ in current_relation:
            if state == tuple_[0]:
                classes.append(tuple_[1])
            if state == tuple_[1]:
                classes.append(tuple_[0])
        equivalence_classes_list.append(list(set(classes)))

    classes_without_duplicates = [x for x in equivalence_classes_list if frozenset(x) not in seen and not seen.add(frozenset(x))]
    # remove empty list
    classes = [x for x in classes_without_duplicates if x != []]
    return classes


def calculate_blocks(classes):
    # classes = get_equivalence_classes(test_realtion, all_states)
    blocks = list_powerset(classes)
    return blocks


def get_list_with_without_neighbourhoods(uc_dict, states):   # funktion nimmt einfach einen Zustand
    states_with_neighbourhoods = []
    states_without_neighbourhoods = []
    for state in states:
        if state in uc_dict.keys():
            states_with_neighbourhoods.append(state)
        else:
            states_without_neighbourhoods.append(state)
    return states_with_neighbourhoods, states_without_neighbourhoods


# blöcke = calculate_blocks()
# blöcke = 'bla' #paar blöcke mit mehr klassen bauen
# an_relation = [('s2', 's2'), ('s2', 't2'), ('s2', 'v1'), ('s2', 't1'), ('s2', 'u1'), ('s2', 's1'), ('v1', 's2'), ('v1', 't2'), ('v1', 'v1'), ('v1', 't1'), ('v1', 'u1'), ('v1', 's1'), ('t2', 's2'), ('t2', 't2'), ('t2', 'v1'), ('t2', 't1'), ('t2', 'u1'), ('t2', 's1'), ('t1', 's2'), ('t1', 't2'), ('t1', 'v1'), ('t1', 't1'), ('t1', 'u1'), ('t1', 's1'), ('u1', 's2'), ('u1', 't2'), ('u1', 'v1'), ('u1', 't1'), ('u1', 'u1'), ('u1', 's1'), ('s1', 's2'), ('s1', 't2'), ('s1', 'v1'), ('s1', 't1'), ('s1', 'u1'), ('s1', 's1')]
# clas = get_equivalence_classes(test_realtion, all_states)
# bloks = calculate_blocks(clas)


def calculate_new_relation(blocks_, an_relation):
    update_happened = False
    # eliminate empty list from blocks
    blocks = [x for x in blocks_ if x]
    # print('blocks', blocks)
    for block in blocks:
        # print('block', block)
        # Klassen von Block vereinigen um Teilmengenbeziehung zu prüfen
        union_class_list = [item for sublist in block for item in sublist]
        # print('union class list', union_class_list)
        # jetzt für alle tupel durchschauen ob die Zustände darin oder deren ucs teilmenge der Blöcke sind
        for tuple_ in an_relation:  # tuple mit Zuständen x, y
            # print('tuple_', tuple_)
            # es werden nur Zustände, die beide eine uc haben überprüft, da die unterschiedlichen schon ausgesiebt wurden
            # und die, die beide eine haben eh drin bleiben
            if tuple_[0] in uc_dictionary.keys() and tuple_[1] in uc_dictionary.keys():
                has_subset_tilde_1 = [] # um festzustellen ob ein Zustand sowas hat
                # jetzt die uc mit for_Schleife durchgehen
                for uc in uc_dictionary.get(tuple_[0]):
                    is_set_1 = []
                    # print('uc 1', uc)
                    is_set_1_ = all(x in union_class_list for x in uc)
                    # one = [1, 2, 3]
                    # two = [9, 8, 5, 3, 2, 1]
                    # all(x in two for x in one)
                    # set(one).issubset(set(two))
                    # print('is set 1', is_set_1_)
                    if all(x in union_class_list for x in uc):
                        is_set_1.append(True)
                        # auf super set untersuchen
                        is_tilde_1 = []
                        for class_ in block:
                            # print('class', class_)
                            # hier wird geprüft ob der Schnitt von uc und Klasse leer ist oder nicht
                            if set(class_) & set(uc):
                                # set(class_).intersection(uc) != set():
                                is_tilde_1.append(True)
                            else:
                                is_tilde_1.append(False)
                        # print('is_tilde_1', is_tilde_1)
                        # hier wird geprüft ob uc mit keiner der Klassen des Blocks einen leeren Schnitt hat
                        if all(is_tilde_1):
                            has_subset_tilde_1.append(True)
                        else:
                            has_subset_tilde_1.append(False)
                # print('has tilde_1', has_subset_tilde_1)
                # das gleiche jetzt für den anderen Zustand
                has_tilde_2 = []
                for uc_ in uc_dictionary.get(tuple_[1]):
                    is_set_2 = []
                    is_tilde_2 = []
                    # print('uc_2', uc_)
                    # print('is_set_2', all(x in union_class_list for x in uc_))
                    if all(x in union_class_list for x in uc_):
                        is_set_2.append(True)
                        for class_ in block:
                            # print('class', class_)
                            # is_tilde_2 = []
                            if set(class_) & set(uc_):
                                is_tilde_2.append(True)
                            else:
                                is_tilde_2.append(False)
                        if all(is_tilde_2):
                            has_tilde_2.append(True)
                        else:
                            has_tilde_2.append(False)
                        # print('is_tilde2', is_tilde_2)
                # print('has tilde 2', has_tilde_2)
                # if not is_set_1 and not is_set_2:
                #     continue
                # if not(all(is_set_1) and not(all(is_set_2))):
                #     continue
                # if all(is_set_1 and not(all(is_set_2))):  # hier muss vielleicht any hin - nein, es geht immer nur um eine
                #     print('removed tuple', tuple_)
                #     an_relation.remove(tuple_)
                #     update_happened = True
                #     continue
                # if not(all(is_set_1)) and all(is_set_2):  # hier muss vielleicht any hin - nein, es geht immer nur um eine
                #     print('removed tuple', tuple_)
                #     an_relation.remove(tuple_)
                #     update_happened = True
                #     continue
                # klar dass das nicht geht, weil ja nur eins leer sein muss oder ?
                # if not has_subset_tilde_1 and not has_tilde_2:
                #     continue
                if not(any(has_subset_tilde_1) or is_set_1) and any(has_tilde_2):
                    # print('removed tuple', tuple_)
                    an_relation.remove(tuple_)
                    update_happened = True
                    continue
                if any(has_subset_tilde_1) and not(any(has_tilde_2) or is_set_2):
                    # print('removed tuple', tuple_)
                    an_relation.remove(tuple_)
                    update_happened = True
    return update_happened, an_relation

# print('das ist eine iteration', calculate_new_relation(bloks, an_relation))


def calculate_bisimulation(uc_dict, states):
    coarsest_relation = calculate_coarsest_relation(state_list_1, state_list_2)
    # current_relation = coarsest_relation # muss immer die zuletzt berechnete sein
    # am besten hier direkt die mit NH von denen ohne trennen
    with_nh, without_nh = get_list_with_without_neighbourhoods(uc_dict, states)
    without_different_nh = [x for x in coarsest_relation if
                                  (x[0] in with_nh and x[1] in with_nh or x[0] in without_nh and x[1] in without_nh)]
    relation_before = without_different_nh
    # current_relation = []
    # hier jetzt ne flag setzen
    updateshappened = True
    # while relation_before_ != current_relation:
    while updateshappened:
        # updateshappened = False
        current_relation = deepcopy(relation_before)
        # temp_rel = current_relation
        # hier kommen jetzt die Funktionsaufrufe
        classes = get_equivalence_classes(current_relation, all_states)
        # print('classes', classes)
        blocks = calculate_blocks(classes)
        # print('blocks', blocks)
        updateshappened, relation_before = calculate_new_relation(blocks, current_relation)
        # print(updateshappened, relation_before)
    return current_relation


# bisimation = calculate_bisimulation(uc_dictionary, all_states)
# print('bisimulation', bisimation)
# cr = (calculate_coarsest_relation(state_list_1, state_list_2))
# print(get_equivalence_classes())
# with_nh, without_nh = get_list_with_without_neighbourhoods(uc_dictionary, all_states)

# list comprehension um tupel zu eliminieren
# without_tuple_different_nh = [x for x in cr if (x[0] in with_nh and x[1] in with_nh or x[0] in without_nh and x[1] in without_nh)]
# print('without Nh', without_tuple_different_nh)

# musterlösung = {(s1 , s2 ), (t1 , t2 ), (v1 , t2 )}
# todo es sind auch paare aus demselben system drin und u1 wurde auch entfernt zuerst...
# so_jetzt = [('t2', 't2'), ('t2', 't1'), ('t2', 'v1'), ('t1', 't2'), ('t1', 't1'), ('t1', 'v1'), ('v1', 't2'), ('v1', 't1'), ('v1', 'v1')]
# so jetzt_ = [('t1', 't1'), ('t1', 't2'), ('t1', 'v1'), ('t2', 't1'), ('t2', 't2'), ('t2', 'v1'), ('s2', 's1'), ('s2', 's2'), ('s1', 's1'), ('s1', 's2'), ('u1', 'u1'), ('v1', 't1'), ('v1', 't2'), ('v1', 'v1')]
