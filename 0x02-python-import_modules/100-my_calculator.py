#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    args = len(sys.argv)
    operators = ['+', '-', '/', '*']
    operator_used = ""
    result = 0

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operand = sys.argv[2]

        for i in operators:
            operand_found = False
            if(operand == i):
                operand_found =True
                operator_used = i
                break
        if not operand_found:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if(operator_used == '+'):
                result = add(a, b)
                print("{} {} {} = {}".format(a, operator_used, b, result))
            elif(operator_used == '-'):
                result = sub(a, b)
                print("{} {} {} = {}".format(a, operator_used, b, result))
            elif(operator_used == '*'):
                result = mul(a, b)
                print("{} {} {} = {}".format(a, operator_used, b, result))
            else:
                result = div(a, b)
                print("{} {} {} = {}".format(a, opeartor_used, b, result))
