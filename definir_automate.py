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
    

    # definition des etats  (intiaux et finaux).

    nombre_etats = int(input("\nEntrez le nombre d'etats de l'automate: "))
    i=0 ; bool = True
    while i < nombre_etats:

        if bool == True:
            etat = [input(" \nentrez le nom de l'etat numero " + str(i+1) + ": ")]

        if not  A.valider_etat(etat):

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

        nombre_transitions_partant_de_cet_etat = int(input(" entrez le nombre de transitions sortantes de cet etat : "))
        j=0

        while j < nombre_transitions_partant_de_cet_etat:
        
            symbole = input(f" entrez le symbole de la transition numero {str(j+1)}: ")
            etat_destination = input(f" entrez le nom de l'etat destination de la transition numero {str(j+1)}: ")

            retour = A.ajout_transition(etat, symbole,  [etat_destination])
            
            if retour == True :
                
                j = j+1

            print(retour)

    return A

print(f"\n{definir()}")