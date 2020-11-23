# uc_with_state_example = [[['s'], [['t'], ['u, v']]], [['u'], [['u']]]]
#
# so = [[[['s1'], [['s1'], ['u1, v1']]]], [[['t1'], [['t1'], ['u1']]]]]
#
# example_input_string = 's1: s1, t1; u1, v1'
#
# first_list = example_input_string.split(':')
# print(first_list)
# second_list = [(first_list[0]), first_list[1].split(';')]
# print('second list', second_list)
# # denke hieraus könnte man ein dictionary erstellen
# # die uc müsste noch lstrip()
#
# #current_input = ['s1', [' s1, t1', ' u1, v1']]
# # muss aufgesplittet werden
# part_1 = [second_list[0]]
# part_2 = [[x.lstrip()] for x in second_list[1]]
# res = [part_1, part_2]
# # es fehlt immer noch eine Klammer
# res_ = [res]
# print(res_)
# test = [[['s1'], [['t'], ['u1, v1']]], [['u'], [['u']]]]
# print(res[0])
# print(res[1])
# # test = [[['s'], [['t1'], ['u1, v1']]]]
# uc_dictionary = {}
# for item in test:
#     for val in item[0]:
#         uc_dictionary[val] = item[1]
# print(uc_dictionary)
#
list_ = ['s1: s1; u1, v1', 't1: t1; u1']

inp = ['s1: u1, v1; t1']


def process_input(input_list_from_all_entry_boxes):
    list_with_processed_input = []
    for input_ in input_list_from_all_entry_boxes:
        first_list = input_.split(':')
        second_list = [(first_list[0]), first_list[1].split(';')]
        part_1 = [second_list[0]]
        part_2 = [[x.lstrip().split(', ')] for x in second_list[1]]
        # print('part_2', part_2)
        # print('unpacked', part_2[0])
        # part_2_unpacked = part_2[0]
        res = [part_1, part_2]
        # print('res', res)
        # res_list = [res]
        list_with_processed_input.append(res)

    uc_dictionary = {}
    for item in list_with_processed_input:
        for val in item[0]:
            uc_el_list = []
            for el in item[1]:
                uc_el_list.append(el[0])

            uc_dictionary[val] = uc_el_list

    # Zustände aus dict
    uc_nh = uc_dictionary.values()
    tuple_list_to_be_colored = []
    for nhs in uc_nh:
        for nh in nhs:
            tuple_list_to_be_colored.append(tuple(nh))

    return list_with_processed_input, uc_dictionary, tuple_list_to_be_colored

# so können 2 unabhängige tupel-listen erstellt werden
# print(process_input(inp))
# list_, dict_, tuple_list = process_input(inp)
#
# print(list_)
# print(dict_)
# print(tuple_list)
# another_tuple_list = [('t1', 'u1', 'v1'), ('s1', 'u1', 'v1'), ('t1', 'v1'), ('s1', 't1', 'u1'), ('s1', 't1', 'v1'), ('t1', 'u1'), ('u1', 'v1'), ('t1',), ('s1', 't1', 'u1', 'v1'), ('s1', 't1')]
# final_intermediate_list = [(e) for e in another_tuple_list if e not in tuple_list]
# print(final_list)
