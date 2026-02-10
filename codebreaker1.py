#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import common


def init():
    global tentatives
    tentatives = set()
    return


def codebreaker(evaluation_p):
    global tentatives
    # Combinaison au hasard
    combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    
    # Sortir une combinaison aléatoire jamais essayée auparavant
    while combinaison in tentatives:
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    # Ajouter la combinaison aux tentatives déjà esssayées
    tentatives.add(combinaison)
    
    return combinaison
