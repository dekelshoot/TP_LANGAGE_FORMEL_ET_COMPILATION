
from base import Automate
from reconnaissance import reconnaissance
import util
# reconnaissance d'un texte par un automate


def reconnaissance_texte(A: Automate, texte: str, sep=" ") -> list:
    """ Permet de reconnaitre tous les mots d'une phrase dentrée en paramètre et renvoie
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
        Matrice_reconnaissance.append([token, reconnaissance(A, token)])

    return Matrice_reconnaissance


texte = " aa aab ab bba je suis Dekel Shoot   "
A = util.read("AF.af")
print(reconnaissance_texte(A=A, texte=texte))
