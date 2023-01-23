#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mylist = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("{}".format("out of range"))
        except ZeroDivisionError:
            print("{}".format("division by zero"))
        except (ValueError, TypeError):
            print("{}".format("wrong type"))
        finally:
            mylist.append(result or 0)
    return (mylist)
