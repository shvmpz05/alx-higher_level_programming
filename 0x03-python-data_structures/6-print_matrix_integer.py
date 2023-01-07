#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for z in x:
            if z != x[-1]:
                print("{} ".format(z), end='')
            else:
                print("{}".format(z), end='')
        print()
