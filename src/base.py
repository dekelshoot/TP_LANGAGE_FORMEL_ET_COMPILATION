# classe automate
from util import to_png, save
from Automate import Automate


# ------fonctions complémentaires------------------------------------------------------------------------------

# 1. determinisation d'un automate
def determinisation(A: Automate) -> Automate:
    """
    Permet de déterminiser l'automate entré en paramètre

    @param A: Automate a derterminiser
    @return Automate déterminiser
    """

    if A.est_deterministe():
        return A

    else:

        tous_les_etats_du_determinise = []
        toutes_les_transitions_du_determinise = {}

        etat_initial_du_determinise = []
        for etat in A.etats_initiaux:
            for num_etat in etat:
                etat_initial_du_determinise.append(num_etat)

        tous_les_etats_du_determinise.append(etat_initial_du_determinise)
        etat_initial_du_determinise = [etat_initial_du_determinise]

        for etat in tous_les_etats_du_determinise:

            for character in A.alphabet:
                nouvel_etat_pour_charactere = []

                for numero_etat in etat:

                    liste_des_etats = A.f_transitions([numero_etat], character)

                    for e in liste_des_etats:
                        for num_etat in e:
                            if num_etat not in nouvel_etat_pour_charactere:
                                nouvel_etat_pour_charactere.append(num_etat)
                if nouvel_etat_pour_charactere not in tous_les_etats_du_determinise:
                    if len(nouvel_etat_pour_charactere) != 0:
                        tous_les_etats_du_determinise.append(
                            nouvel_etat_pour_charactere)

                if len(nouvel_etat_pour_charactere) != 0:
                    toutes_les_transitions_du_determinise[(tuple(etat), character)] = [
                        nouvel_etat_pour_charactere]

        etats_finaux_du_determinise = []
        for etat in tous_les_etats_du_determinise:
            for etat_final in A.etats_finaux:  # ici aussi
                for num_etat in etat_final:
                    if num_etat in etat:
                        if etat not in etats_finaux_du_determinise:
                            etats_finaux_du_determinise.append(etat)
        etats_finaux_du_determinise = etats_finaux_du_determinise

        A_prime = Automate()
        A_prime.create(alphabet=A.alphabet, etats=tous_les_etats_du_determinise, etats_initiaux=etat_initial_du_determinise,
                       etats_finaux=etats_finaux_du_determinise, transitions=toutes_les_transitions_du_determinise)

        return A_prime

# 2. reconnaissance d'un mot par un automate


def reconnaissance_mot(A: Automate, mot: str) -> bool:
    """ Permet de reconnaitre un mot entré en paramètre et renvoie
        un booleen qui dit si le mot est reconnu ou non.

         @param A: l'automate pour la reconnaissance .
         @param mot: le mot a reconnaitre

         @renvoie True si le mot est reconnu et False si non"""

    if A.est_deterministe():

        etat = A.etats_initiaux[0]
        for char in mot:
            if char not in A.alphabet:
                return [False, "unknown"]
            etat = A.f_transitions(etat, char)[0]
            if len(etat) == 0 or etat == ['puit']:
                return [False, "unknown"]
        if etat in A.etats_finaux:
            return [True, A.type]
        return [False, "unknown"]

    else:
        pile = []
        for chaque_etat_initial in A.etats_initiaux:
            pile.append((chaque_etat_initial, 0))

        while len(pile) > 0:
            etat_actuel, indice_actuel_du_mot = pile.pop()
            if indice_actuel_du_mot == len(mot):
                if etat_actuel in A.etats_finaux:
                    return [True, A.type]
            else:
                etats_possibles_pour_cette_transition = A.f_transitions(
                    etat_actuel, mot[indice_actuel_du_mot])
                for chaque_etat in etats_possibles_pour_cette_transition:
                    if len(chaque_etat) != 0 and chaque_etat != ['puit']:
                        pile.append((chaque_etat, indice_actuel_du_mot+1))

        return [False, "unknown"]


