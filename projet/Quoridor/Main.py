# -*- coding: utf-8 -*-

from Plateau import *


class Main():
    """
    Crée un plateau de jeu.
    """


    p = Plateau()
    p.initTabMurs()

    p.init_matrice()

    count = 0

    while(p.finDeJeu == False):
        if(count % 2 == 0):
            p.affichejeu()
            p.tour(p.j1)
        else:
            p.tour(p.j2)
        
        count += 1
