
import matplotlib.pyplot as plt
def collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        steps += 1
    return (True, steps)
ix = 1
steps_list = []
upperbound = int(input("Upper bound? "))
plot_type = int(input("Plot type? ('0' for histogram, '1' for scatter) "))
while ix <= upperbound:
    results = collatz(ix)
    print(ix, "...", results[0])
    steps_list.append(results[1])
    ix += 1
if plot_type == 0:
    plt.hist(steps_list, bins=max(steps_list))
    plt.title("Steps Frequency in Collatz Sequences")
    plt.ylabel("Frequency")
    plt.xlabel("Number of Steps")
    plt.show()
if plot_type == 1:
    plt.scatter(range(1, upperbound + 1), steps_list)
    plt.title("Length of Collatz Sequences")
    plt.ylabel("Number of Steps")
    plt.xlabel("n")
    plt.show()
