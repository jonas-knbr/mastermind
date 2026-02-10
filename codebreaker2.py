#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import common


def init():
    global derniere_tentative, possibles
    derniere_tentative = ""
    possibles = set()
    return


def codebreaker(evaluation_p):
    global derniere_tentative, possibles
    # Si aucune évaluation n'a été fournie (premier essai), on effectue juste un essai au hasard
    if evaluation_p == None:
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
        derniere_tentative = combinaison
        return combinaison
    
    # On est au deuxième essai, on doit creer l'ensemble des possibles
    elif len(possibles) == 0:
        possibles = common.donner_possibles(derniere_tentative, evaluation_p)
   
    # Cas général
    else:
        common.maj_possibles(possibles, derniere_tentative, evaluation_p)
    
    # On prend une solution au hasard parmi les possibles
    combinaison = random.choice(list(possibles))
    derniere_tentative = combinaison
    
    return combinaison
