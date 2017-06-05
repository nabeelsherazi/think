import time, string, sys
def print_slow(string):
    print(">>>", end=' ')
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)
    print()
while True:
    print_slow("What is your question?")
    question_input = input(">>> ")
    time.sleep(.25)
    print_slow("Worry not, child.")
    time.sleep(.25)
    print_slow("Mitochondria is the powerhouse of the cell.")
    time.sleep(.25)
    print_slow("Does this resolve your fears?")
    does_resolve = input(">>> ")
    clean_does_resolve = ""
    for i in does_resolve:
        if i not in string.punctuation:
            clean_does_resolve += i
    if clean_does_resolve.lower() == "yes":
        time.sleep(.25)
        print_slow("Good.")
        time.sleep(.25)
        print_slow("We are proud of your successes.")
        break
input()
