#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Autorisons le codemaker à changer sa combinaison cible quand il le souhaite, à condition de
# respecter les évaluations déjà données. L’objectif du codemaker est de faire durer la partie le
# plus longtemps possible.

import random
import common

def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))

def codemaker(combinaison):
    global solution
    return common.evaluation(solution, combinaison)