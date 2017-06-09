# New data structure: a list bd1 = [6, 4, 2, 0, 5, 7, 1, 3] represents the row
# of the queens, since the col of each queen is equal to its index and cannot
# be repeated. Note also that the row of any queen cannot be repeated, thus
# for an N x N board, any solution must be a permutation of {1 ... N-1}
# (since we are zero-indexed counting)

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # Calc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def main():
    import random
    rng = random.Random()
    bd = list(range(8))
    num_found = 0
    tries = 0
    solns = []
    for s in range(92):
        while True:
            rng.shuffle(bd)
            tries += 1
            if (not has_clashes(bd)) and (bd not in solns):
                solns.append(bd[:])
                print("found solution {0} in {1} tries.".format(bd, tries))
                tries = 0
                num_found += 1
                break
        print("total {0} unique solutions found".format(num_found))


if __name__ == "__main__":
    main()
    input()
