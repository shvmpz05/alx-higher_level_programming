#!/usr/bin/python3
def uppercase(str):
    uppercase = 0
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            uppercase = 32
        else:
            uppercase = 0
        print(f"{chr(ord(i) - uppercase)}", end="")
    print() 
