# import base
# import util
# A = base.Automate()
# A.ajouter_symbole("a")
# A.ajouter_symbole("b")
# A.ajout_etat(["1"], initial=True)
# A.ajout_etat(["2",], final=True)
# A.ajout_transition(["1"], "a", ["1"])
# A.ajout_transition(["1"], "b", ["2"])
# A.ajout_transition(["2"], "b", ["2"])
# util.to_png(A=A)
# print(A)

# import util
# import determinisation
# A = util.read("AF.af")
# B = determinisation.determinisation(A)
# print(B.etats)
# print(B.etats_initiaux)
# print("finaux", B.etats_finaux)
# print("transition" + str(B.transitions))
# util.to_png(A=B)
# print(B)


# import util
# import reconnaissance
# import completion
# import determinisation
# A = util.read("AF.af")
# text = "aaaba"

# B = determinisation.determinisation(A)
# C = completion.completion(B)
# util.to_png(B)


import util
import base
import reconnaissance
import completion
from determinisation import determinisation

A = base.Automate()
B = base.Automate()
A.ajouter_symbole("a")
A.ajouter_symbole("b")

B.ajouter_symbole("a")
B.ajouter_symbole("b")

A.ajout_etat(["0"], initial=True, final=True)
A.ajout_etat(["1",])

B.ajout_etat(["0"], initial=True, final=True)
B.ajout_etat(["1",])

A.ajout_transition(["0"], "b", ["0"])
A.ajout_transition(["0"], "a", ["1"])
A.ajout_transition(["1"], "b", ["1"])
A.ajout_transition(["1"], "a", ["0"])

B.ajout_transition(["0"], "a", ["0"])
B.ajout_transition(["0"], "b", ["1"])
B.ajout_transition(["1"], "b", ["1"])
B.ajout_transition(["1"], "b", ["0"])

# print(A)
# print(B)
C = A+B

print(C)

util.to_png(determinisation(C))
