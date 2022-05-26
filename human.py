# Week5 project : RPSLS (Rock, Paper, Scissors, Lizard, Spock)

# 5/25/2022 rev.1 : James's help 
# human class (child class) : will inherit all its member variables from Player class (parent) 



from player import Player
from time import sleep 

class Human(Player) :

    def __init__(self, name) :
        super().__init__()
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.name = name

def choose_guesture(self) : 
        self.gesture_choice = int(input("Press 0 for Rock, 1 for Paper, 2 Scissor, 3 for Lizzard, 4 for Spock"))
        sleep(1)
        print(f"{self.name} has picked {int(self.gesture_choice)}")
