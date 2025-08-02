def add(x, y):
    """Performs addition of two numbers."""
    return x + y

def subtract(x, y):
    """Performs subtraction of two numbers."""
    return x - y

def multiply(x, y):
    """Performs multiplication of two numbers."""
    return x * y

def divide(x, y):
    """
    Performs division of two numbers.
    Handles division by zero error.
    """
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def calculator():
    """
    Main function to run the arithmetic calculator.
    Takes two numbers and an operator from the user, then performs the calculation.
    """
    print("Welcome to the Simple Python Calculator!")
    print("---------------------------------------")

    while True:
        try:
            # Get the first number from the user
            num1_str = input("Enter first number: ")
            num1 = float(num1_str) # Convert input to a float for decimal support

            # Get the second number from the user
            num2_str = input("Enter second number: ")
            num2 = float(num2_str) # Convert input to a float

            # Get the operator choice from the user
            operator = input("Choose an operation (+, -, *, /): ")

            result = None # Initialize result variable

            # Perform the chosen operation based on user input
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please choose from +, -, *, or /.")
                continue # Ask for input again if operator is invalid

            # Print the result if a valid operation was performed
            if result is not None:
                print(f"The result of {num1} {operator} {num2} is: {result}")

        except ValueError:
            # Handle cases where user enters non-numeric input for numbers
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Thank you for using the calculator! Goodbye.")
            break # Exit the loop if user doesn't want to continue

calculator()