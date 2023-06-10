from base import *
from util import *

# create_automate_complementaire()
# # A = read("AF.af")
# # to_png(A, "A.png")
# # A.minimiser()
# # to_png(A, "minimiser.png")
# A = read("Automate_loop.af")
# B = read("Automate_condition.af")
# C = read("Automate_int.af")
# D = read("Automate_variable.af")
# E = read("Automate_operator.af")

# F = A+B+C+E


# save(F, "F.af")
# to_png(F, "F.png")

# # texte = "if a = 5 then 124 else 324"

# texte = "while b < 10 do b = b + 1"
# print(reconnaissance_texte(F, texte))

# res = reconnaissance_texte(F, texte)

# print("\n\n")
# print(determine_type(res))

A = Automate()

alphabet = ["ε", "a", "b", "c"]
etats = [["0"], ["1"], ["2"], ["3"], ["4"], ["5"],
         ["6"], ["7"], ["8"], ["9"], ["10"], ["11"]]

etats_initiaux = [["0"]]
etats_finaux = [["11"]]

A_transitions = {
    (('0',), 'ε'): [['1'], ['7']],
    (('1',), 'ε'): [['4'], ['2']],
    (('2',), 'a'): [['3']],
    (('3',), 'ε'): [['4'], ['2']],
    (('4',), 'ε'): [['5']],
    (('5',), 'b'): [['6']],

    (('6',), 'ε'): [['11']],
    (('7',), 'a'): [['8']],
    (('8',), 'ε'): [['9']],
    (('9',), 'c'): [['10']],
    (('10',), 'ε'): [['11']],

}

A.create(alphabet, etats, etats_initiaux, etats_finaux, A_transitions)

to_png(A, "A__.png")

A.determiniser()

to_png(A, "A_determiniser.png")

# A.minimiser()

# to_png(A, "minimiser.png")
