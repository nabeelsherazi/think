import math
import random
import time
# Data structure planning
# Board will be set up as a list of queen objects, which will be generated in
# sequential order so that each next queen does not clash with any of the last
# queens. For a board of N x N, N queens must be generated.
#
# Sample 8x8 board bd1 = [q1, q2, q3, q4, a5, q6, q7, q8] where qi = Queen(x, y)


class Board:
    """ Creates board objects, which hold queens. """
    def __init__(self, sz):
        self.queenslist = []
        self.size = sz

    def add_queen(self, queen):
        if type(queen) is not Queen:
            return "Pass queen objects only."
        elif len(self.queenslist) == self.size:
            return "Board full."
        else:
            self.queenslist.append(queen)

    def reset(self):
        self.queenslist = []


class Queen:
    """ Creates queen objects, in a specified row and column. """
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __eq__(self, other):
        return self.col == other.col and self.row == other.row

    def __ne__(self, other):
        return not (self.col == other.col and self.row == other.row)

    def __str__(self):
        return "Queen in column {0}, row {1}".format(self.col, self.row)

    def share_diagonal(self, tgt):
        """Checks if tgt queen shares a diagonal with self."""
        dx = abs(tgt.col - self.col)
        dy = abs(tgt.row - self.row)
        return dx == dy

    def clashes_left(self, board):
        for q in board.queenslist:
            if q.row == self.row:
                return True
            if self.share_diagonal(q):
                return True
        return False


def main():
    rng = random.Random()
    bd_sz = int(input("What is the board size? "))
    bd = Board(bd_sz)
    # Board is an object with attribute queenslist and method add_queens to add new queens
    print("Warning: there are {0} possible cases for this board".format(math.factorial(bd_sz)))
    t0 = time.clock()
    #import pdb; pdb.set_trace()
    candidate_solved = False
    while candidate_solved is False:
        for c in range(bd_sz):  # Need to place exactly bd_sz queens
            tries = 1
            queen_candidate = Queen(c, rng.randint(0, bd_sz - 1))  # Random seed
            candidate_solved = False
            for i in range(7):
                if not queen_candidate.clashes_left(bd):  # Alter candidate row until no longer clash
                    candidate_solved = True
                    break
                if queen_candidate.row != bd_sz - 1:  # If current row is 0-6, increment one
                    queen_candidate.row += 1
                else:  # If current row is 7, increment to zero
                    queen_candidate.row = 0
                tries += 1
            if candidate_solved is False:  # Entered impossible position
                bd.reset()
                print("Entered unsolvable board position - resetting.")
                break
            bd.add_queen(queen_candidate)  # Add copy of candidate to list
            print("Solved {0} in {1} tries.".format(str(queen_candidate), tries))
    t1 = time.clock()
    dt = t1 - t0
    time.sleep(1)
    print("Solved board in {0:.1f} seconds.".format(dt))
    print("Solution:")
    for q in bd.queenslist:
        print(q)


main()
input()

# if __name__ == "__main__":
#     q1 = Queen(5, 2)
#     q2 = Queen(2, 0)
#     q3 = Queen(3, 0)
#     q4 = Queen(4, 3)
#     q5 = Queen(4, 1)
#
#     assert not q1.share_diagonal(q2)
#     assert q1.share_diagonal(q3)
#     assert q1.share_diagonal(q4)
#     assert q1.share_diagonal(q5)
#     print("all tests passed!")
#     input()
