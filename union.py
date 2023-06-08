# classe automate
import copy
from re import T


from base import B


class Automate():

	"""
	Ce qu'il faut savoir de la calsse Automate() :

	1. L'alphabet est une LISTE de tous les symboles du langage reconnu
	2. L'ensemble des etats, Q, c'est egalement une liste des differents etats de l'automate, donc une LISTE DE LISTE.
	3. L'etat initial, est une LISTE DE LISTE, (d'au moins une liste), si la liste n'a qu'une seule liste alors, 
	alors cet automate n'a qu'un seul etat initial, maintenant si cette une seule liste n'a qu'un seul element, alors l'etat initial
	est un sous ensemble d'un seul etat..
	4. Pareil pour l'etat final.
	5. Un etat qi maintenant est une simple LISTE d'un ou plusieurs elements, si cette liste a un seul element alors cet etat est un 
	sous ensemble d'un seul etat
	6. La fonction de transition prend donc en entree, une liste d'elements, un str ( le symbole ) et retourne une liste de liste, j'explique :
	un etat est materialisé par une liste d'elements, ca peut etre plus d'un element(dans le cas d'un determinisé), 
	le symbole est tout simplement un caractere de l'alphabet à lire. La liste de le liste retournee est tout simplement la liste
	des differents etats ou la transition peut nous emmener, la premiere liste est pour contenir ces differents etats, la deuxieme
	est pour chacun des etats ou ca nous mene
	7. Le dictionnaire transactions est un dictionnaire materialisant les transitions de l'automate, un element du dictionnaire est 
	tel que la cle est un tuple contenant deux elements, le premiere est un tuple, qui a tous les elements de l'etat et l'autre
	element est le symbole lu, maintenant la valeur est est une liste de liste donc la liste des etats aux quels ca mene

	"""

	
	# Constructeur de la classe
	def __init__(self):
		
		self.alphabet = []
		self.etats = []
		self.etats_initiaux = []
		self.etats_finaux = []
		self.transitions = {}

	
	# fonction de transition
	def f_transitions(self, etat:list, symbole:str) -> list:

		for trans in self.transitions: # je parcours les transitions
			if list(trans[0]) == etat and trans[1] == symbole: # si je tombe sur un transition telle que l'etat est celui que je passe en entree, et le symbole ce lui que je passe en entree
				return self.transitions[trans] # alors je prends l'etat au quel ca mene et je le retourne
		return []


	# fonction permettant de savoir si un automate contient des epsilonnes-transitions
	def est_epsilone_non_deterministe(self)->bool:
		
		for trans in self.transitions.keys():
			if trans[1] == 'ε' :
				return True
		return False

	
	# fonction permettant de savoir si un automate est non-deterministe
	def est_non_deterministe(self)->bool:
		
		for trans in self.transitions.values():
			if len(trans) > 1:
				return True
		
		if len(self.etats_initiaux) > 1:
			return True

		return False

	
	# fonction permettant de savoir si un automate est deterministe
	def est_deterministe(self)->bool:
		
		for trans in self.transitions.values():
			if len(trans) > 1:
				return False
	
		if len(self.etats_initiaux) > 1:
			return False

		if len(self.etats) == 0 or len(self.alphabet) == 0:
			return False

		for trans in self.transitions.keys():
			if trans[1] == 'ε' :
				return True

		return True


	# fonction permettant de savoir si un automate est complet
	def est_complet(self)->bool:
		
		for etat in self.etats:
			for char in self.alphabet:
				if (tuple(etat),char) not in self.transitions.keys():
					return False
		
		if len(self.etats) == 0 or len(self.alphabet) == 0:
			return False

		return True


	def ajout_etat(self, etat:list, initial = False, final = False) -> bool:

		"""
		ajout d'un etat dans un automate
		@param state : l'etat que tu veux ajouter dans l'automate (une liste, qui est l'etat)
		@param initial : si True, alors l'etat est un etat initial
		@param final : si True, alors l'etat est un etat final

		"""

		if not etat in self.etats:
			self.etats.append(etat)

			if initial == True:
				self.etats_initiaux.append(etat)

			if final == True:
				self.etats_finaux.append(etat)
				
			return True
		else:
			
			return False


	def valider_symbole(self, symbole:str) -> bool:

		if symbole not in self.alphabet:
			return False
		return True

	
	def ajouter_symbole(self, symbole:str) -> bool:

		if symbole not in self.alphabet:
			self.alphabet.append(symbole)
			return True
		return False
	

	def valider_etat(self, etat:list) -> bool:

		if etat not in self.etats:
			return False
		return True


	# determinisation d'un automate
	def determiniser(self):

		if not self.est_deterministe():
			
			tous_les_etats_du_determinise = []	
			toutes_les_transitions_du_determinise = {}	

			etat_initial_du_determinise = []
			for etat in self.etats_initiaux:
				for num_etat in etat:
					etat_initial_du_determinise.append(num_etat)
			
			tous_les_etats_du_determinise.append(etat_initial_du_determinise)
			etat_initial_du_determinise = [etat_initial_du_determinise]
			
			for etat in tous_les_etats_du_determinise:
				
				for character in self.alphabet:
					nouvel_etat_pour_charactere = []
					
					for numero_etat in etat:
						
						liste_des_etats = self.f_transitions([numero_etat], character)
						
						for e in liste_des_etats: 
							for num_etat in e:
								if num_etat not in nouvel_etat_pour_charactere: nouvel_etat_pour_charactere.append(num_etat)
					if nouvel_etat_pour_charactere not in tous_les_etats_du_determinise:
						if len(nouvel_etat_pour_charactere) != 0:
							tous_les_etats_du_determinise.append(nouvel_etat_pour_charactere)

					if len(nouvel_etat_pour_charactere) != 0:	
						toutes_les_transitions_du_determinise[(tuple(etat),character)]=[nouvel_etat_pour_charactere]
				

			etats_finaux_du_determinise = []
			for etat in tous_les_etats_du_determinise:
				for etat_final in self.etats_finaux: # ici aussi
					for num_etat in etat_final:
						if num_etat in etat:
							if etat not in etats_finaux_du_determinise: etats_finaux_du_determinise.append(etat)
			etats_finaux_du_determinise = etats_finaux_du_determinise
				
			
			self.etats_initiaux = tous_les_etats_du_determinise ; self.etats_finaux = etats_finaux_du_determinise 
			self.etats =  etat_initial_du_determinise ; self.transitions = toutes_les_transitions_du_determinise
		

	def trouver_classe(self, dictionnaire, liste):

		liste = tuple(liste)
		for cle in dictionnaire.keys():
			if all(element in cle for element in liste):
				return cle
		return None


	def minimiser(self):
		
		if not self.est_deterministe():
			self.determiniser()
		
		non_finaux  = [x for x in self.etats if x not in self.etats_finaux]
		pie = [non_finaux, self.etats_finaux]
		nouvelles_classes_equivalence = []

		while pie != nouvelles_classes_equivalence:
			
			for classe_equivalence in pie:
				if len(classe_equivalence)>1:
					print("la calsse d'equivalence est ", classe_equivalence)
					dictionnaire_nouvelles_classes_equivalence = {tuple(element for sous_liste in classe for element in sous_liste): [] for classe in pie}
					dictionnaire_nouvelles_classes_equivalence_copy = str(dictionnaire_nouvelles_classes_equivalence)
					
					for symbole in self.alphabet:
						
						dictionnaire_nouvelles_classes_equivalence = eval(dictionnaire_nouvelles_classes_equivalence_copy)
						print("le dictionnaire au debut est ", dictionnaire_nouvelles_classes_equivalence)
						print("quand je suis su le symole ", symbole)
						for etat in classe_equivalence:
							print(f"etat {etat} de la classe {classe_equivalence}")
							etat_arrive = self.f_transitions(etat, symbole)
							print(f"etat {etat} de la classe {classe_equivalence} avec le smbole {symbole} me mene a {etat_arrive}")
							
							if len(etat_arrive) != 0:
								classe = self.trouver_classe(dictionnaire_nouvelles_classes_equivalence, etat_arrive[0])
								
								dictionnaire_nouvelles_classes_equivalence[classe].append(etat)
								print(f"comme cest non vide et que etat errive {etat_arrive} est dans la classe {classe_equivalence} alors j'ajoute l'etat {etat} dans le dictionnaire")
								print(f" et le dictionnaire devient {dictionnaire_nouvelles_classes_equivalence}")
							else:
								
								print(f"comme etat arrive est vide  je recommence")
								break

						
						i = sum(bool(classe) for classe in dictionnaire_nouvelles_classes_equivalence.values())
						if	i>1:
							print("i est",i)
							break
						
					
					for classe in dictionnaire_nouvelles_classes_equivalence.values():
						if classe:
							nouvelles_classes_equivalence.append(classe)

					print(pie, "SEP", classe_equivalence, "PIE ET CLASSE EQUIVALENCE")
					ce_qui_etait_la_quon_a_pas_scinde  = [x for x in pie if x != classe_equivalence]
					print(ce_qui_etait_la_quon_a_pas_scinde)
					nouvelles_classes_equivalence.extend(ce_qui_etait_la_quon_a_pas_scinde)
					
					print(f"les nouvelles classes d'equivalences que je forme apres parcours de la classe {classe_equivalence} sont {nouvelles_classes_equivalence}")
					if nouvelles_classes_equivalence != pie:
						pie = nouvelles_classes_equivalence
						nouvelles_classes_equivalence = []
						break
					else:
						dictionnaire_nouvelles_classes_equivalence = {tuple(element for sous_liste in classe for element in sous_liste): [] for classe in pie}
						break

		print(f"les classes d'equivalences finales sont : {nouvelles_classes_equivalence}")
			                
		# Construction de l'automate minimisé
		automate_minimise = Automate()

		# Ajout de l'alphabet
		for symbole in self.alphabet:
			automate_minimise.ajouter_symbole(symbole)

		# Parcours des nouvelles classes d'équivalence
		for classe in pie:
			nouvel_etat = automate_minimise.ajout_etat(["=".join(["=".join(etat) for etat in classe])])

			# Si la classe contient un état initial, on le définit comme état initial dans l'automate minimisé
			if any(etat in self.etats_initiaux for etat in classe):
				automate_minimise.etats_initiaux = [nouvel_etat]

			# Si la classe contient un état final, on le définit comme état final dans l'automate minimisé
			if any(etat in self.etats_finaux for etat in classe):
				automate_minimise.etats_finaux.append(nouvel_etat)

			# Parcours de l'alphabet pour la construction des transitions
			for symbole in self.alphabet:
				etat_arrive = self.f_transitions(classe[0], symbole)  # On prend le premier état de la classe dequivalence
				if etat_arrive:
					nouvelle_classe = self.trouver_classe(dictionnaire_nouvelles_classes_equivalence, etat_arrive[0])
					nouvel_etat_arrive = automate_minimise.ajout_etat(["=".join([etat for etat in nouvelle_classe])])
					automate_minimise.ajout_transition(nouvel_etat, symbole, nouvel_etat_arrive)

		# Copie des attributs non modifiés de l'automate original dans l'automate minimisé
		automate_minimise.transitions = self.transitions

		# Affectation de l'automate minimisé à l'automate actuel
		self.alphabet = automate_minimise.alphabet
		self.etats = automate_minimise.etats
		self.etats_initiaux = automate_minimise.etats_initiaux
		self.etats_finaux = automate_minimise.etats_finaux
		self.transitions = automate_minimise.transitions


	# fonction permettant de creer un automate
	def create(self, alphabet: list, etats: list, etats_initiaux: list, etats_finaux: list, transitions: dict):
		"""
        creation d'un automate (definition du quintuplet)
        @param alphabet : l'alphabet de l'automate
        @param etats : liste des etats de l'automate (il s'agit s'une liste de liste)
        @param etats_initiaux : liste des etats initiaux de l'automate (il s'agit d'une liste d'une liste)
        @param etats_finaux : liste des etats finaux de l'automate (il s'agit d'une liste d'une liste)

        """

		self.alphabet = alphabet
		self.etats = etats
		self.etats_initiaux = etats_initiaux
		self.etats_finaux = etats_finaux
		self.transitions = transitions


	def ajout_transition(self, etat_depart: list, symbole: str, etat_arrive: list) -> bool:
       
	    
		if not self.valider_symbole(symbole):
			print('le symbole ' + symbole + ' ne fait pas partie de l\'alphabet.')
			return False

		if not self.valider_etat(etat_depart):
			print('l\'etat de depart ' + etat_depart[0] + ' ne fait pas partie des etats.')
			return False

		if not self.valider_etat(etat_arrive):
			print('l\'etat d\'arrive ' + etat_arrive[0] + ' ne fait pas partie des etats.')
			return False

        # donc j'ajoute la trasition si : oit le couple etat initaial, symbole n'existe pas encore soit ca existe mais etat arrive n'est pas celui que je veux ajouter
		if (tuple(etat_depart), symbole) not in self.transitions or ((tuple(etat_depart), symbole) in self.transitions and etat_arrive not in self.f_transitions(etat_depart, symbole)):

			if (tuple(etat_depart), symbole) in self.transitions:
				self.transitions[tuple(etat_depart),symbole].append(etat_arrive)
			else:
                # print("l'état d'arrivé est", etat_arrive)
				self.transitions[(tuple(etat_depart), symbole)] = [etat_arrive]

			return True

		elif (tuple(etat_depart), symbole) in self.transitions and etat_arrive in self.f_transitions(etat_depart, symbole):
			print("transition deja presente dans l'automate")
			return False


    # fonction qui retourne toutes les natures d'un automate
	def nature(self) -> str:

		nature = []
			
		if self.est_epsilone_non_deterministe():
			nature.append("ε-AFN")

		if self.est_non_deterministe():
			nature.append("AFN")

		if self.est_deterministe():
			nature.append("AFD")

		if self.est_complet():
			nature.append("Complet")

		if len(nature) == 0:
			nature = ['non correctement defini.']

		return "Cet automate est : " + ", ".join(nature)

	
	def verifier_etats(self):
		pass


	# Afficher de facon commode un automate
	def __str__(self):

		"""
		Affichage de facon propre l'objet automate
		"""
		#intermediaires = set([etat[0] for etat in self.etats]) - set([etat[0] for etat in self.etats_initiaux]) - set([etat[0] for etat in self.etats_finaux])
		#print(intermediaires)
		ret =  self.nature() + "\n"
		ret += "   - alphabet   : {" + ", ".join(self.alphabet) + "} \n"
		ret += "   - initiaux      : " + ", ".join(["(%s)" % ",".join(init) for init in self.etats_initiaux]) + "\n"
		#ret += "   - etats intermediaires : " + ", ".join([",".join(init) for init in intermediaires]) + "\n" 
		ret += "   - finaux    : " + ", ".join(["(%s)" %",".join(init) for init in self.etats_finaux]) + "\n"
		ret += "   - nombre d'etats : %d \n" % (len(self.etats))
		ret += "   - transitions :\n"
		for etat in self.etats:
			ret += "       Partant de l'état (%s): \n" % (",".join(etat))
			for symbole in self.alphabet:
				
				if not len(self.f_transitions(etat,symbole)) == 0:
					for dest in self.f_transitions(etat,symbole):
						ret +=  "          en lisant le symbole (%s) on arrive à l'état (%s)\n" % (symbole, ",".join(dest))
						
		return ret
    

	# surcharge de l'opération d'addition
	def __add__(self, b):

		"""
		les noms des etats doivent etre differents
		"""

		if self.alphabet != b.alphabet:
			print("les deux automates doivent avoir le meme alphabet")
			exit()
		
		else:
			tous_les_etats_de_union = []
			toutes_les_transitions_union = {}

			len_etat_1 = len(self.etats_initiaux)
			etat_initial_union = []
			for etat in self.etats_initiaux:
				for num_etat in etat:
					etat_initial_union.append(num_etat)

			for etat in b.etats_initiaux:
				for num_etat in etat:
					etat_initial_union.append(num_etat)
            
			tous_les_etats_de_union.append(etat_initial_union)
			etat_initial_union = [etat_initial_union]

			for etat in tous_les_etats_de_union:
				
				for character in self.alphabet:
					
					len_etat_1 = 0
					nouvel_etat_pour_charactere = []

					for numero_etat in etat:
						
						
						liste_des_etats = self.f_transitions([numero_etat], character)
						if len(liste_des_etats) == 0:
							liste_des_etats = b.f_transitions([numero_etat], character)

						for e in liste_des_etats:
							for num_etat in e:
								if num_etat not in nouvel_etat_pour_charactere:
									nouvel_etat_pour_charactere.append(num_etat)


					if nouvel_etat_pour_charactere not in tous_les_etats_de_union:
						if len(nouvel_etat_pour_charactere) != 0:
							tous_les_etats_de_union.append(nouvel_etat_pour_charactere)	

					if len(nouvel_etat_pour_charactere) != 0:
						toutes_les_transitions_union[(tuple(etat), character)] = [
							nouvel_etat_pour_charactere]

			etats_finaux_de_union = []
			for etat in tous_les_etats_de_union:
				for etat_final in self.etats_finaux: 
					for num_etat in etat_final:
						if num_etat in etat:
							if etat not in etats_finaux_de_union:
								etats_finaux_de_union.append(etat)

				for etat_final in b.etats_finaux: 
					for num_etat in etat_final:
						if num_etat in etat:
							if etat not in etats_finaux_de_union:
								etats_finaux_de_union.append(etat)

			etats_finaux_de_union = etats_finaux_de_union
			res = Automate()
			res.create(self.alphabet, tous_les_etats_de_union, etat_initial_union, etats_finaux_de_union, toutes_les_transitions_union)
			print(res)
		return res


