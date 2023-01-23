#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    if (my_list):
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end="")
                counter += 1
            except IndexError:
                print()
                return (counter)
    print()
    return counter
