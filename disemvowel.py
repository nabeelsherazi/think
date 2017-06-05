vowels = "aeiouAEIOU"

def remove_vowels(input_string):
    '''removes vowels from an inputted string and returns new string'''
    modified_string = ""
    for c in input_string:
        if c not in vowels:
            modified_string += c
        else:
            continue
    return modified_string

input_string = input("Enter a string. \n")
output = remove_vowels(input_string)
print(output)
input()