### TESTS

"""
a = Automate()

a.ajouter_symbole(symbole = "a")

a.ajouter_symbole(symbole = "b")

a.ajout_etat(etat = ['0'] , initial =True , final =True)

a.ajout_etat(etat = ['1'] , )

a.ajout_transition( ['0'] , "a" , ['1'])
a.ajout_transition( ['0'] , "b" , ['0'])
a.ajout_transition( ['1'] , "b" , ['1'])
a.ajout_transition( ['1'] , "a" , ['0'])


b = Automate()

b.ajouter_symbole(symbole = "a")

b.ajouter_symbole(symbole = "b")

b.ajout_etat(etat = ['2'] , initial =True , final =True)

b.ajout_etat(etat = ['3'] , )

b.ajout_transition( ['2'] , "a" , ['2'])
b.ajout_transition( ['2'] , "b" , ['3'])
b.ajout_transition( ['3'] , "a" , ['3'])
b.ajout_transition( ['3'] , "b" , ['2'])



a = Automate()

a.ajouter_symbole(symbole = "a")

a.ajouter_symbole(symbole = "b")

a.ajout_etat(etat = ['0'] , initial =True , final =True)

a.ajout_etat(etat = ['1'] , )

a.ajout_etat(etat = ['2'])

a.ajout_transition( ['0'] , "b" , ['1'])
a.ajout_transition( ['0'] , "a" , ['2'])
a.ajout_transition( ['1'] , "b" , ['0'])
a.ajout_transition( ['2'] , "a" , ['1'])


b = Automate()

b.ajouter_symbole(symbole = "a")

b.ajouter_symbole(symbole = "b")

b.ajout_etat(etat = ['3'] , initial =True , final =True)

b.ajout_etat(etat = ['4'] , )

b.ajout_transition( ['3'] , "a" , ['4'])
b.ajout_transition( ['4'] , "b" , ['3'])
"""

