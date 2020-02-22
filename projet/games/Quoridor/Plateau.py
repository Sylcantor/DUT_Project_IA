# coding=utf-8

from games.game import Game
from games.Quoridor.Joueur import *
from math import *

from games.Quoridor.Joueur import Joueur


class Plateau(Game):
    """Classe Plateau

    Le plateau de jeu est représenté par une liste de listes
    (càd un tableau à deux dimensions) de taille 19 * 17.
    """

    # Tableau représentant l'état des cases du plateau
    tabDeJeu = []

    def __init__(self):
        """Constructeur de la classe Plateau

        Un plateau possède :
            - un nombre de ligne,
            - un nombre de colonnes,
            - des phases,
            - deux joueurs.
        """

        # Détermine la taille du plateau
        self.ligne = 19
        self.colonne = 17

        # Ajout des phases de jeu
        self.phases = []
        self.phases.append("Déplacez vous")
        self.phases.append("Indiquez numéro position du mur à poser")
        self.currentphase = self.phases[0]

        # Compteur de phases
        self.numerophase = 1

        # Ajout des informations concernant les joueurs
        self.players = ['Joueur 1', 'Joueur 2']
        self.currentplayer = None

        self.j1 = Joueur(self.players[0], 'A', self.ligne-1, 1, 1, 8)
        self.j2 = Joueur(self.players[1], 'B', 0, 1, self.ligne-2, 8)

        self.players_info = []
        self.players_info.append(self.j1)
        self.players_info.append(self.j2)

        # Initialisation du plateau
        self.initTabDeJeu()

    def initTabDeJeu(self):
        """Méthode initTabDeJeu

        Remplit le tableau :
            - de 5 pour la ligne d'arrivée du joueur B
            - de 7 pour la ligne d'arrivée du joueur A
            - de 0 pour les cases libres dédiées aux joueurs
            - de m pour les cases libres dédiées aux murs
        """

        for i in range(self.ligne):
            self.tabDeJeu.append([])

            if(i == 0):
                for j in range(self.colonne):
                    self.tabDeJeu[i].append(5)

            elif(i == self.ligne-1):
                for j in range(self.colonne):
                    self.tabDeJeu[i].append(7)

            elif(i % 2 == 0):
                for j in range(self.colonne):
                    self.tabDeJeu[i].append('m')

            else:
                for j in range(self.colonne):
                    if(j % 2 == 0):
                        self.tabDeJeu[i].append(0)
                    else:
                        self.tabDeJeu[i].append('m')

        # Ajout des joueurs sur le plateau de jeu
        self.tabDeJeu[self.j1.posY][self.j1.posX] = self.j1.pion
        self.tabDeJeu[self.j2.posY][self.j2.posX] = self.j2.pion

    def print_game(self):
        """Méthode print_game

        Affiche le plateau de jeu avec les coordonnées de chacune des cases.
        """

        # Numérotation des colonnes
        string = "\n"
        string += '       '

        for j in range(self.colonne):
            string += str(j)
            string += '   '

        string += "\n       ------------------------------------------------------------------------"
        string += '\n\n'

        # Numérotation des lignes et affichage du tableau de jeu
        for i in range(self.ligne):
            for j in range(self.colonne):

                # Numérotation des lignes comprenant un seul chiffre
                if(i < 10):
                    if(j == 0):
                        string += str(i)
                        string += ' |   '

                # Numérotation des lignes comprenant deux chiffres
                elif(i > 9):
                    if(j == 0):
                        string += str(i)
                        string += ' |   '

                # Affichage des valeurs pour les colonnes comprenant un seul chiffre
                if(j < 10):
                    string += str(self.tabDeJeu[i][j])
                    string += '   '

                # Affichage des valeurs pour les colonnes comprenant deux chiffres
                elif(j > 9):
                    string += str(self.tabDeJeu[i][j])
                    string += '    '

            # Si c'est la dernière ligne
            if(i == self.ligne-1):
                string += "\n"

            # Sinon
            else:
                string += "\n"
        return string

    def winner(self):
        """Méthode victoire

        Détermine la fin du jeu et le joueur gagnant.
        """

        if(self.j1.posY == self.ligne-1 or self.blocage(self.j1)):
            gagnant = self.j1.name
        elif(self.j2.posY == 0 or self.blocage(self.j2)):
            gagnant = self.j1.name
        elif self.numerophase >= 40:
            gagnant = "Draw"
        else:
            gagnant = None

        return gagnant

    def numMurs(self):
        """Méthode numMurs

        Attribut un numéro à chacune des cases disponibles pour la pose d'un mur.
        """

        # Numérotation des cases
        num = 0

        # Tableau regroupant le résultat de l'attribution
        murs = []

        for i in range(1, self.ligne-2):
            for j in range(self.colonne-1):
                if(self.tabDeJeu[i][j] == 'm'):
                    num += 1
                    attribution = {'numéro': num, 'y': i, 'x': j}
                    murs.append(attribution)
                    # print(attribution)

            # print("\n")

        return murs

    def initMatrice(self):
        """Méthode initMatrice

        Initialise la matrice d'adjacence du plateau de jeu.
        Ces états correspondent aux cases '0' voisines.
        """

        # Initialisation des variables
        matrice = {}
        voisins = []
        key = 1
        decalage = 9

        # On attribut une liste (des voisins) vide à chaque état
        for i in range(0, 83):
            matrice[i] = voisins

        for i in range(1, self.ligne-1):
            for j in range(0, self.colonne):
                if(self.tabDeJeu[i][j] == 0 or self.tabDeJeu[i][j] == 'A' or self.tabDeJeu[i][j] == 'B'):

                    # S'il n'y a pas de mur en haut
                    if(self.tabDeJeu[i-1][j] == 'm'):
                        voisins.append(key-decalage)

                    # Si on n'est pas sur la dernière colonne
                    if(j != self.colonne-1):
                        # S'il n'y a pas de mur à droite
                        if(self.tabDeJeu[i][j+1] == 'm'):
                            voisins.append(key+1)

                    # S'il n'y a pas de mur en bas
                    if(self.tabDeJeu[i+1][j] == 'm'):
                        voisins.append(key+decalage)

                    # Si on n'est pas sur la première colonne
                    if(j != 0):
                        # S'il n'y a pas de mur à gauche
                        if(self.tabDeJeu[i][j-1] == 'm'):
                            voisins.append(key-1)

                    # Réinitialisation
                    matrice[key] = voisins
                    voisins = []
                    key += 1

        # Ajout des voisins pour la ligne d'arrivée de 'B'
        matrice[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Ajout des voisins pour la ligne d'arrivée de 'A'
        matrice[82] = [81, 80, 79, 78, 77, 76, 75, 74, 73]

        for j in range(1, 10):
            matrice[j].append(0)

        for k in range(73, 82):
            matrice[k].append(82)

        for key in matrice:
            print(key, ' : ', matrice[key], end='\n')

        return matrice

    def getNoeudJoueur(self, joueur):
        """Méthode getNoeudJoueur

        Détermine le numéro du noeud du joueur à partir de ses coordonnées.
        """

        return floor(joueur.posY/2)*9 + ceil((joueur.posX+1)/2)

    def cheminVersSortie(self, graphe, debut, fin, chemin):
        """Méthode cheminVersSortie

        Retourne un chemin de 'debut' vers 'fin' dans le 'graphe' s'il existe,
        Sinon retourne 'None'.
        """

        chemin.append(debut)

        if(debut == fin):
            return chemin

        if(debut not in graphe):
            return None

        for noeud in graphe[debut]:

            if(noeud not in chemin):
                newChemin = self.cheminVersSortie(graphe, noeud, fin, chemin)

                if(newChemin):
                    return newChemin

        return None

    def blocage(self, joueur):
        """Méthode blocage

        Vérifie si le 'joueur' est bloqué.
        """

        graphe = self.initMatrice()
        debut = self.getNoeudJoueur(joueur)
        chemin = []

        if(joueur is self.j1):
            fin = 82
        else:
            fin = 0

        if(self.cheminVersSortie(graphe, debut, fin, chemin) is not None):
            print(chemin)
            return False
        else:
            return True


######################### Méthodes utilisées par les agents #########################


    def play_move(self, choix, currentplayer):
        """Méthode play_move

        Permet de jouer :
            - déplacer son pion lors de la phase de déplacement,
            - poser un mur lors de la phase de pose de murs.
        """

        def phase_deplacement(choix, currentplayer_info):
            if(choix in self.valid_moves(currentplayer)):
                # Déplacement du pion du joueur courant
                currentplayer_info.seDeplacer(choix, self)
                # Ajoute la nouvelle position du joueur sur le plateau de jeu
                self.tabDeJeu[currentplayer_info.posY][currentplayer_info.posX] = currentplayer_info.pion

        def phase_pose_murs(choix, currentplayer_info):
            if(choix in self.valid_moves(currentplayer)):
                murs = self.numMurs()
                # Pose d'un mur par le joueur courant
                currentplayer_info.poserMur(murs, choix, self)

        # Mise à jour du nom du joueur courant
        self.currentplayer = currentplayer

        # Initialisation du joueur courant
        currentplayer_info = None

        # On récupère le joueur grâce à self.players_info
        for i in self.players_info:
            if(i.nom is self.currentplayer):
                currentplayer_info = i
                break

        if self.currentphase is self.phases[0]:
            phase_deplacement(choix, currentplayer_info)
        elif self.currentphase is self.phases[1]:
            phase_pose_murs(choix, currentplayer_info)

        # On fait passer le joueur à la phase suivante
        # Phase suivante dynamique selon self.currentphase dans self.phases
        if self.numerophase+1 < 41:
            currentplayer_info.numerophase += 1

        # On change de phase globale :
        # Si tous les joueurs sont à la phase suivante,
        # alors la phase globale du jeu passe à la phase d'après
        dummy_phase = self.players_info[0].numerophase

        for i, element in enumerate(self.players_info):
            if(element.numerophase is not dummy_phase):
                # Alors quelqu'un n'a pas encore terminé
                break
            # Dernier élément
            if i is len(self.players_info) - 1:
                if self.numerophase < 41:
                    if self.numerophase % 4 == 0:
                        self.currentphase = self.phases[1]
                    else:
                        self.currentphase = self.phases[0]
                    self.numerophase += 1

    def valid_moves(self, currentplayer, all_moves=False):
        """Méthode valid_moves

        Retourne la liste de tous les coups possibles.
        """

        def phase1():
            """Méthode phase_deplacement

            Retourne la liste des coups pour la phase de déplacement.
            """

            liste_coups = []
            direction = ["haut", "bas", "gauche", "droite"]

            def check_deplacement(choix):
                """Méthode check_deplacement

                Vérifie que le joueur puisse se déplacer sur son choix à partir de sa position actuelle.
                """

                if(choix in direction):
                    return (currentplayer_info.check_moves(choix, self))
                else:
                    return False

            for i in direction:
                if(check_deplacement(i)):
                    liste_coups.append(i)

            return liste_coups

        def phase2():
            """Méthode phase_pose_murs

            Retourne la liste des coups pour la phase de pose de murs.
            """

            liste_coups = []
            murs = self.numMurs()
            idMurs = []

            # On récupère l'id de chaque cellule sur laquelle on peut poser un mur
            for i in range(len(murs)):
                idMurs.append(murs[i]['numéro'])

            def check_pose_murs(choix):
                """Méthode check_pose_murs

                Vérifie que le joueur puisse poser un mur sur la case de son choix.
                """

                if(choix in idMurs):
                    return (currentplayer_info.check_laying_walls(murs, choix, self))
                else:
                    return False

            for i in idMurs:
                if(currentplayer_info.check_laying_walls(murs, i, self)):
                    liste_coups.append(i)

            return liste_coups

        # Initialisation du joueur courant
        currentplayer_info = None

        # On récupère le joueur grâce à self.players_info
        for i in self.players_info:
            if(i.nom is currentplayer):
                currentplayer_info = i
                break

        # On fait un switch case sur self.currentphase
        switch = {
            self.phases[0]: phase1(),
            self.phases[1]: phase2()
        }

        # Les coups pour la phase globale actuelle du jeu
        if all_moves is not True:
            moves = switch.get(self.currentphase)

        # Tous les coups possibles du jeu (sert à initialiser la matrice Q)
        else:
            # On applatit la liste
            moves = sum(switch.values(), [])

        return moves
