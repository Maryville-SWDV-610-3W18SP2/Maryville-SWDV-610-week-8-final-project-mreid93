"""
Matthew Reid
SWDV 610 - Data Structure, Spring 2018
Final Project

For my final, I tackled the Knight's Tale. Using a fairly short recursive algorithm, my solution is below.
All I've done is created a class for a Board (representing chess board) with methods for determing if a move is valid and generator for all possible moves.
Then, using a recursive function, we find the possible move with the least number of next possible moves
and travel there. This is done repeatedly until all board moves have been exhausted.
"""
class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

    def isValidMove(self, cell):
        x, y = cell
        return (x >= 0 and x <= self.width-1) and (y >=0 and y <= self.height-1)

    def possibleMoves(self, cell):
        x, y = cell
        listOfMoves = [[x+1, y-2], [x+2, y-1], [x+2, y+1], [x+1, y+2],
               [x-1, y-2], [x-2, y-1], [x-2, y+1], [x-1, y+2]]
        for elem in listOfMoves:
            if self.isValidMove(elem):
                # Using yield because we are returning a generator
                yield elem
        
def knightsTour(start, path):
    if not path:
        path = (start)
    if len(path) == board.area:
        yield path
    for next_cell in board.possibleMoves(start):
        if next_cell not in path:
            path += (next_cell,)
            # Using yield because we are returning a generator
            yield from knightsTour(next_cell, path)

# Used a 4x4 board
board = Board(4,4)
moves = list(knightsTour([0,0], tuple()))
print(moves[0])
print('Done!')