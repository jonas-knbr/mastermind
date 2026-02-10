#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import play
import codemaker1
import codebreaker2
import matplotlib.pyplot as plt

nbr_parties = 1000 #int(input("Combien de parties ?\n> "))
parties = []

for _ in range(nbr_parties):
    parties.append(play.play(codemaker1, codebreaker2, quiet=True))

plt.title(f"Histogramme du nombre d'essais réalisés par le codebreaker2\n({nbr_parties} parties)")
plt.xlabel("Nombre d'essais")
plt.ylabel("Nombre d'occurrences")
plt.hist(parties)
plt.savefig(f"q7_histogramme_{nbr_parties}_parties.png")
plt.savefig(f"q7_histogramme.png")
plt.show()