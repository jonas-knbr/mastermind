#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import common

def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))

def codemaker(combinaison):
    global solution
    return common.evaluation(solution, combinaison)