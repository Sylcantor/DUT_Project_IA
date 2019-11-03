# affichage
import matplotlib.pyplot as plt

class QDiagram:
    
    def __init__(self, cumul_reward_list):
        self.cumul_reward_list = cumul_reward_list
        self.generate_affi()
    
    def generate_affi(self):
        plt.plot(self.cumul_reward_list[:100])
        plt.ylabel('Cumulative reward')
        plt.xlabel('Étape')
        plt.show()