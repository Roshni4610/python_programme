while True:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    op = input("Enter operation (+, -, *, /, %): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "%":
        print("Result:", a % b)
    elif op == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator.")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "y":
        print("Goodbye!")
        break
