from subprocess import call
from base import Automate


def read(filename):
    """ Lire le AF spécifié à partir d'un fichier.
         Un AF peut être sauvegardé avec la fonction 'save'.
         @param filename le fichier dans lequel le DFA est stocké.
         @return le AF du fichier.
        """
    local_dict = locals()
    with open(filename, "r") as file:
        exec(compile(open(filename).read(), filename, 'exec'), globals(), local_dict)

    return local_dict["a"]


def save(af: Automate, filename):
    """ Enregistrez le AF spécifié dans un fichier.
         Un DFA peut être lu avec la fonction 'read'.
         @param dfa le DFA à sauvegarder
         @param filename le nom du fichier dans lequel
        l'automate sera sauvé."""
    txt = "a = Automate()\n\n"

    # Ajout de l'alphabet
    for symbole in af.alphabet:
        txt += "a.ajouter_symbole(symbole = \"" + symbole + "\")\n\n"

    # Ajout des états
    for etat in af.etats:
        if etat in af.etats_finaux:
            txt += "a.ajout_etat(etat = ['" + \
                str(etat[0]) + "'] , final =True)\n\n"

        if etat in af.etats_initiaux:
            txt += "a.ajout_etat(etat = ['" + \
                str(etat[0]) + "'] , initial =True)\n\n"
        if etat not in af.etats_finaux and etat not in af.etats_initiaux:
            txt += "a.ajout_etat(etat = ['"+str(etat[0]) + "'] , )\n\n"

    # Ajout des transitions
    for etat in af.etats:
        for symbole in af.alphabet:
            if (tuple(etat), symbole) in af.transitions.keys():
                i = 0
                for arrive_etat in af.transitions[(tuple(etat), symbole)]:
                    txt += "a.ajout_transition( ['"+str(etat[0]) + "'] , \"" + str(symbole) + "\" , " + str(af.f_transitions(
                        etat, symbole)[i])+")\n"
                    i += 1

    # Création du fichier de sauvegarde
    with open(filename, "w") as file:
        file.write(txt)


def to_dot(A: Automate, name="Graph"):
    """ Renvoie une chaîne correspondant au AF spécifié au format DOT.
         @param AF le AF à convertir au format DOT.
         @param name le nom de l'automate pour le fichier DOT ("Graph") par défaut.
         @renvoie l'automate au format DOT."""
    ret = "digraph " + name + " {\n    rankdir=\"LR\";\n\n"
    ret += "    // States (" + str(len(A.etats)) + ")\n"

    def state_name(s): return "Q_" + str(A.etats.index(s))

    # States
    ret += "    node [shape = point ];     __Qi__ // Initial state\n"
    for etat in A.etats:
        ret += "    "
        if etat in A.etats_finaux:
            ret += "node [shape = doublecircle]; "
        else:
            ret += "node [shape = circle];       "
        ret += state_name(etat) + " [label = \" " + ",".join(etat) + " \"];\n"

    # Transitions
    ret += "\n    // Transitions\n"
    for etat in A.etats_initiaux:
        ret += "    __Qi__ -> " + \
            state_name(etat) + "; // Initial state arrow\n"
    for etat in A.etats:
        for symbole in A.alphabet:
            if (tuple(etat), symbole) in A.transitions.keys():
                i = 0
                for arrive_etat in A.transitions[(tuple(etat), symbole)]:
                    ret += "    " + state_name(etat) + " -> " + state_name(A.f_transitions(
                        etat, symbole)[i]) + " [label = \"" + ",".join(symbole) + " \"];\n"
                    i += 1
    return ret + "}\n"


def to_png(A: Automate, filename=None, name="Graph"):
    """ Créer l'image PNG correspondant à la représentation du
         DFA spécifié dans un fichier.
         L'automate est converti au format DOT et la commande point s'appelle
         afin de générer le PNG.
         @param dfa le DFA à convertir en PNG.
         @param name le nom du graphe.
         @param filename le nom du fichier PNG, utilisez le nom du graphique si
             non spécifié. """

    if filename is None:
        filename = name + ".png"

    tmp_file = filename + ".tmp"
    with open(tmp_file, "w") as file:
        file.write(to_dot(A, name))

    call(("dot -Tpng " + tmp_file + "  -o " + filename).split(" "))
    call(("rm " + tmp_file).split(" "))
