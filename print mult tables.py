def print_multiples(current_num, table_sz):
    for i in range(1, table_sz + 1):
        end_space = ""
        number_length = len(str(current_num * i))
        for j in range(5 - number_length):
            end_space = end_space + " "
        print(current_num * i, end = end_space)

def print_mult_table(table_sz):
    for n in range(1, table_sz + 1):
        print_multiples(n, table_sz)
        print()

while True:
    req_table_sz = input("What number should the table go up to? ")
    try:
        req_table_sz = int(req_table_sz)
    except:
        print("Invalid response.")
    else:
        break
print_mult_table(req_table_sz)
input()
