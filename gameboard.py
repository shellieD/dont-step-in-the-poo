"""
Game board functionality
"""
from random import randrange
# from time import sleep
import pyfiglet


class Board():
    """
    Creates an instance of the game board
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
        clear_path = randrange(0, 8)
        return clear_path

    def _clear_path_coord(self):
        clear_path_coord = [(self.clear_path, x) for x in range(8)]
        return clear_path_coord

    def _set_up_poos(self):
        poos = []
        while len(poos) < 13:
            for i in range(8):
                if i != self.clear_path:
                    poos.append((i, randrange(0, 8)))
        return poos

    def draw_board(self):
        """
        Displays game board
        """
        self._open_game_board()

        print("   0  1  2  3  4  5  6  7")

        for i, row in enumerate(self.board):
            print(i, " " + " ".join(row))

    def _open_game_board(self):
        """
        Opens game board ready to play or something like that
        """
        print("\U0001f4a9 " * 22)
        game_board = pyfiglet.figlet_format("          GAME-BOARD", font="bubble")
        print(game_board)
        # print(
        #     " \n"
        #     "Top left corner is row 0, col 0. "
        #     "Bottom right corner is row 7, col 7.\n"
        #     "Make a clear path across the garden "
        #     "horizontally without stepping in dog poop! \U0001f4a9\n"
        #     "Step in 5 poos and it's game-over! \n"
        #     "GOOD LUCK!"
        # )
        print("\U0001f4a9 " * 22 + " \n")

# coord_tuple is a tuple of a couple of integers
# (row, cols)
# poos is a list of tuples of a couple of integers
# each tuple is a coordinate of a poo (row, cols)
    def update_board(self, coord_tuple):
        if coord_tuple in self.poos:
            print("Splat")
            self.board[coord_tuple[0]][coord_tuple[1]] = '\U0001f4a9 '
        else:
            self.board[coord_tuple[0]][coord_tuple[1]] = '\U0001f97e '

# new_board = Board(8, 8)

# new_board.draw_board()
