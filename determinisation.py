from base import Automate


# 1. determinisation d'un automate
def determinisation(A: Automate) -> Automate:

    if A.est_deterministe():
        return A

    else:

        tous_les_etats_du_determinise = []
        toutes_les_transitions_du_determinise = {}

        etat_initial_du_determinise = []
        for etat in A.etats_initiaux:
            for num_etat in etat:
                etat_initial_du_determinise.append(num_etat)

        tous_les_etats_du_determinise.append(etat_initial_du_determinise)
        etat_initial_du_determinise = [etat_initial_du_determinise]

        for etat in tous_les_etats_du_determinise:

            for character in A.alphabet:
                nouvel_etat_pour_charactere = []

                for numero_etat in etat:

                    liste_des_etats = A.f_transitions([numero_etat], character)

                    for e in liste_des_etats:
                        for num_etat in e:
                            if num_etat not in nouvel_etat_pour_charactere:
                                nouvel_etat_pour_charactere.append(num_etat)
                if nouvel_etat_pour_charactere not in tous_les_etats_du_determinise:
                    if len(nouvel_etat_pour_charactere) != 0:
                        tous_les_etats_du_determinise.append(
                            nouvel_etat_pour_charactere)

                if len(nouvel_etat_pour_charactere) != 0:
                    toutes_les_transitions_du_determinise[(tuple(etat), character)] = [
                        nouvel_etat_pour_charactere]

        etats_finaux_du_determinise = []
        for etat in tous_les_etats_du_determinise:
            for etat_final in A.etats_finaux:  # ici aussi
                for num_etat in etat_final:
                    if num_etat in etat:
                        if etat not in etats_finaux_du_determinise:
                            etats_finaux_du_determinise.append(etat)
        etats_finaux_du_determinise = etats_finaux_du_determinise

        A_prime = Automate()
        A_prime.create(alphabet=A.alphabet, etats=tous_les_etats_du_determinise, etats_initiaux=etat_initial_du_determinise,
                       etats_finaux=etats_finaux_du_determinise, transitions=toutes_les_transitions_du_determinise)

        return A_prime
