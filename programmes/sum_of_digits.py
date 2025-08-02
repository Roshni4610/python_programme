# sum of digit of a number:

num = input("Enter a number:")
sum_digit = sum(int(digit) for digit in num)
print("Sum of digit:", sum_digit)