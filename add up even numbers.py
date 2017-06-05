def add_even_numbers(list):
    sum = 0
    for n in list:
        if n % 2 != 0:
            continue
        else:
            sum += n
    return sum

while True:
    input_list = input("Enter your list of numbers separated by commas. \n")
    try:
        input_list = input_list.split(", ")
        new_input_list = []
        for i in input_list:
            new_input_list.append(int(i))
        sum = add_even_numbers(new_input_list)
    except:
        print("Invalid entry.")
    else:
        break
print("The sum of all even numbers in this list is", sum)
input()
