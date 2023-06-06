from base import Automate


# 2. reconnaissance d'un mot par un automate
def reconnaissance(A: Automate, mot: str) -> bool:

    if A.est_deterministe():

        etat = A.etats_initiaux[0]
        for char in mot:
            if char not in A.alphabet:
                return False
            etat = A.f_transitions(etat, char)[0]
            if len(etat) == 0 or etat == ['puit']:
                return False
        if etat in A.etats_finaux:
            return True
        return False

    else:
        pile = []
        for chaque_etat_initial in A.etats_initiaux:
            pile.append((chaque_etat_initial, 0))

        while len(pile) > 0:
            etat_actuel, indice_actuel_du_mot = pile.pop()
            if indice_actuel_du_mot == len(mot):
                if etat_actuel in A.etats_finaux:
                    return True
            else:
                etats_possibles_pour_cette_transition = A.f_transitions(
                    etat_actuel, mot[indice_actuel_du_mot])
                for chaque_etat in etats_possibles_pour_cette_transition:
                    if len(chaque_etat) != 0 and chaque_etat != ['puit']:
                        pile.append((chaque_etat, indice_actuel_du_mot+1))

        return False


A = Automate()

# exemple de ce à quoi doit ressembler le dictionnaire des transitions
A_transitions = {
    ((0,), 'b'): [[0]],
    ((0,), 'a'): [[1]],
    ((1,), 'b'): [[1]],
    ((1,), 'a'): [[2]],
    # ((2,),'b'):[[2]],
    ((2,), 'b'): [[2], [3]],
    ((2,), 'a'): [[0]],
    ((3,), 'b'): [[3]],
    ((3,), 'a'): [[0]]
}

A.create(alphabet=['a', 'b'], etats=[[0], [1], [2], [3]], etats_initiaux=[
         [0]], etats_finaux=[[3]], transitions=A_transitions)
