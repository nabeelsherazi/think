def find(strng, ch, start=0, end=None):
    '''Finds and returns the index of ch in strng, starting at start and ending at end.
    Returns -1 if ch not found.
    Default start is [0] and default end is None'''
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

string = input("What string do you want to search? \n")
char = input("What character do you want to search for? \n (single letter only) ")
req_start_point = input("Do you want to request a starting point? Type 'yes' or 'no'.").lower()
if req_start_point == 'yes':
    start_point = int(input("What index would you like to start from? \n (type a number from 0 to 1 minus the length of your string)"))
else: start_point = 0
req_end_point = input("Do you want to request an ending point? Type 'yes' or 'no'. ").lower()
if req_end_point == 'yes':
    end_point = int(input("What index would you like to end at? \n (type a number from 0 to 1 minus the length of your string)"))
else:
    end_point = None
print("Running search...")
result = find(string, char, start_point, end_point)
if result != -1:
    print("Character {0} found at index {1}!".format(char, result))
else:
    print("Character not found (-1)")
input()