a = Automate()

a.ajouter_symbole(symbole = "a")

a.ajouter_symbole(symbole = "b")

a.ajout_etat(etat = ['0'], initial =True)
a.ajout_etat(etat = ['1'])
a.ajout_etat(etat = ['2'])
a.ajout_etat(etat = ['3'])
a.ajout_etat(etat = ['4'])
a.ajout_etat(etat = ['5'], final =True)

a.ajout_transition( ['0'] , "b" , ['3'])
a.ajout_transition( ['0'] , "a" , ['1'])
a.ajout_transition( ['1'] , "a" , ['1'])
a.ajout_transition( ['1'] , "b" , ['2'])
a.ajout_transition( ['2'] , "a" , ['2'])
a.ajout_transition( ['2'] , "b" , ['5'])
a.ajout_transition( ['3'] , "a" , ['3'])
a.ajout_transition( ['3'] , "b" , ['4'])
a.ajout_transition( ['4'] , "a" , ['4'])
a.ajout_transition( ['4'] , "b" , ['5'])
a.ajout_transition( ['5'] , "a" , ['5'])
a.ajout_transition( ['5'] , "b" , ['5'])

#print(a)
#a.minimiser()

c = Automate()

c.ajouter_symbole(symbole = "a")

c.ajouter_symbole(symbole = "b")
c.ajouter_symbole(symbole = "c")

