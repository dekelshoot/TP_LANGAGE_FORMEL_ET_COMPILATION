from symtable import Symbol
from base import Automate



def definir() -> Automate:
    
    A = Automate()
    
    # definition de l'alphabet

    taille_alphabet = int(input("Entrez le nombre de symbole de l'alphabet: "))
    i=0
    while i < taille_alphabet:
        
        char = input(" entrez le symbole numero " + str(i+1) + ": \t")
        if not  A.valider_symbole(char):
            A.ajouter_symbole(char)
            i = i + 1

        else:

            print("symbole deja present.")
    



    return A

print(definir())