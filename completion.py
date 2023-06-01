from base import Automate



# 3. completion d'un automate
def completion(A:Automate) -> Automate:

	if A.est_complet():
		return A
	
	else:
		A_prime = Automate()
		A_prime = A
		A_prime.etats.append(['puit'])
		for etat in A_prime.etats:
			for char in A_prime.alphabet:
				if (tuple(etat),char) not in A_prime.transitions.keys():
					A_prime.transitions[(tuple(etat),char)]=[['puit']]

		for char in A_prime.alphabet:
			A_prime.transitions[(tuple(['puit']),char)]=[['puit']]
		return A_prime