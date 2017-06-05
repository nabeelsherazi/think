import time

def is_prime(number):
    for f in range(2, number//2):
        if number % f == 0: #if the modulus of the factor is zero, then it is a factor of that number
            return False
    return True

prime_counter = 1
while True:
    try:
        end_prime = input('What number prime do you want? \n')
        end_prime = int(end_prime)
        if end_prime < 1:
            raise ValueError
    except:
        print('Invalid response.')
    else:
        break
current_number = 3
if end_prime == 1:
    print('The 1st prime number is 2! Duh!')
    input()
    raise SystemExit

start_time = time.clock()
while prime_counter != end_prime:
    if is_prime(current_number) == True:
        prime_counter += 1
    current_number += 2
end_time = time.clock()
delta_time = end_time - start_time

ending_number = int(str(end_prime)[-1])
if ending_number == 1:
    ending_type = 'st'
elif ending_number == 2:
    ending_type = 'nd'
elif ending_number == 3:
    ending_type = 'rd'
elif ending_number >= 4 or ending_number == 0:
    ending_type = 'th'

print('The {0}{1} prime number is {2}! (calculated in {3:.3f} seconds)'.format(end_prime, ending_type, (current_number - 2), delta_time))
input()
