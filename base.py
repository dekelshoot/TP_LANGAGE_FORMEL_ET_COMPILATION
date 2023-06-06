# classe automate

from re import T


class Automate():

    """
    Ce qu'il faut savoir de la calsse Automate() :

    1. L'alphabet est une LISTE de tous les symboles du langage reconnu
    2. L'ensemble des etats, Q, c'est egalement une liste des differents etats de l'automate, donc une LISTE DE LISTE.
    3. L'etat initial, est une LISTE DE LISTE, (d'au moins une liste), si la liste n'a qu'une seule liste alors,
    alors cet automate n'a qu'un seul etat initial, maintenant si cette une seule liste n'a qu'un seul element, alors l'etat initial
    est un sous ensemble d'un seul etat..
    4. Pareil pour l'etat final.
    5. Un etat qi maintenant est une simple LISTE d'un ou plusieurs elements, si cette liste a un seul element alors cet etat est un
    sous ensemble d'un seul etat
    6. La fonction de transition prend donc en entree, une liste d'elements, un str ( le symbole ) et retourne une liste de liste, j'explique :
    un etat est materialisé par une liste d'elements, ca peut etre plus d'un element(dans le cas d'un determinisé),
    le symbole est tout simplement un caractere de l'alphabet à lire. La liste de le liste retournee est tout simplement la liste
    des differents etats ou la transition peut nous emmener, la premiere liste est pour contenir ces differents etats, la deuxieme
    est pour chacun des etats ou ca nous mene
    7. Le dictionnaire transactions est un dictionnaire materialisant les transitions de l'automate, un element du dictionnaire est
    tel que la cle est un tuple contenant deux elements, le premiere est un tuple, qui a tous les elements de l'etat et l'autre
    element est le symbole lu, maintenant la valeur est est une liste de liste donc la liste des etats aux quels ca mene

    """

    # Constructeur de la classe
    def __init__(self):

        self.alphabet = []
        self.etats = []
        self.etats_initiaux = []
        self.etats_finaux = []
        self.transitions = {}

    # fonction de transition
    def f_transitions(self, etat: list, symbole: str) -> list:

        for trans in self.transitions:  # je parcours les transitions
            # si je tombe sur un transition telle que l'etat est celui que je passe en entree, et le symbole ce lui que je passe en entree
            if list(trans[0]) == etat and trans[1] == symbole:
                # alors je prends l'etat au quel ca mene et je le retourne
                return self.transitions[trans]
        return []

    # fonction permettant de savoir si un automate contient des epsilonnes-transitions
    def est_epsilone_non_deterministe(self) -> bool:

        for trans in self.transitions.keys():
            if trans[1] == 'e':
                return True
        return False

    # fonction permettant de savoir si un automate est non-deterministe
    def est_non_deterministe(self) -> bool:

        for trans in self.transitions.values():
            if len(trans) > 1:
                return True

        if len(self.etats_initiaux) > 1:
            return True

        return False

    # fonction permettant de savoir si un automate est deterministe
    def est_deterministe(self) -> bool:

        for trans in self.transitions.values():
            if len(trans) > 1:
                return False

        if len(self.etats_initiaux) > 1:
            return False

        return True

    # fonction permettant de savoir si un automate est complet
    def est_complet(self) -> bool:

        for etat in self.etats:
            for char in self.alphabet:
                if (tuple(etat), char) not in self.transitions.keys():
                    return False
        return True

    def ajout_etat(self, etat: list, initial=False, final=False) -> bool:
        """
        ajout d'un etat dans un automate
        @param state : l'etat que tu veux ajouter dans l'automate (une liste, qui est l'etat)
        @param initial : si True, alors l'etat est un etat initial
        @param final : si True, alors l'etat est un etat final

        """

        if not etat in self.etats:
            self.etats.append(etat)

            if initial == True:
                self.etats_initiaux.append(etat)

            if final == True:
                self.etats_finaux.append(etat)

            return True
        else:

            return False

    def valider_symbole(self, symbole: str) -> bool:

        if symbole not in self.alphabet:
            return False
        return True

    def ajouter_symbole(self, symbole: str) -> bool:

        if symbole not in self.alphabet:
            self.alphabet.append(symbole)
            return True
        return False

    def valider_etat(self, etat: list) -> bool:

        if etat not in self.etats:
            return False
        return True

    def ajout_transition(self, etat_depart: list, symbole: str, etat_arrive: list) -> bool:
        """
        ajout d'une transition dans un automate
        @param etat_depart : l'etat de depart de la transition
        @param symbole : si True, alors l'etat est un etat initial
        @param etat_arrive : si True, alors l'etat est un etat final

        """
        if not self.valider_symbole(symbole):
            print('le symbole ' + symbole +
                  ' ne fait pas partie de l\'alphabet.')
            return False

        if not self.valider_etat(etat_depart):
            print('l\'etat de depart ' +
                  etat_depart[0] + ' ne fait pas partie des etats.')
            return False

        if not self.valider_etat(etat_arrive):
            print('l\'etat d\'arrive ' +
                  etat_arrive[0] + ' ne fait pas partie des etats.')
            return False

        # donc j'ajoute la trasition si : oit le couple etat initaial, symbole n'existe pas encore soit ca existe mais etat arrive n'est pas celui que je veux ajouter
        if (tuple(etat_depart), symbole) not in self.transitions or ((tuple(etat_depart), symbole) in self.transitions and etat_arrive not in self.f_transitions(etat_depart, symbole)):

            if (tuple(etat_depart), symbole) in self.transitions:
                self.transitions[tuple(etat_depart),
                                 symbole].append(etat_arrive)
            else:
                # print("l'état d'arrivé est", etat_arrive)
                self.transitions[(tuple(etat_depart), symbole)] = [etat_arrive]

            return True

        elif (tuple(etat_depart), symbole) in self.transitions and etat_arrive in self.f_transitions(etat_depart, symbole):
            print("transition deja presente dans l'automate")
            return False

    # fonction qui retourne toutes les natures d'un automate
    def nature(self) -> str:

        nature = []

        if self.est_epsilone_non_deterministe():
            nature.append("e-AFN")

        if self.est_non_deterministe():
            nature.append("AFN")

        if self.est_deterministe():
            nature.append("AFD")

        if self.est_complet():
            nature.append("Complet")

        return "Cet automate est : " + ", ".join(nature)

    # fonction permettant de creer un automate
    def create(self, alphabet: list, etats: list, etats_initiaux: list,
               etats_finaux: list, transitions: dict):
        """
        creation d'un automate (definition du quintuplet)
        @param alphabet : l'alphabet de l'automate
        @param etats : liste des etats de l'automate (il s'agit s'une liste de liste)
        @param etats_initiaux : liste des etats initiaux de l'automate (il s'agit d'une liste d'une liste)
        @param etats_finaux : liste des etats finaux de l'automate (il s'agit d'une liste d'une liste)

        """

        self.alphabet = alphabet
        self.etats = etats
        self.etats_initiaux = etats_initiaux
        self.etats_finaux = etats_finaux
        self.transitions = transitions

    # Afficher de facon commode un automate

    def __str__(self):
        """
        Affichage de facon propre l'objet automate
        """
        intermediaires = set([etat[0] for etat in self.etats]) - set([etat[0]
                                                                      for etat in self.etats_initiaux]) - set([etat[0] for etat in self.etats_finaux])
        ret = self.nature() + ":\n"
        ret += "   - alphabet   : {" + ", ".join(self.alphabet) + "} \n"
        ret += "   - initiaux      : " + \
            ", ".join([init[0] for init in self.etats_initiaux]) + "\n"
        ret += "   - etats intermediaires : " + \
            ", ".join([init for init in intermediaires]) + "\n"
        ret += "   - finaux    : " + \
            ", ".join([init[0] for init in self.etats_finaux]) + "\n"
        ret += "   - nombre d'etats : %d \n" % (len(self.etats))
        ret += "   - transitions :\n"
        for etat in self.etats:
            ret += "       Partant de l'état (%s): \n" % (etat[0])
            for symbole in self.alphabet:

                if not len(self.f_transitions(etat, symbole)) == 0:
                    for dest in self.f_transitions(etat, symbole):
                        ret += "          en lisant le symbole (%s) on arrive à l'état (%s)\n" % (
                            symbole, dest[0])

        return ret

    def Union(lst1, lst2):
        final_list = list(set(lst1) | set(lst2))
        return final_list
    # surcharge de l'opération d'addition

    def __add__(self, other):
        alphabet = self.Union(self.alphabet, other.alphabet)
        etats = self.Union(self.etats, other.etats)
        etats_initiaux = self.Union(self.etats_initiaux, other.etats_initiaux)
        etats_finaux = self.Union(self.etats_finaux + other.etats_finaux)
        transitions = {}
        transitions.update(self.transitions)
        transitions.update(other.transitions)
        res = Automate()
        res.create(alphabet, etats, etats_initiaux, etats_finaux, transitions)
        return res


