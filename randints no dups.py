import random

def no_dups(terms, lbound, ubound):
    output = []
    while len(output) != terms:
        cand = rng.randint(lbound, ubound)
        if cand not in output:
            output.append(cand)
    return output

rng = random.Random()
print("This program will return any number of non-repeating random numbers between two bounds you specify")
while True:
    terms_input = input("How many random numbers do you want? \n")
    lbound_input = input("What is the lower bound for numbers? (Note: lower bound will be included in range of possible numbers) \n")
    ubound_input = input("What is the upper bound for numbers? (Note: upper bound will not be included in range of possible numbers) \n")
    try:
        terms_input = int(terms_input)
        lbound_input = int(lbound_input)
        ubound_input = int(ubound_input)
    except TypeError:
        print("One of the entered values is not a valid number!")
    if lbound_input > ubound_input:
        print("Invalid range of numbers!")
    elif (ubound_input - lbound_input) < terms_input:
        print("More terms requested than possible in range!")
    else:
        break
print(no_dups(terms_input, lbound_input, ubound_input))
input()
