#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    total = 0
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = str(sys.argv[2])
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if operator == '+':
        total = add(a, b)
    elif operator == '-':
        total = sub(a, b)
    elif operator == '*':
        total = mul(a, b)
    elif operator == '/':
        total = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print('{} {} {} = {}'.format(a, operator, b, total))
    exit(0)