# 2 (suite) reconnaissance d'un texte par un automate
def reconnaissance_texte(A: Automate, texte: str, sep=" ") -> list:
    """ Permet de reconnaitre tous les mots d'une phrase entrés en paramètre et renvoie
        un matrice a deux dimensions contituer du mot et d'un booleen qui dit si le mot
        est reconnu ou non.
         @param A: l'automate pour la reconnaissance .
         @param texte: le texte a reconnaitre
         @param sep: le séparateur
         @renvoie une liste de reconnaissance"""

    # sépareation du texte en tokens
    tokens = texte.split(sep)
    token_temp = []
    for token in tokens:
        if len(token) != 0:
            token_temp.append(token)
    tokens = token_temp

    Matrice_reconnaissance = []
    for token in tokens:
        Matrice_reconnaissance.append([token]+reconnaissance_mot(A, token))

    return Matrice_reconnaissance


# 3. completion d'un automate
def completion(A: Automate) -> Automate:
    """
    Permet de completer un Automate.

    @param A: l'automate à completer .
    @renvoie l'automate complété
    """

    if A.est_complet():
        return A

    else:
        A_prime = Automate()
        A_prime = A
        A_prime.etats.append(['puit'])
        for etat in A_prime.etats:
            for char in A_prime.alphabet:
                if (tuple(etat), char) not in A_prime.transitions.keys():
                    A_prime.transitions[(tuple(etat), char)] = [['puit']]

        for char in A_prime.alphabet:
            A_prime.transitions[(tuple(['puit']), char)] = [['puit']]
        return A_prime


# Definition d'un automate avec la console en entrant ses constituabts au clavier
def definir() -> Automate:
    """Definition d'un automate avec la console en entrant ses 
    constituabts au clavier

    @renvoie : L'automate définit
    """
    A = Automate()

    # definition de l'alphabet

    taille_alphabet = int(input("Entrez le nombre de symbole de l'alphabet: "))
    i = 0
    while i < taille_alphabet:

        char = input(" entrez le symbole numero " + str(i+1) + ": \t")
        if not A.valider_symbole(char):
            A.ajouter_symbole(char)
            i = i + 1

        else:

            print("symbole deja present.")

    # definition des etats  (intiaux et finaux).

    nombre_etats = int(input("\nEntrez le nombre d'etats de l'automate: "))
    i = 0
    bool = True
    while i < nombre_etats:

        if bool == True:
            etat = [
                input(" \nentrez le nom de l'etat numero " + str(i+1) + ": ")]

        if not A.valider_etat(etat):

            if bool == True:
                print(" cet etat est-il initial, final ou intermediaire ? \n  initial -> i , final -> f, intermediaire -> a, initial et final -> if :")
            type = input(str(etat[0]) + ": \t")
            if type == 'i':
                A.ajout_etat(etat, initial=True)
                i = i + 1
            elif type == 'f':
                A.ajout_etat(etat, final=True)
                i = i + 1
            elif type == 'if':
                A.ajout_etat(etat, initial=True, final=True)
                i = i + 1
            elif type == 'a':
                A.ajout_etat(etat)
                i = i + 1
            else:
                print("entrez un choix valide.")
                bool = False

        else:
            print(" etat deja dans la liste des etats de l'automate")

    # definition des transitions.

    for etat in A.etats:

        print(f"\nEtat {etat[0]} :")

        nombre_transitions_partant_de_cet_etat = int(
            input(" entrez le nombre de transitions sortantes de cet etat : "))
        j = 0

        while j < nombre_transitions_partant_de_cet_etat:

            symbole = input(
                f" entrez le symbole de la transition numero {str(j+1)}: ")
            etat_destination = input(
                f" entrez le nom de l'etat destination de la transition numero {str(j+1)}: ")

            retour = A.ajout_transition(etat, symbole,  [etat_destination])

            if retour == True:

                j = j+1

            print(retour)
    save(A, "AF.af")
    to_png(A=A)
    return A

# creation des automates complementaires


