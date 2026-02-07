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

def creer_tous_possibles(couleurs, taille=LENGTH):
    taille_ensemble = len(couleurs)**taille
    ensemble = set()
    while len(ensemble) < taille_ensemble:
        element = ''.join(random.choices(couleurs, k=taille))
        ensemble.add(element)
    return ensemble

def donner_possibles(combinaison, evaluation):
    nbr_possibles = len(COLORS)**LENGTH
    possibles = creer_tous_possibles(COLORS)
    nbr_bp, nbr_mp = evaluation
    
    # Si aucune couleur placée ne correspond à la solution
    if not nbr_bp and not nbr_mp:
        couleurs_dans_comb = [color for color in COLORS if color in combinaison]
        possibles -= creer_tous_possibles(couleurs_dans_comb)
    else:
        compte_couleurs = {color:combinaison.count(color) for color in COLORS}
        
        # Si l'on a placé une seule couleur
        if LENGTH in compte_couleurs.values():
            couleur_max = max(compte_couleurs, key=lambda x: compte_couleurs[x])
            
            # On supprime toutes les combinaisons qui n'ont pas nbr_mp+nbr_bp fois cette couleur
            for possible in possibles:
                if possible.count(couleur_max) < nbr_mp + nbr_mp:
                    possibles.remove(possible)
                
    return possibles
