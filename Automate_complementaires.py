from base import Automate, alphabets
from util import to_png, save
import reconnaissance_texte


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


# automate reconnaissant un opérateur
Automate_operator = Automate()
Automate_operator.alphabet = alphabets["operators"]
Automate_operator.type = "operators"
Automate_operator.ajout_etat(["0"], initial=True)
Automate_operator.ajout_etat(["1"], final=True)
for symbole in Automate_operator.alphabet:
    Automate_operator.ajout_transition(["0"], symbole, ["1"])
save(Automate_operator, "Automate_operator.af")

# automate reconnaissant un booleen
Automate_boolean = Automate()
Automate_boolean.alphabet = alphabets["boolean"]
print(alphabets["boolean"])
Automate_boolean.type = "boolean"
Automate_boolean.ajout_etat(["0"], initial=True)
Automate_boolean.ajout_etat(["1"])
Automate_boolean.ajout_etat(["2"])
Automate_boolean.ajout_etat(["3"])
Automate_boolean.ajout_etat(["4"], final=True)
Automate_boolean.ajout_etat(["5"])
Automate_boolean.ajout_etat(["6"])
Automate_boolean.ajout_etat(["7"])
Automate_boolean.ajout_etat(["8"])
Automate_boolean.ajout_etat(["9"], final=True)
Automate_boolean.ajout_transition(["0"], "T", ["1"])
Automate_boolean.ajout_transition(["1"], "r", ["2"])
Automate_boolean.ajout_transition(["2"], "u", ["3"])
Automate_boolean.ajout_transition(["3"], "e", ["4"])
Automate_boolean.ajout_transition(["0"], "F", ["5"])
Automate_boolean.ajout_transition(["5"], "a", ["6"])
Automate_boolean.ajout_transition(["6"], "l", ["7"])
Automate_boolean.ajout_transition(["7"], "s", ["8"])
Automate_boolean.ajout_transition(["8"], "e", ["9"])
save(Automate_boolean, "Automate_boolean.af")


texte = ": if a = 5 then True 124 else 324"
to_png(Automate_int, filename="Automate_int.png")
print(Automate_int)
print(reconnaissance_texte.reconnaissance_texte(Automate_int, texte))
