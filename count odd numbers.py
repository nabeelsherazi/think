def count_odd_numbers(list):
    counter = 0
    for n in list:
        if n % 2 == 0:
            continue
        else:
            counter += 1
    return counter

while True:
    input_list = input("Enter your list of numbers separated by commas. \n")
    try:
        input_list = input_list.split(", ")
        new_input_list = []
        for i in input_list:
            new_input_list.append(int(i))
        count = count_odd_numbers(new_input_list)
    except:
        print("Invalid entry.")
    else:
        break
print("There are", count, "odd numbers in that list!")
input()
