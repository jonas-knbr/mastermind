#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import play
import codemaker1
import codemaker2
import codebreaker2
import matplotlib.pyplot as plt

nbr_parties = 1000 #int(input("Combien de parties ?\n> "))
parties = [[], []]

for _ in range(nbr_parties):
    print(f"{_} parties jouées")
    parties[0].append(play.play(codemaker1, codebreaker2, quiet=True))
    parties[1].append(play.play(codemaker2, codebreaker2, quiet=True))

# Permet d'afficher deux graphiques en un
fig, ax = plt.subplots(1, 2)

for i in range(2):
    ax[i].set_title(f"codemaker{i+1}\n({nbr_parties} parties)")
    ax[i].set_xlabel("Nombre d'essais")
    ax[i].set_ylabel("Nombre d'occurrences")
    ax[i].hist(parties[i])
    
plt.savefig(f"q8_histogramme_{nbr_parties}_parties.png")
plt.savefig(f"q8_histogramme.png")
plt.show()