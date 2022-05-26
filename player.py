


from typing_extensions import Self
from time import sleep
from game import Game



        


class Player(): 
    def __init__(self,name) :
        
        self.name = " "      # passing from game.py
        self.win = 0
        self.gesture_list = ["Rock","Paper","Scissors", "Lizard", "Spock"]
        self_chosen_guesture = ""
        self_rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
        

        global rpsls_table
        rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