c.ajout_etat(etat = ['0'], initial =True)
c.ajout_etat(etat = ['1'])
c.ajout_etat(etat = ['2'])
c.ajout_etat(etat = ['3'])
c.ajout_etat(etat = ['4'], final = True)
c.ajout_etat(etat = ['5'], final =True)

c.ajout_transition( ['0'] , "b" , ['0'])
c.ajout_transition( ['0'] , "a" , ['2'])
c.ajout_transition( ['0'] , "c" , ['1'])
c.ajout_transition( ['1'] , "a" , ['3'])
c.ajout_transition( ['1'] , "c" , ['3'])
c.ajout_transition( ['1'] , "b" , ['1'])
c.ajout_transition( ['2'] , "a" , ['2'])
c.ajout_transition( ['2'] , "b" , ['4'])
c.ajout_transition( ['2'] , "c" , ['3'])
c.ajout_transition( ['3'] , "a" , ['3'])
c.ajout_transition( ['3'] , "c" , ['3'])
c.ajout_transition( ['3'] , "b" , ['5'])
c.ajout_transition( ['4'] , "a" , ['4'])
c.ajout_transition( ['4'] , "b" , ['4'])
c.ajout_transition( ['4'] , "c" , ['5'])
c.ajout_transition( ['5'] , "a" , ['5'])
c.ajout_transition( ['5'] , "b" , ['5'])
c.ajout_transition( ['5'] , "c" , ['5'])


print(a)
a.minimiser()