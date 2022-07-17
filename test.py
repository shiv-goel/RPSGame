import assign
import unittest

class GameTest(unittest.TestCase):
    def test_initialization(self):
        game = assign.Game(False)
        self.assertEqual(game.player_wins, 0)
        self.assertEqual(game.comp_wins,0)
        self.assertEqual(game.draws,0)

    def test_eval(self):
        game = assign.Game(False)

        #Both the player and computer made the same choice
        for i in range(1,4):  
            cur1 = game.player_wins
            cur2 = game.comp_wins
            cur3 = game.draws
            game.eval(i,i)
            self.assertEqual(game.player_wins,cur1)
            self.assertEqual(game.comp_wins,cur2)
            self.assertEqual(game.draws,cur3 + 1)

        #Player chooses Rock and computer chooses Paper
        cur1 = game.player_wins
        cur2 = game.comp_wins
        cur3 = game.draws
        game.eval(1,2)
        self.assertEqual(game.player_wins,cur1)
        self.assertEqual(game.comp_wins,cur2 + 1)
        self.assertEqual(game.draws,cur3 )

        #Player chooses Rock and computer chooses Scissors
        cur1 = game.player_wins
        cur2 = game.comp_wins
        cur3 = game.draws
        game.eval(1,3)
        self.assertEqual(game.player_wins,cur1 + 1)
        self.assertEqual(game.comp_wins,cur2)
        self.assertEqual(game.draws,cur3)

        #Player chooses Paper and computer chooses Rock
        cur1 = game.player_wins
        cur2 = game.comp_wins
        cur3 = game.draws
        game.eval(2,1)
        self.assertEqual(game.player_wins,cur1 + 1)
        self.assertEqual(game.comp_wins,cur2)
        self.assertEqual(game.draws,cur3)

        #Player chooses Paper and computer chooses Scissors
        cur1 = game.player_wins
        cur2 = game.comp_wins
        cur3 = game.draws
        game.eval(2,3)
        self.assertEqual(game.player_wins,cur1)
        self.assertEqual(game.comp_wins,cur2 + 1)
        self.assertEqual(game.draws,cur3)

        #Player chooses Scissors and computer chooses Rock
        cur1 = game.player_wins
        cur2 = game.comp_wins
        cur3 = game.draws
        game.eval(3,1)
        self.assertEqual(game.player_wins,cur1)
        self.assertEqual(game.comp_wins,cur2 + 1)
        self.assertEqual(game.draws,cur3)

        #Player chooses Scissors and computer chooses Paper
        cur1 = game.player_wins
        cur2 = game.comp_wins
        cur3 = game.draws
        game.eval(3,2)
        self.assertEqual(game.player_wins,cur1 + 1)
        self.assertEqual(game.comp_wins,cur2)
        self.assertEqual(game.draws,cur3)
        
if __name__=="__main__":
    unittest.main()