# 5/24/2022  , rev.1 : 
# 5/25/2022 , rev.2 : adding comments
# Mapping game = [ 0 : Rock , 1 : Paper , 2 : Scissors ,  3 : Lizard , 4 : Spock ]
#  
# 
# Gmae class
# 1- inquery humna name
# 2 - run game 
#   2-1 : greeting
#   2-2 : game rules
#   2-3 : diplay chosen gestures
#   2-4 : determining & showing winner for the first round 
#   2-5 : determining & showing winner for the second round 
#   2-6 : determining & showing winner for the third round
# 3 - end game   
# 2-7 : determining & showing final result 


from player import Player
from human import Human
from ai import AI


class Game() : 
    def __init__(self):
        # self.player = ()
        self.player_one = Human(input("Enter your name: "))
        # self.human = (input("Enter your name: "))

        self.player_two = AI(("Semiramis"))
        # self.ai    = (("Semiramis"))
        
        self.run_game()     # pending ???????????????????????????????????????????
        
        self.ending()       #????????????????????????????????????????????
        pass 
    
    def run_game(self) :
        self.display_greeting()        # done
        self.display_rpsls_rules()      # done
        self.players_choose_gesture()  # ai is done , human is not
        

        # determining the winer and the loser
       
        #player_move =
        #comp_move = 
       
       #  Win-lose matrix : more details in my project handwritten note
        #global rpsls_table
        #rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
        # player_move = [number] , comp_move = [number]
        #winner = rps_table[player_move][comp_move]
        
        #print()
        #if winner == player_move:
        #    print(name, "WINS!!!")
        #elif winner == comp_move:
        #    print("COMPUTER WINS!!!")
        #else:
        #    print("TIE GAME")       
        #print()
        #time.sleep(2)
        #clear()

        


        # display the winner name 
        # store the winner count .print score
        # play again 

        
        


    def display_greeting(self):
        print()
        print("*** Welcome to Rock Paper Scissors Lizard Spock by Semi ***")
        print()



    def display_rpsls_rules(self):
        print()
        print( 
            """"
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
    """ 
        )



    def players_choose_gesture(self) :
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        pass

    

