# affichage
import matplotlib.pyplot as plt


class QDiagram:
    """
    A class used for the representing the outcome of QLearning
    """

    def __init__(self, cumul_reward_list):
        """
        Parameters
        ----------
        cumul_reward_list : a list
            for the rewards    
        """
        self.cumul_reward_list = cumul_reward_list
        self.generate_affi()

    def generate_affi(self):
        """
        For generating the diagram   
        """
        plt.plot(self.cumul_reward_list[:100])
        plt.ylabel('Cumulative reward')
        plt.xlabel('Étape')
        plt.show()
