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
        self.human = (input("Enter your name: "))
        self.ai    = (input("Semiramis"))
        
        self.run_game()#???????????????????????????????????????????
        
        self.ending() #????????????????????????????????????????????
        pass 
    
    def run_game(self) :
        self.display_greeting()        # done
        self.display_rpsls_rule()      # done
        self.players_choose_starters()
        

        # asked & displayed human's gesture choice in Human class 
        # display human's input gesture
        player_move = 

        # asked & displayed Ai's gesture choice in Ai class 
      
         comp_move = 
       
        
      
        # determining the winer and the loser
        #  Win-lose matrix : more details in my project handwritten note
        rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
        # player_move = [number] , comp_move = [number]
        winner = rps_table[player_move][comp_move]
        print()
        if winner == player_move:
            print(name, "WINS!!!")
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
        else:
            print("TIE GAME")       
        print()
        time.sleep(2)
        clear()

        


        # display the winner name 
        # store the winner count .print score
        # play again 

        
        


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
**
** Number of players = 2 ( Human & Computer) 
**
** Human & Computer geture map: 
* Rock     = 0
* Paper    = 1
* Scissors = 2
* Lizard   = 3
* Spock    = 4
**
** Human chooses a gesture
** Computer Randomly chooses a geture
**
** Winner & Loser determination : 
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


def players_choose_starters(self) :
    self.human.choose_starter()
    self.ai.choose_starter()

    


    player_guesture_chioce = Human.choose_guesture.self.gesture_choice

    






def print_score(self):

