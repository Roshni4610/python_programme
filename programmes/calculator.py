# Calculator = Add,Subtract,Multiply,Divide two number.

class Calculator:
    @staticmethod
    def add(x, y):
        return print(x + y)

    @staticmethod
    def subtract(x, y):
        return print(x - y)

    @staticmethod
    def multiple(x, y):
        return print(x * y)

    @staticmethod
    def divide(x, y):
        print(x / y)
        if y != 0:
            print("cannot divide")
        else:
            print(x / y)


while True:

    x = float(input("Enter a number 1:"))
    op = input("Enter a operator(+, -, *, /):")
    y = float(input("enter a number 2:"))

    if op == "+":
        Calculator.add(x, y)
    elif op == "-":
        Calculator.subtract(x, y)
    elif op == "*":
        Calculator.multiple(x, y)
    elif op == "/":
        Calculator.divide(x, y)
    else:
        print("invalid operator(+, -, *, /,)")
