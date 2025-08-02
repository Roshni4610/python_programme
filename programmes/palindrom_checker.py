#Palindrome Checker
while True:
    text = input("Enter a text:")
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")