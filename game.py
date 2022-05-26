# 5/24/2022  , rev.1 : 
# 5/25/2022 , rev.2 : adding comments
# Mapping game = [ 0 : Rock , 1 : Paper , 2 : Scissors ,  3 : Lizard , 4 : Spock ]
#  
# 
# 
#
# 


from ast import Try
from player import Player
from human import Human
from ai import AI


class Game() : 
    def __init__(self):
        self.player = ()
        self.human=()
        self.ai=()
        pass 
    
    def run_game(self) :
        self.display_greeting()        # done
        self.display_rpsls_rule()      # done
        
        
        self.game()
        self.ending()


# Game Rules

def display_greeting():
    print()
    print("*** Welcome to Rock Paper Scissors Lizard Spock by Semi ***")
    print()



def display_rpsls_rules():
    print()
    print
    ( """"
*****************************************************************        
*** Rules for Rock-Paper-Scissors-Lizard-Spock : ***
** Scissors cuts Paper
** Paper covers Rock
** Rock crushes Lizard
** Lizard poisons Spock
** Spock smashes Scissors
** Scissors decapitates Lizard
** Lizard eats Paper
** Paper disproves Spock
** Spock vaporizes Rock
** Rock crushes Scissors
*****************************************************************     
""" )
print()


def game() : 
    Player.self.name = input("Enter your name: ")
    player_guesture_chioce = Human.choose_guesture.self.gesture_choice
    








def game():

    while True:
        try:

            choice =  







# determining the winer and the loser
# Win-lose matrix : more details in my project handwritten note
rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]

