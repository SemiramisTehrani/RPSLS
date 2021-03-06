# Week5 project : RPSLS (Rock, Paper, Scissors, Lizard, Spock)

# 5/25/2022 rev.1 : James's help 
# human class (child class) : will inherit all its member variables from Player class (parent) 
# 5/27/2022 rev.2 , session 1o1 : clean up the class , removed extras , fixed for loop 
# 5/27/2022 rev.3 : final code 
# 5/27/2022 rev.4 : Dan's feedback video --> adding warning if user accidently enters alphabets/string to choose gesture --> can't get it worked so far 5/29/2022


# This child class is upposed to 
#  1- get the name from game class
#  2- keep track of game results 
#  3- ask for human's choice
#  4- print the choice



from player import Player
from time import sleep 

class Human(Player) :

    def __init__(self, name) :
        super().__init__(name)
        self.wins = 0               # 5/27/2022 (101 session)simple way to track the win , get rid of loss , ties, and score
        pass

    
    # Similar to Ai method
    def choose_gesture(self) : 

        for gesture in self.gesture_list : 
            print(f"Press {self.gesture_list.index(gesture)} for {gesture}")
 
        user_input = int(input("Choose a gesture between 0 and 4! "))
        
        while not (user_input <= len(self.gesture_list) - 1) :
                print(f"Invalid selection")
                user_input = int(input("Choose a gesture between 0 and 4! "))
                
        #if user_input.isstring() :
        #   print(f"Invalid selection")
        #  user_input = int(input("Choose a gesture between 0 and 4! "))

        self.selected_starter = self.gesture_list[user_input]

        sleep(1)
        print(f"{self.name} has picked {self.selected_starter}")
        pass
        

