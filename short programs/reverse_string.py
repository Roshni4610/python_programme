#  Reverse a String

# Write a Python function to reverse a string without using built-in reverse functions.

#✅ Method 1: Using slicing (most common & Pythonic)
text = "hello"
reversed_text = text[::-1]
print(reversed_text)

#✅ Method 2: Using reversed() with join()
text = "hello"
reversed_text = "".join(reversed(text))
print(reversed_text)

#✅ Method 3: Using str.join() + reversed() + list()
text = "hello"
reversed_text = ''.join(list(reversed(text)))
print(reversed_text)


