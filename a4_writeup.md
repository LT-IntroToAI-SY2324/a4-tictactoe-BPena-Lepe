# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
    The most difficult was the has won method.
2. Explain how you would add a computer player to the game.
    I would create another class, maybe a subclass, and would add a method to play on the board.
3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

If there are 2 xs or  2 os in a row I would make the compute play in the next spot over, and if there was a one square gap between 2xs or 2os the compute would place its move in betweens.