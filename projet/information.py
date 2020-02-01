import matplotlib
import matplotlib.pyplot as plt


def manuel():
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