def create_automate_complementaire():
    """
        creation des automates complementaires tels que:

            - Automate qui reconnait les entier
            - Automate qui reconnait les opérateurs
        """

    # automate reconnaissant les entiers
    Automate_int = Automate()
    Automate_int.alphabet = alphabets["int"]
    Automate_int.type = "int"
    Automate_int.ajout_etat(["0"], initial=True)
    Automate_int.ajout_etat(["1"], final=True)
    for symbole in Automate_int.alphabet:
        Automate_int.ajout_transition(["0"], symbole, ["1"])
        Automate_int.ajout_transition(["1"], symbole, ["1"])
    save(Automate_int, "Automate_int.af")
    to_png(Automate_int, "Automate_int.png")

    # automate reconnaissant les entiers
    Automate_variable = Automate()
    Automate_variable.alphabet = alphabets["variables"]
    Automate_variable.type = "variable"
    Automate_variable.ajout_etat(["0"], initial=True)
    Automate_variable.ajout_etat(["1"], final=True)
    for symbole in Automate_variable.alphabet:
        Automate_variable.ajout_transition(["0"], symbole, ["1"])

    save(Automate_variable, "Automate_variable.af")
    to_png(Automate_variable, "Automate_variable.png")

    # automate reconnaissant un opérateur
    Automate_operator = Automate()
    Automate_operator.alphabet = alphabets["operators"]
    Automate_operator.type = "operator"
    Automate_operator.ajout_etat(["0"], initial=True)
    Automate_operator.ajout_etat(["1"], final=True)
    for symbole in Automate_operator.alphabet:
        Automate_operator.ajout_transition(["0"], symbole, ["1"])
    save(Automate_operator, "Automate_operator.af")
    to_png(Automate_operator, "Automate_operator.png")

    # automate reconnaissant un conditions
    Automate_condition = Automate()
    Automate_condition.alphabet = alphabets["conditions"]
    Automate_condition.type = "condition"
    Automate_condition.ajout_etat(["0"], initial=True)
    Automate_condition.ajout_etat(["1"])
    Automate_condition.ajout_etat(["2"], final=True)
    Automate_condition.ajout_etat(["3"])
    Automate_condition.ajout_etat(["4"])
    Automate_condition.ajout_etat(["5"])
    Automate_condition.ajout_etat(["6"], final=True)
    Automate_condition.ajout_transition(["0"], "i", ["1"])
    Automate_condition.ajout_transition(["1"], "f", ["2"])
    Automate_condition.ajout_transition(["0"], "e", ["3"])
    Automate_condition.ajout_transition(["3"], "l", ["4"])
    Automate_condition.ajout_transition(["4"], "s", ["5"])
    Automate_condition.ajout_transition(["5"], "e", ["6"])
    save(Automate_condition, "Automate_condition.af")
    to_png(Automate_condition, "Automate_condition.png")

    # automate reconnaissant un boucle
    Automate_loop = Automate()
    Automate_loop.alphabet = alphabets["loops"]
    Automate_loop.type = "loop"
    Automate_loop.ajout_etat(["0"], initial=True)
    Automate_loop.ajout_etat(["1"])
    Automate_loop.ajout_etat(["2"])
    Automate_loop.ajout_etat(["3"], final=True)
    Automate_loop.ajout_etat(["4"])
    Automate_loop.ajout_etat(["5"])
    Automate_loop.ajout_etat(["6"])
    Automate_loop.ajout_etat(["7"])
    Automate_loop.ajout_etat(["8"], final=True)
    Automate_loop.ajout_transition(["0"], "f", ["1"])
    Automate_loop.ajout_transition(["1"], "o", ["2"])
    Automate_loop.ajout_transition(["2"], "r", ["3"])
    Automate_loop.ajout_transition(["0"], "w", ["4"])
    Automate_loop.ajout_transition(["4"], "h", ["5"])
    Automate_loop.ajout_transition(["5"], "i", ["6"])
    Automate_loop.ajout_transition(["6"], "l", ["7"])
    Automate_loop.ajout_transition(["7"], "e", ["8"])
    save(Automate_loop, "Automate_loop.af")
    to_png(Automate_loop, "Automate_loop.png")


# alphabet de qui sera utilisé dans tous le devoir
alphabets = {
    "int": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "boolean": ["T", "r", "u", "e", "F", "a", "l", "s", "e"],
    "operators": ["+", "-", "*", "/", "="],
    "variables": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "conditions": ["i", "f", "e", "l", "s", "e"],
    "loops": ["f", "o", "r",  "w", "h", "i", "l", "e"]
}
