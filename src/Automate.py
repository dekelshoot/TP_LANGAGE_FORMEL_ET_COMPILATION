class Automate():

    """
    Ce qu'il faut savoir de la classe Automate() :

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
        self.type = "unknow"

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
            if trans[1] == 'ε':
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

        if len(self.etats) == 0 or len(self.alphabet) == 0:
            return False

        for trans in self.transitions.keys():
            if trans[1] == 'ε':
                return False

        return True

    # fonction permettant de savoir si un automate est complet
    def est_complet(self) -> bool:

        for etat in self.etats:
            for char in self.alphabet:
                if (tuple(etat), char) not in self.transitions.keys():
                    return False

        if len(self.etats) == 0 or len(self.alphabet) == 0:
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

    # determinisation d'un automate

    def determiniser(self):

        if self.est_epsilone_non_deterministe:
            self.passer_de_epsilonne_afn_a_afn()

        if self.est_non_deterministe():

            tous_les_etats_du_determinise = []
            toutes_les_transitions_du_determinise = {}

            etat_initial_du_determinise = []
            for etat in self.etats_initiaux:
                for num_etat in etat:
                    etat_initial_du_determinise.append(num_etat)

                    # print(f"l'etat initial du determinise est : {etat_initial_du_determinise}")
            tous_les_etats_du_determinise.append(etat_initial_du_determinise)
            etat_initial_du_determinise = [etat_initial_du_determinise]
            # print(f"tous les etats de l'automate a l'heure actuelle {tous_les_etats_du_determinise}")

            for etat in tous_les_etats_du_determinise:
                # print(f"Avec l'etat {etat} ")
                for character in self.alphabet:
                    nouvel_etat_pour_charactere = []
                    # print(f"Avec le symbole {character} ")
                    for numero_etat in etat:

                        liste_des_etats = self.f_transitions(
                            [numero_etat], character)

                        # print(f"de l'etat {numero_etat} de la liste {etat} avec le symbole {character} on arrive a {liste_des_etats} ")

                        for e in liste_des_etats:
                            for num_etat in e:
                                if num_etat not in nouvel_etat_pour_charactere:
                                    nouvel_etat_pour_charactere.append(
                                        num_etat)

                                    # print(f"Le nouvel etat 	qu'on forme alors avec {etat} et {character} est {nouvel_etat_pour_charactere}")

                    if nouvel_etat_pour_charactere not in tous_les_etats_du_determinise:
                        if len(nouvel_etat_pour_charactere) != 0:
                            tous_les_etats_du_determinise.append(
                                nouvel_etat_pour_charactere)
                            # print(f"Comme {nouvel_etat_pour_charactere} n'est pas encore dans la liste des etats, je l'ajoute et la liste des etats devient {tous_les_etats_du_determinise} ")

                    if len(nouvel_etat_pour_charactere) != 0:
                        toutes_les_transitions_du_determinise[(tuple(etat), character)] = [
                            nouvel_etat_pour_charactere]
                        # print(f"J'ajoute donc aussi la transition allant de {etat} avec {character}, pour aller a {nouvel_etat_pour_charactere} ")
                        # print(f"l'ensemble des transitions de l'automate est donc deja {toutes_les_transitions_du_determinise}")

            etats_finaux_du_determinise = []
            for etat in tous_les_etats_du_determinise:
                for etat_final in self.etats_finaux:
                    for num_etat in etat_final:
                        if num_etat in etat:
                            if etat not in etats_finaux_du_determinise:
                                etats_finaux_du_determinise.append(etat)
            etats_finaux_du_determinise = etats_finaux_du_determinise

            self.etats_initiaux = etat_initial_du_determinise
            self.etats_finaux = etats_finaux_du_determinise
            self.etats = tous_les_etats_du_determinise
            self.transitions = toutes_les_transitions_du_determinise

    def trouver_classe(self, dictionnaire, liste):

        liste = tuple(liste)
        for cle in dictionnaire.keys():
            if all(element in cle for element in liste):
                return cle
        return None

    def minimiser(self):

        if not self.est_deterministe():
            self.determiniser()
            """print(self)
            print(self.etats)
            nb_etats = len(self.etats)
            for etat in self.etats:
                nb_etats = nb_etats - 1
                print(etat)
                self.renommer_etat(",".join(etat), str(nb_etats))
            print("self")
            print(self)"""

        non_finaux = [x for x in self.etats if x not in self.etats_finaux]
        pie = [non_finaux, self.etats_finaux]
        nouvelles_classes_equivalence = []
        if not any(len(classe) == 0 for classe in pie):
            while pie != nouvelles_classes_equivalence:

                # si toutes les classes s'ont chacunes qu'un seul etat, pas besoin de chercher a les scinder
                if all(len(sublist) == 1 for sublist in pie):
                    print("je suis dans le cas boquant")
                    nouvelles_classes_equivalence = pie
                    print(pie, "pie")
                    print(nouvelles_classes_equivalence,
                          "nouvelles classes d'equivalence")
                    dictionnaire_nouvelles_classes_equivalence = {tuple(
                        element for sous_liste in classe for element in sous_liste): [] for classe in pie}
                    break

                for classe_equivalence in pie:
                    if len(classe_equivalence) > 1:
                        # print("la calsse d'equivalence est ", classe_equivalence)
                        dictionnaire_nouvelles_classes_equivalence = {tuple(
                            element for sous_liste in classe for element in sous_liste): [] for classe in pie}
                        dictionnaire_nouvelles_classes_equivalence_copy = str(
                            dictionnaire_nouvelles_classes_equivalence)

                        for symbole in self.alphabet:

                            dictionnaire_nouvelles_classes_equivalence = eval(
                                dictionnaire_nouvelles_classes_equivalence_copy)
                            # print("le dictionnaire au debut est ", dictionnaire_nouvelles_classes_equivalence)
                            # print("quand je suis su le symole ", symbole)
                            for etat in classe_equivalence:
                                # print(f"etat {etat} de la classe {classe_equivalence}")
                                etat_arrive = self.f_transitions(etat, symbole)
                                # print(f"etat {etat} de la classe {classe_equivalence} avec le smbole {symbole} me mene a {etat_arrive}")

                                if len(etat_arrive) != 0:
                                    classe = self.trouver_classe(
                                        dictionnaire_nouvelles_classes_equivalence, etat_arrive[0])

                                    dictionnaire_nouvelles_classes_equivalence[classe].append(
                                        etat)
                                    # print(f"comme cest non vide et que etat errive {etat_arrive} est dans la classe {classe_equivalence} alors j'ajoute l'etat {etat} dans le dictionnaire")
                                    # print(f" et le dictionnaire devient {dictionnaire_nouvelles_classes_equivalence}")
                                else:

                                    # print(f"comme etat arrive est vide  je recommence")
                                    break

                            taille_nouvelle_classe_equivalence = sum(
                                bool(classe) for classe in dictionnaire_nouvelles_classes_equivalence.values())
                            if taille_nouvelle_classe_equivalence > 1:
                                # print(" la taille de la nouvelle classe d'equivalence avec le symbole ", symbole, " est",taille_nouvelle_classe_equivalence)
                                break

                        for classe in dictionnaire_nouvelles_classes_equivalence.values():
                            if classe:
                                nouvelles_classes_equivalence.append(classe)

                        # print(pie, "SEP", classe_equivalence, "PIE ET CLASSE EQUIVALENCE")
                        ce_qui_etait_la_quon_a_pas_scinde = [
                            x for x in pie if x != classe_equivalence]
                        # print("ce qu'on a pas scinde", ce_qui_etait_la_quon_a_pas_scinde)
                        nouvelles_classes_equivalence.extend(
                            ce_qui_etait_la_quon_a_pas_scinde)

                        # print(f"les nouvelles classes d'equivalences que je forme apres parcours de la classe {classe_equivalence} sont {nouvelles_classes_equivalence}")
                        if nouvelles_classes_equivalence != pie:
                            pie = nouvelles_classes_equivalence
                            nouvelles_classes_equivalence = []
                            break
                        else:
                            dictionnaire_nouvelles_classes_equivalence = {tuple(
                                element for sous_liste in classe for element in sous_liste): [] for classe in pie}
                            break

            print(
                f"les classes d'equivalences finales sont : {nouvelles_classes_equivalence}")

            # Construction de l'automate minimisé
            automate_minimise = Automate()

            # Ajout de l'alphabet
            for symbole in self.alphabet:
                automate_minimise.ajouter_symbole(symbole)

            # Parcours des nouvelles classes d'équivalence
            for classe in pie:
                nouvel_etat = ["=".join(["=".join(etat) for etat in classe])]
                automate_minimise.ajout_etat(nouvel_etat)

                # Si la classe contient un état initial, on le définit comme état initial dans l'automate minimisé
                if any(etat in self.etats_initiaux for etat in classe):
                    automate_minimise.etats_initiaux = [nouvel_etat]

                # Si la classe contient un état final, on le définit comme état final dans l'automate minimisé
                if any(etat in self.etats_finaux for etat in classe):
                    automate_minimise.etats_finaux.append(nouvel_etat)

                # Parcours de l'alphabet pour la construction des transitions
                for symbole in self.alphabet:
                    # On prend le premier état de la classe dequivalence
                    etat_arrive = self.f_transitions(classe[0], symbole)
                    if etat_arrive:
                        nouvelle_classe = self.trouver_classe(
                            dictionnaire_nouvelles_classes_equivalence, etat_arrive[0])
                        nouvel_etat_arrive = [
                            "=".join([etat for etat in nouvelle_classe])]
                        automate_minimise.ajout_etat(nouvel_etat_arrive)
                        automate_minimise.ajout_transition(
                            nouvel_etat, symbole, nouvel_etat_arrive)

            # Affectation de l'automate minimisé à l'automate actuel
            self.alphabet = automate_minimise.alphabet
            self.etats = automate_minimise.etats
            self.etats_initiaux = automate_minimise.etats_initiaux
            self.etats_finaux = automate_minimise.etats_finaux
            self.transitions = automate_minimise.transitions

    def recuperer_epsilonne_fermeture(self, etat: list) -> list:
        """
                fonction permettant d'avoir les epsilones fermetures d'un etat
                @param etat : l'etat dont on veut son epsilonne fermeture
                """
        if not self.est_epsilone_non_deterministe():
            return []
        else:
            liste_epsilonnes_fermetures = [etat]
            symbole = 'ε'
            for etat in liste_epsilonnes_fermetures:
                for trans in self.transitions:
                    if list(trans[0]) == etat and trans[1] == symbole:
                        liste_epsilonnes_fermetures.extend(
                            self.transitions[trans])
            return liste_epsilonnes_fermetures

    def passer_de_epsilonne_afn_a_afn(self):

        if not self.est_non_deterministe():

            for etat in self.etats:
                e_fermeture_de_etat = self.recuperer_epsilonne_fermeture(etat)
                for symbole in self.alphabet:
                    etats_pour_lesquelles_je_dois_creer_de_nouvelles_transitions = []
                    if symbole != 'ε':
                        for e_etat in e_fermeture_de_etat:
                            etat_arrives = self.f_transitions(e_etat, symbole)
                            if etat_arrives:
                                etats_pour_lesquelles_je_dois_creer_de_nouvelles_transitions.extend(
                                    etat_arrives)
                        for ces_etats in etats_pour_lesquelles_je_dois_creer_de_nouvelles_transitions:
                            self.ajout_transition(etat, symbole, ces_etats)

            symbole = 'ε'
            transitions_copy = list(self.transitions.keys())
            for trans in transitions_copy:
                etat, symbole_transition = trans
                if symbole_transition == symbole:
                    del self.transitions[trans]

            if symbole in self.alphabet:
                self.alphabet.remove(symbole)

    def create(self, alphabet: list, etats: list, etats_initiaux: list, etats_finaux: list, transitions: dict, type="unknow"):
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
        self.type = type

    def ajout_transition(self, etat_depart: list, symbole: str, etat_arrive: list) -> bool:

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
            # print("transition deja presente dans l'automate")
            return False

    # Ajout du type a l'automate
    def ajout_type(self, type: str):

        self.type = type

    def nature(self) -> str:

        nature = []

        if self.est_epsilone_non_deterministe():
            nature.append("ε-AFN")

        if self.est_non_deterministe():
            nature.append("AFN")

        if self.est_deterministe():
            nature.append("AFD")

        if self.est_complet():
            nature.append("Complet")

        if len(nature) == 0:
            nature = ['non correctement defini.']

        return "Cet automate est : " + ", ".join(nature)

    def renommer_etat(self, ancien_nom: str, nouveau_nom: str):

        self.etats[self.etats.index([ancien_nom])] = [nouveau_nom]

        if [ancien_nom] in self.etats_initiaux:
            self.etats_initiaux[self.etats_initiaux.index([ancien_nom])] = [
                nouveau_nom]

        if [ancien_nom] in self.etats_finaux:
            self.etats_finaux[self.etats_finaux.index([ancien_nom])] = [
                nouveau_nom]

        transitions_copy = list(self.transitions.keys())
        for transition in transitions_copy:
            etat_origine, symbole = transition
            etats_destinations = self.transitions[transition]

            if etat_origine == (ancien_nom,):
                nouveau_etat_origine = (nouveau_nom,)
            else:
                nouveau_etat_origine = etat_origine

            self.transitions[nouveau_etat_origine,
                             symbole] = etats_destinations

            del self.transitions[transition]

            nouveaux_etats_destinations = []
            for etat in etats_destinations:
                if etat == [ancien_nom]:
                    nouveau_etat = [nouveau_nom]
                else:
                    nouveau_etat = etat

                nouveaux_etats_destinations.append(nouveau_etat)

            self.transitions[nouveau_etat_origine,
                             symbole] = nouveaux_etats_destinations

    # Afficher de facon commode un automate

    def __str__(self):
        """
        Affichage de facon propre l'objet automate
        """

        intermediaires = list(set([element for sublist in self.etats for element in sublist]) - set(
            [element for sublist in self.etats_initiaux for element in sublist]) - set([element for sublist in self.etats_finaux for element in sublist]))

        ret = self.nature() + "\n"
        ret += "   - alphabet   : {" + ", ".join(self.alphabet) + "} \n"
        ret += "   - initiaux      : " + \
            ", ".join(["(%s)" % ",".join(init)
                       for init in self.etats_initiaux]) + "\n"
        ret += "   - etats intermediaires : " + \
            ", ".join(f"({element})" for element in intermediaires) + "\n"
        ret += "   - finaux    : " + \
            ", ".join(["(%s)" % ",".join(init)
                       for init in self.etats_finaux]) + "\n"
        ret += "   - nombre d'etats : %d \n" % (len(self.etats))
        ret += "   - transitions :\n"
        for etat in self.etats:
            ret += "       Partant de l'état (%s): \n" % (",".join(etat))
            for symbole in self.alphabet:

                if not len(self.f_transitions(etat, symbole)) == 0:
                    for dest in self.f_transitions(etat, symbole):
                        ret += "          en lisant le symbole (%s) on arrive à l'état (%s)\n" % (
                            symbole, ",".join(dest))

        return ret

    # surcharge de l'opération d'addition

    def __add__(self, other):
        """
        surchage de l'opération d'addition  qui permet d'additionner deux atomates
        ex: Automate_1 + Automate_2 = Automate_
        @param other: deuxieme authomate
        """

        for etat in other.etats:
            if etat in self.etats:
                other.renommer_etat(",".join(etat), ",".join(etat) + "-2")

        tous_les_etats_de_union = []
        toutes_les_transitions_union = {}
        nouvel_alphabet = list(set(self.alphabet + other.alphabet))

        etat_initial_union = []
        for etat in self.etats_initiaux:
            for num_etat in etat:
                etat_initial_union.append(num_etat)

        for etat in other.etats_initiaux:
            for num_etat in etat:
                etat_initial_union.append(num_etat)

        tous_les_etats_de_union.append(etat_initial_union)
        etat_initial_union = [etat_initial_union]

        for etat in tous_les_etats_de_union:

            for character in nouvel_alphabet:

                nouvel_etat_pour_charactere = []

                for numero_etat in etat:

                    liste_des_etats = self.f_transitions(
                        [numero_etat], character)
                    if len(liste_des_etats) == 0:
                        liste_des_etats = other.f_transitions(
                            [numero_etat], character)

                    for e in liste_des_etats:
                        for num_etat in e:
                            if num_etat not in nouvel_etat_pour_charactere:
                                nouvel_etat_pour_charactere.append(num_etat)

                if nouvel_etat_pour_charactere not in tous_les_etats_de_union:
                    if len(nouvel_etat_pour_charactere) != 0:
                        tous_les_etats_de_union.append(
                            nouvel_etat_pour_charactere)

                if len(nouvel_etat_pour_charactere) != 0:
                    toutes_les_transitions_union[(tuple(etat), character)] = [
                        nouvel_etat_pour_charactere]

        etats_finaux_de_union = []
        for etat in tous_les_etats_de_union:
            for etat_final in self.etats_finaux:
                for num_etat in etat_final:
                    if num_etat in etat:
                        if etat not in etats_finaux_de_union:
                            etats_finaux_de_union.append(etat)

            for etat_final in other.etats_finaux:
                for num_etat in etat_final:
                    if num_etat in etat:
                        if etat not in etats_finaux_de_union:
                            etats_finaux_de_union.append(etat)

        etats_finaux_de_union = etats_finaux_de_union

        res = Automate()
        res.create(nouvel_alphabet, tous_les_etats_de_union, etat_initial_union,
                   etats_finaux_de_union, toutes_les_transitions_union)

        res = normalise_Automate(res)

        return res

    def get_langage_commentaire(self):
        """
        Langage commentaire est une fonction qui retourne un automate 
                qui reconnais les commentaires d'un langage
                """
        A = Automate()
        A.alphabet = self.alphabet
        special_char = ["*", "/", "%"]
        A.alphabet += special_char

        A.ajout_etat(["0"], initial=True)
        A.ajout_etat(["1"])
        A.ajout_etat(["2"])
        A.ajout_etat(["3"])
        A.ajout_etat(["4"])
        A.ajout_etat(["5"])
        A.ajout_etat(["6"])
        A.ajout_etat(["7",], final=True)

    # debut du commentaierz*e
        A.ajout_transition(["0"], "/", ["1"])
        A.ajout_transition(["1"], "*", ["2"])

        for symbole in A.alphabet:
            if symbole not in special_char:
                A.ajout_transition(["2"], symbole, ["2"])
                A.ajout_transition(["5"], symbole, ["2"])

    # echapement du commentaire
        A.ajout_transition(["2"], "%", ["3"])
        A.ajout_transition(["3"], "*", ["4"])
        A.ajout_transition(["4"], "/", ["5"])

    # fin du commentaire
        A.ajout_transition(["2"], "*", ["6"])
        A.ajout_transition(["6"], "/", ["7"])

        return A


def normalise_Automate(A):
    """cest une fonction qui renome tous les etats de l'automate passé en paramètre
    de 0 à l'infini
    @param A: Automate passé en paramètre
    @return Automate normalisé
    """
    etats = []
    transitions = {}
    for i, etat in enumerate(A.etats_initiaux):
        A.etats_initiaux[i] = [str(A.etats.index(etat))]

    for i, etat in enumerate(A.etats_finaux):
        A.etats_finaux[i] = [str(A.etats.index(etat))]

    for key in A.transitions.keys():
        transitions.update({((str(A.etats.index(list(key[0]))),), key[1]): [
                           [str(A.etats.index(A.transitions[key][0]))]]})
    A.transitions = transitions

    for i, etat in enumerate(A.etats):
        etats.append([str(A.etats.index(etat))])
    A.etats = etats

    return A
