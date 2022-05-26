# 5/24/2022 rev.1 : copied from Demo video

# 5/25/2022 : 
# AI class (child class) :  will inherit all its member variables from Player class (parent) 



from player import Player
import random
from time import sleep

class AI(Player) : 

    def __init__(self, name) :
        super().__init__()
        self.score = 0
        self.name = name


    def choose_guesture(self) : 
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors" , "Lizard" , "Spock"]
        sleep(1)
        print(f"{self.name} has picked {gesture_list[int(self.chosen_gesture)]}")
