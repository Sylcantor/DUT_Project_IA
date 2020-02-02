import numpy as np
import matplotlib
import matplotlib.pyplot as plt

"""
fonctions matplotlib
"""


def manuel():
    """
    manuel utilisateur
    """
    fig = plt.figure()
    fig.suptitle('Démarrage', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)

    ax.text(1, 8, 'Manuel apprentissage: ', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    ax.text(1, 1,
            "1.  importer un jeu (game) suivant la structure du jeu de nim\nou le tic tac toe\n\n" +
            "Avec sauvegarde (plus long):\n" +
            "    2.  lancer au terminal: python main.py - a q - t 10000 - s\n" +
            "    pour sauvegarder sous forme de fichier la matrice\n" +
            "    3.  lancer au terminal: python main.py - a q - l\n" +
            "    pour lancer le jeux depuis le fichier précédement créé\n\n" +
            "Sans sauvegarde (pour faire un rapide test):\n" +
            "    2.  lancer au terminal: python main.py - a q - t 10000\n",
            bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})

    ax.axis([0, 10, 0, 10])

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


def plot_multiple_agents_reward(*gls):
    """ Function to plot agent's accumulated reward vs. iteration """

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
              '#bcbd22', '#17becf']
    j = 0
    for i in gls:
        plt.plot(np.cumsum(i.agent.rewards), color=colors[j])
        j += 1
        if j is len(gls):
            j = 0
    plt.title('Two Agents Cumulative Reward vs. Iteration')
    plt.ylabel('Reward')
    plt.xlabel('Episode')
    plt.show()
