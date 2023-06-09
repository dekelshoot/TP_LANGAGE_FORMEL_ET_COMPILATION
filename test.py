from base import *
from util import *

create_automate_complementaire()

A = read("Automate_loop.af")
B = read("Automate_condition.af")
C = read("Automate_int.af")
F = read("Automate_operator.af")

D = A+B+C+F


save(D, "D.af")
to_png(D, "D.png")

texte = "if a = 5 then 124 else 324"
print(reconnaissance_texte(D, texte))
# print(A.alphabet, "\n", A.etats, "\n", A.etats_initiaux,
#       "\n", A.etats_finaux, "\n", A.transitions)
# print(D.alphabet, "\n", D.etats, "\n", D.etats_initiaux,
#       "\n", D.etats_finaux, "\n", D.transitions)