"""
### TESTS

# j'instancie la classe et je cree un automate (A)
A = Automate()

# exemple de ce à quoi doit ressembler le dictionnaire des transitions
A_transitions = {
			((0,),'b'):[[0]], 
			((0,),'a'):[[1]],
			((1,),'b'):[[1]],
			((1,),'a'):[[2]],
			#((2,),'b'):[[2]],
			((2,),'b'):[[2],[3]],
			((2,),'a'):[[0]],
			((3,),'b'):[[3]],
			((3,),'a'):[[0]]
		}

A.create(alphabet=['a','b'], etats=[['0'], ['1'], ['2'], ['3']], etats_initiaux=[['0']], etats_finaux=[['3']], transitions = A_transitions)

# j'instancie la classe et je cree un automate B (la c'est comme un automate qu'on a minimisé)
B = Automate()

# exemple de ce à quoi doit ressembler le dictionnaire des transitions
B_transitions = {
			(('1-6',),'b'):[['1-6']],
			(('1-6',),'a'):[['2-7']], 
			(('2-7',),'b'):[['2-7']],
			(('2-7',),'a'):[['3-8']],
			(('3-8',),'b'):[['3-8']],
			(('3-8',),'a'):[['4-9']],
			(('4-9',),'b'):[['4-9']],
			(('4-9',),'a'):[['0-5']],
			(('0-5',),'b'):[['0-5']]
		}

B.create(alphabet=['a','b'], etats=[['1-6'], ['2-7'], ['3-8'], ['4-9'], ['0-5']], etats_initiaux=[['1-6']], etats_finaux=[['0-5']], transitions = B_transitions)

print(B)
"""
