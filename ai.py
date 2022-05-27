# 5/24/2022 rev.1 : copied from Demo video

# 5/25/2022 : 
# AI class (child class) :  will inherit all its member variables from Player class (parent) 



from player import Player
import random
from time import sleep

class AI(Player) : 

    def __init__(self, name) :
        super().__init__(name)
        
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.score = 0
        


    def choose_guesture(self) : 
        # this is replaced by below
        # self.random_chosen_gesture = str(random.randint(0,4))
        self.selected_starter = random.choice(self.gesture_list)
        
        # this is moved to Player class
        # gesture_list = ["Rock", "Paper", "Scissors" , "Lizard" , "Spock"]
        
        sleep(1)
        print("Computer made a choice!")
        print(f"{self.name} has picked {int(self.selected_starter)}")
        pass
