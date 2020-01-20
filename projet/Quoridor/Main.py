# -*- coding: utf-8 -*-

from Plateau import *

"""
Crée un plateau de jeu.
"""


p = Plateau()
p.initTabMurs()

count = 0

print(p.copy_game_state())

while(p.finDeJeu == False):
    if(count % 2 == 0):
        p.affichejeu()
        p.tour(p.j1)
    else:
        p.tour(p.j2)
    
    count += 1

