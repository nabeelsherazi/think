def remove_all(sub_str, string):
    clean_string = string
    pass_count = 0
    while clean_string.find(sub_str) != -1:
        sub_str_pos = clean_string.find(sub_str)
        clean_string = clean_string[0:(sub_str_pos)] + clean_string[(sub_str_pos + len(sub_str)):]
        pass_count += 1
    if pass_count == 1:
        instance_or_instances = 'instance'
    else:
        instance_or_instances = 'instances'
    print("Removed {0} {1}.".format(pass_count, instance_or_instances))
    return clean_string

input_string = input("Enter a string to parse. \n")
sub_string = input("Enter a sub-string to be removed (case sensitive). \n")
clean_string = remove_all(sub_string, input_string)
print(clean_string)
input()
