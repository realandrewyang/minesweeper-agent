from queue import Queue
import random

class Game:
    """
        A cell is one of

        Unrevealed
        Revealed Mine   -1
        Revealed Number x
        Revealed Empty  0
    """
    MINE = -1

    PLAY = "play"
    LOSE = "lose"
    WIN = "win"

    HIDDEN = "hidden"
    FLAGGED = "flagged"
    REVEALED = "revealed"

    def withinBounds(self, i, j):
        return i >= 0 and i < self.ROWS and j >= 0 and j < self.COLUMNS

    def print(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))

    def __init__(self, rows, columns, mines):
        assert rows >= 0
        assert columns >= 0
        assert mines >= 0 and mines <= rows * columns

        self.ROWS = rows
        self.COLUMNS = columns
        self.MINES = mines
        self.board = [[0 for j in range(self.COLUMNS)] for i in range(self.ROWS)]
        self.display = [[Game.HIDDEN for j in range(self.COLUMNS)] for i in range(self.ROWS)]
        self.STATE = Game.PLAY
        self.hiddenCells = self.ROWS * self.COLUMNS - self.MINES

        minesToPlace = self.MINES
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if minesToPlace == 0:
                    return

                # Place mine
                p = random.randrange(0, self.ROWS * self.COLUMNS - i * self.ROWS + j)
                if p <= minesToPlace:
                    self.board[i][j] = Game.MINE
                    minesToPlace -= 1

                    # Update counts
                    for iDelta in range(-1, 2):
                        for jDelta in range(-1, 2):
                            tempI, tempJ = i + iDelta, j + jDelta
                            if self.withinBounds(tempI, tempJ) and self.board[tempI][tempJ] != Game.MINE:
                                self.board[tempI][tempJ] += 1

    def reveal(self, i, j):
        if self.STATE != Game.PLAY:
            return
        if not self.withinBounds(i, j):
            return
        if self.display[i][j] != Game.HIDDEN:
            return
        self.display[i][j] = Game.REVEALED
        if self.board[i][j] == Game.MINE:
            self.STATE = Game.LOSE
            return
        # TODO reveal algorithm
        

    def flag(self, i, j):
        if self.STATE != Game.PLAY:
            return
        if not self.withinBounds(i, j):
            return
        if self.display[i][j] == Game.REVEALED:
            return
        if self.display[i][j] == Game.FLAGGED:
            self.display[i][j] = Game.HIDDEN
            return
        if self.display[i][j] == Game.HIDDEN:
            self.display[i][j] = Game.HIDDEN
            return

"""
TESTING
random.seed(0)
g = Game(10, 10, 10)
g.print()
g.reveal(0, 1)
"""
