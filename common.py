#!/usr/bin/env python3

import sys
import random

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

def evaluation(combinaison, solution):
    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
        
    nbr_bp = nbr_mp = 0 # Définit les entiers contenant le nombre de plots bien placés et mal placés
    ensemble_solution = set(solution) # Ensemble contenant les éléments présents dans la solution
    
    # Boucle d'évaluation itérant à travers les éléments de la combinaison et de la solution
    for c_comb, c_sol in zip(combinaison, solution):
        if c_comb == c_sol:
            nbr_bp += 1
        elif c_comb in ensemble_solution:
            nbr_mp += 1
            ensemble_solution.remove(c_comb) # évite de compter trop de fois des plots mal placés
    
    return (nbr_bp, nbr_mp)


def donner_possibles (combinaison,evaluation):
    """
    tu vas voir la gueule des if, en plus il faut encore prendre en compte les plots bien placés, pour le moment c'est censé juste enlever des combinaisons en se basant sur le nombre de bonnes couleurs
    """
    possibles = set(''.join(random.choices(COLORS, k=LENGTH))) # ensemble avec toutes les combinaisons possibles que l'on affine au fur et à mesure
    if evaluation[0] == 0: # si aucune bonne couleur 
        possibles.remove (''.join(random.choices(COLORS in combinaison,k=LENGTH))) #enlève toutes les combinaisons qui contiennent au moins une des quatres couelurs de la combianison testée
    elif evaluation[0] == 1 :
        possibles.remove(''.join(random.choices(COLORS in combinaison, k=LENGTH))) #enlève les combinaisons possibles qui contiennent pas de couleurs en commun avec la combinaison
    elif evaluation[0] == 2:
        possibles.remove(random.choices(''.join(random.choices(COLORS in combinaison, k = evaluation[0]-1)).join(''.join(random.choices(COLORS not in combinaison, k=LENGTH+1-evaluation[0]))))) #enlève les combinaisons qui utilisent seulement 1 couleur parmi les couleurs de la combinaisons testée
    elif evaluation[0] == 3 :
        possibles.remove(random.choices((''.join(random.choices(COLORS in combinaison, k=evaluation[0]-1)).join(''.join(random.choices(COLORS not in combinaison, k=LENGTH+1-evaluation[0])))))) #enlève les combinaisons qui utilisent seulement deux couleurs parmi les quatres de la combinaison testée (je suis vraiment pas sûr que ça fonctionne)
    elif evaluation[0] == 4:
        possibles.remove(''.join(random.choices(COLORS not in combinaison, k=LENGTH))) # élimine les combinaisons qui n'utilisent pas les couleurs de combinaison
    