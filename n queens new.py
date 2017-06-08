# Data structure planning
# Board will be set up as a list of queen objects, which will be generated in
# sequential order so that each next queen does not clash with any of the last
# queens. For a board of N x N, N queens must be generated.
#
# Sample 8x8 board bd1 = [q1, q2, q3, q4, a5, q6, q7, q8] where qi = Queen(x, y)

class Board:
    """Creates board objects, which hold queens."""
    def __init__(self, sz):
        self.queenslist = []
        self.size = sz

    def add_queen(queen):
        if len(self.queenslist) == self.sz:
            return "Board full."
        else:
            self.queenslist.append(queen)


class Queen:
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def share_diagonal(self, tgt):
        """Checks if tgt queen shares a diagonal with self."""
        dx = abs(tgt.col - self.col)
        dy = abs(tgt.row - self.row)
        return dx == dy

    def clashes_left(self, board):
        for q in board.queenslist:
            if q.row == self.row:
                return True


if __name__ == "__main__":
    q1 = Queen(5, 2)
    q2 = Queen(2, 0)
    q3 = Queen(3, 0)
    q4 = Queen(4, 3)
    q5 = Queen(4, 1)

    assert not q1.share_diagonal(q2)
    assert q1.share_diagonal(q3)
    assert q1.share_diagonal(q4)
    assert q1.share_diagonal(q5)
    print("all tests passed!")
    input()
