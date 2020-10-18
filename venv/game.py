import algorithm as alg

uc_dict = {'s1': [['t1'], ['u1', 'v1']], 'u1': [['u1']], 's2': [['t2']]}

list_with_recently_picked_states = []
all_states = ['s1', 't1', 'u1', 'v1', 's2', 't2']

list_with_recently_picked_states = []
# das Spiel soll mindestens solange laufen, bis Spieler 1 keinen Zustand mehr wählen kann oder will
while all_states != list_with_recently_picked_states:
    state_1 = input('Spieler 1 wähle Zustand ')
    if state_1 not in all_states:
        print('Ungültiger Zustand')
        break
    state_2 = input('Spieler 2 wähle Zustand ')
    if state_2 not in all_states:
        print('Ungültiger Zustand')
        break
    list_with_recently_picked_states.append(state_1)
    # erstmal checken, ob die Zustände beide NH haben
    with_nh, without_nh = alg.get_list_with_without_neighbourhoods(uc_dict, all_states)
    if (state_1 in with_nh and state_2 in without_nh) or (state_1 in without_nh and state_2 in with_nh):
        print('Nicht bisimular, weitermachen')
    if state_1 in without_nh and state_2 in without_nh:
        print('Ja, die sind bisimular, weitermachen')
    if state_1 in with_nh and state_2 in with_nh:
        nh_1__ = input('jetzt NH wählen Spieler 1: ')
        nh_1_ = nh_1__.lstrip().split(', ')
        nh_1 = nh_1_[0]
        print(nh_1)
        for item in uc_dict.get(state_1):
            if nh_1 not in item:
                print('Das ist kein NH des gewählten Zustandes')
                break
        nh_2 = input('jetzt NH wählen Spieler 2: ')
        print(nh_2)
        # hier muss wahrscheinlich der input noch angepasst werden, vielleicht mit list()
        for item in uc_dict.get(state_2):
            if nh_2 not in item:
                print('Das ist kein NH des gewählten Zustandes')
                break # hier wird nur die for-Schleife beendet bis jetzt
        # jetz muss Spieler 1 in den Nh von Spieler 2 wechseln
        state_in_NH_1 = input('Spieler 1: wähle Zustand aus NH von Spieler 2 ')
        state_in_NH_2 = input('Spieler 1: wähle Zustand aus NH von Spieler 1, der dazu bisimular ist ')
        if state_in_NH_1 not in nh_2:
            print('Der Zustand is da nicht drin')
            break
        if state_in_NH_2 not in nh_1:
            print('Der Zustand is da nicht drin')
            break
        list_with_recently_picked_states.append(state_in_NH_1)
        if list_with_recently_picked_states == all_states:
            print('Spieler 2 kann alle Zustände matchen und hat gewonnen')









