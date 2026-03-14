#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Autorisons le codemaker à changer sa combinaison cible quand il le souhaite, à condition de
# respecter les évaluations déjà données. L’objectif du codemaker est de faire durer la partie le
# plus longtemps possible.

import random
import common

def init():
    global solution, possibles, resultats
    
    # Solution aléatoire
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    # Ensemble contenant toutes les combinaisons possibles respectant 
    # toutes les évaluations passées ; pour l'instant toutes les solutions
    # puisqu'aucune évaluation n'a encore été réalisée
    possibles = common.donner_possibles(None, None)
    resultats = []
    return

def codemaker(combinaison):
    global solution, possibles, resultats
    
    groupes_evaluations = { (i,j) : [0, []] for i in range(common.LENGTH + 1) for j in range(common.LENGTH + 1)}
    candidats = possibles.copy()
    # Sélection et scorage des candidats valides
    for candidat in candidats:
        valide = True
        for resultat in resultats:
            # Si le candidat ne respecte pas une évaluation passée,
            # on le saute
            if common.evaluation(candidat, resultat[0]) != resultat[1]:
                valide = False
                break
        
        if not valide:
            break
        # Le candidat est valide, on va maintenant le classifier
        # selon son évalution
        evaluation_candidat = common.evaluation(candidat, combinaison)
        groupes_evaluations[evaluation_candidat][0] += 1
        groupes_evaluations[evaluation_candidat][1].append(candidat)
        
    # Attribution de la nouvelle solution au meilleur candidat, i.e un au
    # hasard parmi le groupe d'évaluation le plus fréquent
    solution = random.choice(max(groupes_evaluations.values(), key=lambda x : x[0])[1])
    
    # Évaluation de la combinaison actuelle proposée
    evaluation_actuelle = common.evaluation(solution, combinaison)
    resultats.append((combinaison, evaluation_actuelle))
    # Mise à jour des possibles
    common.maj_possibles(possibles, combinaison, evaluation_actuelle)
    return evaluation_actuelle