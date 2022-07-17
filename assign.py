import random
import time
from enum import IntEnum

class Convertor(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Game():
    def __init__(self,verbose):
        self.verbose = verbose
        if self.verbose == True:
            print("Let's play Rock, Paper and Scissors")
            print("=======================")

        self.player_wins = 0
        self.comp_wins   = 0
        self.draws       = 0

    def printStatus(self):
        if self.verbose == True:
            print("Games played: ", self.player_wins + self.comp_wins + self.draws)
            print("Player wins!!!: ", self.player_wins)
            print("Computer wins: ", self.comp_wins)
            print("Draws: ", self.draws)

    def eval(self, p_sel, c_sel):
        who_wins = -1
        if p_sel == c_sel:
            who_wins = 0
        elif p_sel == 1:
            if c_sel == 2:
                who_wins = 2
            else:
                who_wins = 1
        elif p_sel == 2:
            if c_sel == 3:
                who_wins = 2
            else:
                who_wins = 1
        elif p_sel == 3:
            if c_sel == 1:
                who_wins = 2
            else:
                who_wins = 1

        if who_wins == 0:
            if self.verbose == True:
                print("It is a draw!!!")
            self.draws += 1
        elif who_wins == 1:
            if self.verbose == True:
                print("Player wins!!!")
            self.player_wins += 1
        else:
            if self.verbose == True:
                print("Computer wins!!!")
            self.comp_wins += 1


    def player_choice(self):        #Getting the choice of user
        if self.verbose == True:
            print("Enter your choice:\n1 for rock \n2 for paper \n3 for scissors\n")

            sel = int(input("Your choice : "))
            while sel < 1 or sel > 3:
                sel = int(input("Err! Enter a valid choice: "))

            if self.verbose == True:
                print("You have chosen", Convertor(sel).name)
                print("=======================")

            return sel

    def comp_choice(self):          #Getting the choice of computer
        if self.verbose == True:
            print("Computer is making a move...")
        time.sleep(1)
        sel = random.randint(1,3)
        if self.verbose == True:
            print("Computer has chosen",Convertor(sel).name)
            print("=======================")

        return sel

    def playMatch(self):
        p_sel = self.player_choice()
        c_sel = self.comp_choice()
        time.sleep(1)
        self.eval(p_sel, c_sel)

    def run(self):
        if self.verbose == True:   
            while True:
                self.playMatch()
                time.sleep(1)
                self.printStatus()
                again = input("Do you want to play again (Y/N): ")
                if again.lower() == 'n':
                    break
         
            print("\n=======================\n")
            print("Final Status:")
            self.printStatus()


if __name__=="__main__":
    game = Game(True)
    game.run()
    