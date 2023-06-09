from base import *
from util import *

create_automate_complementaire()
# A = read("AF.af")
# to_png(A, "A.png")
# A.minimiser()
# to_png(A, "minimiser.png")
A = read("Automate_loop.af")
B = read("Automate_condition.af")
C = read("Automate_int.af")
D = read("Automate_variable.af")
E = read("Automate_operator.af")
print(A.type)
F = A+B+C+E


save(F, "F.af")
to_png(F, "F.png")

texte = "if a = 5 then 124 else 324"
print(reconnaissance_texte(F, texte))

res = reconnaissance_texte(F, texte)

print(determine_type(res))
