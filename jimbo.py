def jimbo(word):
    if word[::-1] != word:
        print("not a palindrome jimbo")
    else:
        print(word)
        ix = 1
        for j in range(len(word) - 2):
            print(word[ix] + (' '*(ix - 1)) + word[ix] + (' '*(len(word) - (ix + 2))) + word[ix])
            ix += 1
        print(word)
if __name__ == "__main__":
    jimbo(input('wus poppin jimbo? '))
    input()
