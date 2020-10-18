

all_state_list = [1, 2, 3, 4, 5]
equivalence_relation = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)]


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


def get_equivalence_classes(all_states, eq_relation):
    equivalence_classes_list = []
    seen = set()
    for state in all_states:
        classes = []
        for tuple_ in eq_relation:
            if state == tuple_[0]:
                classes.append(tuple_[1])
            if state == tuple_[1]:
                classes.append(tuple_[0])
        equivalence_classes_list.append(list(set(classes)))

    classes_without_duplicates = [x for x in equivalence_classes_list if frozenset(x) not in seen and not seen.add(frozenset(x))]
    # remove empty list
    classes = [x for x in classes_without_duplicates if x != []]
    return classes


def calculate_blocks():
    classes = get_equivalence_classes(all_state_list, equivalence_relation)
    blocks = list_powerset(classes)
    return blocks


print(get_equivalence_classes(all_state_list, equivalence_relation))
print(calculate_blocks())

liste = [[], [[1, 2, 3]], [[4]], [[1, 2, 3], [4]], [[5]], [[1, 2, 3], [5]], [[4], [5]], [[1, 2, 3], [4], [5]]]
# g = [[1, 2, 3], [3, 2, 1], [1, 3, 2], [9, 0, 1], [4, 3, 2]]
# seen = set()
#
# [x for x in g if frozenset(x) not in seen and not seen.add(frozenset(x))]
# Out[4]: [[1, 2, 3], [9, 0, 1], [4, 3, 2]]