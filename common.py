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

def donner_possibles(combinaison, evaluation_comb):
    nbr_possibles = len(COLORS)**LENGTH
    possibles = set()
    
    while len(possibles) < nbr_possibles:
        element = ''.join(random.choices(couleurs, k=LENGTH))
        if evaluation(element) == evaluation_comb:
            possibles.add(element)
                
    return possibles
