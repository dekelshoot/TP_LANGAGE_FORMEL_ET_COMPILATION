# TP_LANGAGE_FORMEL_ET_COMPILATION.pdf

   ## Département d’informatique
   ## Tp Examen Langage Formel et Compilation
   ## 2022 - 2023  

## Objectif: 
  Fournir un outil de manipulation d’automates et s’en servir pour la reconnaissances de tokens dans un texte source.
## I- Vers l’analyse Lexical
### 1. Construction d’un AFD minimal. 
L’outil permettra :
#### a. A l’utilisateur d’entrer les données correspondant à un automate (alphabet, ensemble d’états, l’état initial(ou les états s’il y en a plusieurs), l’état
final(ou les états finaux s’il y en a plusieurs), la fonction de transition);
#### b. de dire si l’automate entrée est un AFD, AFN ou ε-AFN,
#### c. de Déterminiser l’automate entré
#### d. De minimiser l’automate l’automate entré
### 2. Reconnaissance des mots.
Étant donné un texte source constitué de mots séparés par un séparateur (au choix), l’outil devra dire si chaque mot est reconnu ou
non par l’automate.
### 3. Vers l’analyse lexicale: 
Étant donné un texte source, on voudrait maintenant
reconnaitre des mots issus d’automates différents. Pour cela, ajouter dans votre outil une fonction permettant de faire l’union de deux automates et d’afficher l’AFD
résultat. Utiliser cette dernière fonction pour permettre à votre outil de reconnaitre
dans un texte source des mots issus de deux, trois ou quatre automates différents.
### 4. Tests:
À la question 1, vous pourrez utiliser n’importe quel automate pour tester.
Aux quetions 2 et 3, vous utiliserez un texte similaire au suivant : if a = 5 then 124
else 324 .


Si l’on suppose que l’automate considéré ne reconnait que des entiers et que le
REPUBLIQUE DU CAMEROUN
Paix – Travail – Patrie
- . - . - . -
UNIVERSITÉ DE YAOUNDÉ I
Faculté des Sciences
Département d'Informatique
B.P. 812 Yaoundé
REPUBLIC OF CAMEROON
Peace – Work – Fatherland
- . - . - . -
UNIVERSITY OF YAOUNDÉ I
Faculté des Sciences
Department of Computer Science
P.O.Box 812 Yaoundé
séparateur est l’espace, votre outil pourra sortir la séquence suivante (question 2) :
 <if:unknow><a:unknow><=:unknow><5:int><then:unknow><124:int><else:unknow><324:int>
Si en plus des entiers, votre outil reconnait les opérateurs, la sortie sera similaire à
ceci (question 3) :
<if:unknow><a:unknow><=:operator><5:int><then:unknow><124:int><else:unknow><324:int>
L’outil pourra être capable de reconnaitre les entiers, les opérateurs et mêmes les
variables :
<if:unknow><a:var><=:operator><5:int><then:unkknow><124:int><else:unknow><324:int>
II- Langage des commentaires
Produire un outil qui permet la reconnaissance des commentaires dans texte
donné. les commentaires ont la forme : / ∗ w ∗ /, où le commentaire proprement
dit w ne peut pas contenir le facteur ∗/, sauf si il est immédiatement précédé du
caractère d’échappement %. Vous définirez vous même votre alphabet.
CONSIGNES:
• Le travail se fera par groupe de 5;
• Les devoirs zippés (requirements, readme, code source, rapport) seront envoyés à l’adresse mail kouamojulesquentin@gmail.com au plus tard le vendredi 9 juin 2023 à 23h59;
• La présentation se fera le SAMEDI 10 JUIN 2023 à 9H00, chaque groupe muni
de son rapport imprimé;
• Le(s) langage(s) et les technologies sont laissés au choix. 
