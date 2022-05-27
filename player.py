# Week5 project : RPSLS (Rock, Paper, Scissors, Lizard, Spock)

# 5/25/2022 rev.1 : James's help 
# Player class (parent class) : Player stores similarities of Ai and Humnan classes
# 5/26/2022 rev.2 (office hour) :   


from typing_extensions import Self
from time import sleep
from game import Game



        


class Player(): 
    def __init__(self,name) :
        
        self.name = name
        self.gesture_list = ["Rock","Paper","Scissors", "Lizard", "Spock"]
        self.selected_starter = ""
        
        
        pass 
    
    def choose_starter(self) :
        pass
        
        
