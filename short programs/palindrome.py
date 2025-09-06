#Check for Palindrome

#Check if a string is a palindrome (reads the same forwards and backwards).

def is_palindrome(s):
    # Compare string with its reverse
    return s == s[::-1]

word = "racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
