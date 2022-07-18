# Rock, Paper and Scissors
This is a python application to play the game of Rock, Paper and Scissors against the computer. The application asks the player to enter his choice and
also makes a choice for the computer. Then the game is played and the winner is decided according to the rules of the game. At the end of the game, player
gets an option to choose whether to continue playing or to exit from the game.

To check the correctness of algorithm, the application uses `unittest` module to run tests for a lot of testcases.
## Playing the game
Run the `assign.py` and enter your choice when prompted to do so.
```
$ python3 assign.py
Let's play Rock, Paper and Scissors
=======================
Enter your choice:
1 for rock 
2 for paper 
3 for scissors

Your choice : 1
```
After entering your choice, the computer makes a move and the winner(or draw) is decided. After that, you get an option whether to continue playing or exit
the game.
```
=======================
You : Rock | Computer : Paper
=======================
Computer wins!!!
Games played:  1
Player wins:  0
Computer wins:  1
Draws:  0
Do you want to play again (Y/N): 
```
If you enter `Y/y`, the game continues and the above steps are repeated. If you enter `N/n`, the game stops and the final score is displayed.
```
Final Status:
Games played:  1
Player wins!!!:  0
Computer wins:  0
Draws:  1
```
Run the `test.py` file to run the tests.
```
$ python3 test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''
