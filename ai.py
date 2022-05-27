# 5/24/2022 rev.1 : copied from Demo video

# 5/25/2022 : 
# AI class (child class) :  will inherit all its member variables from Player class (parent) 


# This child class is upposed to 
#  1- get the name from game class
#  2- keep track of game results 
#  3- ask for human's choice
#  4- print the choice

# from game import Game
from player import Player
import random
from time import sleep

class AI(Player) : 

    def __init__(self, name) :
        super().__init__(name)
        
        # not sure about these yet 
        self.wins = 0
        #self.losses = 0
        #self.ties = 0
        # self.score = 0
        

# this doesn't return any thing 
    def choose_guesture(self) : 
        self.selected_starter = random.choice(self.gesture_list)
        
        sleep(1)
        print("Computer made a choice!")
        print(f"{self.name} has picked {self.selected_starter}")
        pass
