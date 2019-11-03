# q learning with table https://cdancette.fr/2017/08/18/reinforcement-learning-part1/
import numpy as np

import Game
from Game import Game

import QDiagram
from QDiagram import QDiagram

# On définit le nombre d’états (16), et d’actions pour chaque état (4)
states_n = 16
actions_n = 4
Q = np.zeros([states_n, actions_n])

# Set learning parameters
lr = .85  # learning rate, c’est la vitesse d’apprentissage
y = .99  # détermine l’importance des récompenses futures
num_episodes = 1000  # nombre de parties que l’on va faire
cumul_reward_list = []
actions_list = []
states_list = []

# 0.1 chance to go left or right instead of asked direction
game = Game(4, 4, 0.1)

for i in range(num_episodes):  # for jusqu'à la fin du nombre de parties que l’on va faire
    
    print("____nouvelle partie____") 
    
    actions = []
    s = game.reset()
    states = [s]
    cumul_reward = 0
    d = False
    while True:
        
        # on choisit une action aléatoire avec une certaine probabilité, 
        # qui décroit avec i : 1. / (i +1)
        Q2 = Q[s, :] + np.random.randn(1, actions_n)*(1. / (i + 1))
        a = np.argmax(Q2)
        
        s1, reward, d, _ = game.move(a)
        
        # Fonction de mise à jour de la Q-table
        Q[s, a] = Q[s, a] + lr*(reward + y * np.max(Q[s1, :]) - Q[s, a])
        cumul_reward += reward
        s = s1
        actions.append(a)
        states.append(s)
        
        if d == True:
            break
        
        game.print()  # affichage du jeu en temps réel
      
    print("Affichage fin:")    
    game.print()  # affichage du jeu à la fin d'une partie
        
    states_list.append(states)
    actions_list.append(actions)
    cumul_reward_list.append(cumul_reward)

    print("Score over time: " + str(sum(cumul_reward_list[-100:])/100.0))

game.reset()

diag = QDiagram(cumul_reward_list)
