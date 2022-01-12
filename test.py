from random import randrange


class Board():

    def __init__ (self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.clear_path = self._clear_path()
        self.clear_path_coord = self._clear_path_coord()
        self.poos = self._set_up_poos()

    def _clear_path(self):
        clear_path = randrange(0, 8)
        return clear_path

    def _clear_path_coord(self):
        clear_path_coord = [(self.clear_path, x) for x in range(8)]
        print(clear_path_coord)
        return clear_path_coord 

    def _set_up_poos(self):
        poos = []
        for i in range(8):
            if i != self.clear_path:
                poos.append((i, randrange(0, 8)))
        print(poos)
        return poos

    def draw_board(self):
        board = [["\U0001f7e9 " for i in range(self.cols)] for j in range(self.rows)]

        for row in board:
            print(" ".join(row))


test = Board(8, 8)   

test.draw_board()


