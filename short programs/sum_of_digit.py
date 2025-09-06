# Sum of Digits

# Write a function to calculate the sum of digits of a given integer.


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

num = 987
print("Sum of digits:", sum_of_digits(num))
