import sys, time
sys.path.append('C:\\Users\\nxtfa\\Desktop\\Programming\\my lib')
from testsuite import *
from searchalgos import *

def remove_adjacent_dups(xs):
    result = []
    mre = None
    for e in xs:
        if e != mre:
            result.append(e)
            mre = e
    return result

test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])
