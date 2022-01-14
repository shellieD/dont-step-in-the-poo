"""
Game board functionality
"""
from random import randrange
# from time import sleep
import pyfiglet


class Board():
    """ Creates an instance of the game board

    Builds the board
    Creates coordinates for poos
    Creates coordinates for clear path

    """
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.clear_path = self._clear_path()
        self.clear_path_coord = self._clear_path_coord()
        self.poos = self._set_up_poos()
        self.board = [
            ["\U0001f7e9 " for i in range(self.cols)] for j in range(self.rows)
        ]

    def _clear_path(self):
        """ Selects random int between 0 and 8
        (not including 8)

        This random number will represent the
        row where no poos are placed.

        ---
        returns: integer
        """
        clear_path = randrange(0, 8)
        return clear_path

    def _clear_path_coord(self):
        """ Creates coordinates for clear path

        Uses return value of clear path and iterates
        through range of 8 to turn into list of tuples.

        returns: list of 8 tuples with 2 ints.
        e.g if clear_path is 4 then clear_path_coord is:
        [(4,0), (4,1), (4,2)... etc]

        """
        clear_path_coord = [(self.clear_path, x) for x in range(8)]
        return clear_path_coord

    def _set_up_poos(self):
        """ Selects random coordinates for 13 poos.

        Ensures there is at least one poo on each row
        except the row with a clear path

        ---
        returns: List of 13 tuples with 2 ints
        [(row, col), (row, col)...]

        """
        poos = []
        while len(poos) < 13:
            for i in range(8):
                if i != self.clear_path:
                    poos.append((i, randrange(0, 8)))
        return poos

    def draw_board(self):
        """Displays game board

        ---
        Prints game board with column headings and
        row indexes.

        """
        self._open_game_board()

        print("   0  1  2  3  4  5  6  7")

        for i, row in enumerate(self.board):
            print(i, " " + " ".join(row))

    def _open_game_board(self):
        """
        Displays gameboard title

        Uses pyfiglet to style title.

        """
        print("\U0001f4a9 " * 22)
        game_board = pyfiglet.figlet_format("GAME-BOARD", font="bubble")
        print(game_board)
        print("\U0001f4a9 " * 22 + " \n")
        print(
            "Make a clear path from left to right "
            "across \n the garden without stepping in dog poop! \U0001f4a9\n"
            "Step in 5 poos and it's game-over"
            "Good luck!"
        )
        print("\U0001f4a9 " * 22 + " \n")

    def update_board(self, coord_tuple):
        """ Updates board after each player guess.
        Replaces green tile with a poo if a poo is discovered.
        Replaces green tile with boot if no poo is discovered.

        ---
        Find the index for the row and then the column to locate
        the correct tile in the board to update.
        """
        if coord_tuple in self.poos:
            self.board[coord_tuple[0]][coord_tuple[1]] = '\U0001f4a9 '
        else:
            self.board[coord_tuple[0]][coord_tuple[1]] = '\U0001f97e '
