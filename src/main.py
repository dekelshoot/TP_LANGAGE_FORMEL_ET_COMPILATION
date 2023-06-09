from Automate import Automate
from base import definir, reconnaissance_texte, determine_type
from util import to_png

## CREATION DU MENU

print("=======================TP LANGAGE FORMEL ET COMPILATION=======================")
print("                     -------------------------------------                     ")

def menu():

    print("=======================VERS L'ANALYSE LEXICAL=======================")
    print("                    -------------------------------                 ")

    print(" Avant tout, vous devez definir l'automate \n")
    A = definir()
    options_petit_1(A)

    menu_reconnaissance_mot(A)

    menu_reconnaissance_expression()

    langage_commentaire()

    print("=======================Merci de votre visite=======================")
    print("                     -------------------------                     ")


def langage_commentaire():

    print("=======================LANGAGE DES COMMENTAIRES=======================")
    print("                    -------------------------------                 ")

    A = Automate()
    taille_alphabet = int(input("Entrez le nombre de symbole de l'alphabet: "))
    i = 0
    while i < taille_alphabet:

        char = input(" entrez le symbole numero " + str(i+1) + ": \t")
        if not A.valider_symbole(char):
            A.ajouter_symbole(char)
            i = i + 1
        else:
            print("symbole deja present.")
    
    commentaire = A.get_langage_commentaire()
    print(commentaire)



def options_petit_1(A) :

    print("----------------------1. Construction d'un AFD minimal----------------------")
    print("                      --------------------------------                      ")


    choix_2 = '1'
    while(choix_2 == '1'):
    
        print("\n1. Afficher l'automate ")
        print("2. Determiner la nature de l'automate ")
        print("3. Determiniser l'automate ")
        print("4. Minimiser l'automate ")
        print("\t Que voulez vous faire ??")
        choix = input("\t >> ")

        while choix != '1' and choix != '2' and choix != '3' and choix != '4' :

            print("Veuillez faire un choix valide svp ")
            print("\n Que voulez vous faire ??\n")
            choix = input("\t >> ")
        
        if choix == '1':
            print(A)
        
        if choix == '2':
            print(A.nature())
        
        if choix == '3':
            A.determiniser()
            print("Affichage de l'automate determinisé")
            print(A)
            #to_png(A, filename = "automate_deterministe.png")
            #print("L'automate deterministe a ete sauvegardé au nom de <automate_deterministe.png> dans le dossier <png> du projet")

        
        if choix == '4':
            A.minimiser()
            print("Affichage de l'automate minimal")
            print(A)
            #to_png(A, filename = "automate_minimal.png")
            #print("L'automate deterministe a ete sauvegardé au nom de <automate_minimal.png> dans le dossier <png> du projet")
        
        print("Voulez-vous effectuer une autre action ??")
        print("\t 1. Oui ")
        print("\t 2. Non ")
        choix_2 = input("\t >> ")

        while choix_2 != '1' and choix_2 != '2':

            print("Veuillez faire un choix valide svp ")
            choix = input("\t >> ")


def menu_reconnaissance_mot(A):

    print("----------------------Reconnaissance des phrases avec cet automate----------------------")
    print("                      --------------------------------------------                      ")
    print("Entrez un texte afin de savoir si l'automate reconnait les mots de ce texte (le separateur est l'espace)")
       
    texte = input("\t >> ")

    print(reconnaissance_texte(A, texte))


def menu_reconnaissance_expression():

    print("----------------------Reconnaissance des phrases de la forme < if a = 5 then 124 else 324> ----------------------")
    print("                      --------------------------------------------------------------------                      ")
    print("Entrez l'expression")
       
    expression = input("\t >> ")

    print(determine_type(expression))



menu()