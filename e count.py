import time
import string

def remove_punctuation(input_string):
    '''removes punctuation from a string and returns it split into a list'''
    clean_string = ''
    for c in input_string:
        if c not in string.punctuation:
            clean_string += c
    return clean_string.split()

def tally_es(word_list):
    '''tallies total number of words and number of words with 'e's in them'''
    total_count = 0
    e_count = 0
    for wd in word_list:
        if 'e' in wd or 'E' in wd:
            e_count += 1
        total_count += 1
    return (total_count, e_count)

input_string = input("Enter a string to be analyzed. \n")
start_time = time.clock()
print("Analyzing string.")
word_list = remove_punctuation(input_string)
counts = tally_es(word_list)
e_percentage = round((counts[1] / counts[0]) * 100)
end_time = time.clock()
delta_time = end_time - start_time
print("String analyzed in {0:.4f} seconds.".format(delta_time))
print("Your text contains {0} words, of which {1} ({2}%) contain an \"e\".".format(counts[0], counts[1], e_percentage))
print("Isn't that wild?")
input()
