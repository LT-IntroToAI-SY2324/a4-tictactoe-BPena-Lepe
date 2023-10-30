# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self):
        self.board=['*']*9
    
    def __str__(self) ->str:
        s=""
        for x in [0,3,6]:
            s+=self.board[x+0]+" "+self.board[x+1]+" "+self.board[x+2]+"\n"
        return s

    def make_move(self,player,pos)->bool:
        if(pos<0 or pos>8 or self.board[pos]!='*'):
            return False
        self.board[pos]=player
        return True
    def has_won(self,player) ->bool:
        x=0
        while x<7:
            if x!='*' and self.board[x]==player and self.board[x]==self.board[x+1] and self.board[x+1]==self.board[x+2]:
                return True
            x+=3
        x=0
        while x<3:
            if x!='*' and self.board[x]==player and self.board[x]==self.board[3+x] and self.board[3+x]==self.board[6+x]:
                return True
            x+=1
        if x!='*' and self.board[x]==player and ((self.board[0]==self.board[4] and self.board[4]==self.board[8]) or (self.board[2]==self.board[4] and self.board[4]==self.board[6]) ):
            return True
        else:
            return False
    def game_over(self) ->bool:
        if self.has_won("X") or self.has_won("O"):
            return True
        x=0
        while x<9:
            if self.board[x]=='*':
                return False
        return True
    def clear(self) -> None:
        self.board=['*']*9
        
def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise6

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
    # play_tic_tac_toe()
