# Linear Search

# Implement linear search to find the index of a given element in a list. If not found, return -1.

def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1

numbers = [10, 25, 30, 45, 50]
x = 45
print(linear_search(numbers, x))
