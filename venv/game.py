import algorithm as alg


# todo es muss noch ausgeschlossen werden, dass Spieler 2 aus demselben NHF wählt
# todo es müssen alle upper closures als NH gewählt werden können


# ich könnte 3 Funktionen schreiben, eine die direkt die gewählten zustände prüft
# zustände und nh müssen in 2 verschiedenen zügen gewählt werden, da die spieler dann je nachdem entscheiden können
# dann die wo Nh gewählt werden
# dann wo die Zustände in den Nh überprüft werden
uc_dict = {'s1': [['t1'], ['u1', 'v1']], 'u1': [['u1']], 's2': [['t2']]}
all_states = ['s1', 't1', 'u1', 'v1', 's2', 't2']
bisimulation = alg.calculate_bisimulation(uc_dict, all_states)
print(bisimulation)


def pick_states(all_states):
    test = True
    while test:
        state_1 = input('Spieler 1 wähle Zustand ')
        if state_1 not in all_states:
            print('Ungültiger Zustand, nochmal')
            continue
        else:
            list_with_recently_picked_states.append(state_1)
            test = False
        state_2 = input('Spieler 2 wähle Zustand ')

    test_2 = True
    while test_2:
        if state_2 not in all_states:
            print('Ungültiger Zustand, nochmal')
            continue
        else:
            test = False

    # erstmal checken, ob die Zustände beide NH haben
    with_nh, without_nh = alg.get_list_with_without_neighbourhoods(uc_dict, all_states)
    if (state_1 in with_nh and state_2 in without_nh) or (state_1 in without_nh and state_2 in with_nh):
        # todo alert box dafür machen
        print('Nicht bisimular, weitermachen')
    if state_1 in without_nh and state_2 in without_nh:
        print('Ja, die sind bisimular,')



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
        # todo alert box dafür machen
        print('Nicht bisimular, weitermachen')
    if state_1 in without_nh and state_2 in without_nh:
        print('Ja, die sind bisimular, weitermachen')
    if state_1 in with_nh and state_2 in with_nh:
        nh_1__ = input('jetzt NH wählen Spieler 1: ')
        nh_1_ = nh_1__.lstrip().split(', ')
        nh_1 = nh_1_[0]
        print(nh_1_)
        if nh_1_ not in uc_dict.get(state_1):
            print('Das ist kein NH des gewählten Zustandes')

        # hier wird direkt abgebrochen wenn die erste uc nicht dem NH entspricht
        # for item in uc_dict.get(state_1):
        #     print('item', item)
        #     if nh_1 not in item:
        #         print('Das ist kein NH des gewählten Zustandes')
        #         break
        nh_2__ = input('jetzt NH wählen Spieler 2: ')
        nh_2_ = nh_2__.lstrip().split(', ')
        nh_2 = nh_2_[0]
        print(nh_2_)
        # hier muss wahrscheinlich der input noch angepasst werden, vielleicht mit list()
        if nh_2_ not in uc_dict.get(state_2):
            print('Das ist kein NH des gewählten Zustandes')
            break # hier wird nur die for-Schleife beendet bis jetzt
        # jetz muss Spieler 1 in den Nh von Spieler 2 wechseln

        # hier mit for Schleife überprüfen, ob die Zustände bisimular sind bis Spieler 2 keinen mehr wählen kann
        i = 0
        for i in range(len(nh_2) - 1):
            i = i+1
            test = True
            while test:
                state_in_NH_1 = input('Spieler 1: wähle Zustand aus NH von Spieler 2 ')
                if state_in_NH_1 not in nh_2_:
                    print('Der Zustand is da nicht drin, nochmal')
                    continue
                state_in_NH_2 = input('Spieler 2: wähle Zustand aus NH von Spieler 1, der dazu bisimular ist ')
                if state_in_NH_2 not in nh_1_:
                    print('Der Zustand is da nicht drin, nochmal')
                    continue
                else:
                    test = False
            if (state_in_NH_1, state_in_NH_2) in bisimulation:
                print('Ja sind bisimular')
                continue
            else:
                print('Nicht bisimular, Spieler 1 hat gewonnen')
                continue

        # das müsste außerhalb der while Schleife stehen, wenn nach einem Zustandspaar wirklich Schluss sein soll
        print('Spiel ist zuende')
        list_with_recently_picked_states.append(state_in_NH_1)
        if list_with_recently_picked_states == all_states:
            print('Spieler 2 kann alle Zustände matchen und hat gewonnen')








