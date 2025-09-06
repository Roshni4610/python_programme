# Count Frequency of Elements in a List

# Given a list, count how many times each element appears.

from collections import Counter

numbers = [1, 2, 2, 3, 1, 4, 2, 3]
freq = Counter(numbers)
print(freq)
