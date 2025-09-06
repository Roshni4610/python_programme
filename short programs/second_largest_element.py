# Find Second Largest Element

# Find the second largest number in a list without using built-in sorting.

def second_largest(lst):
    unique = set(lst)   # remove duplicates
    if len(unique) < 2:
        return None
    unique.remove(max(unique))  # remove largest
    return max(unique)

numbers = [10, 20, 4, 45, 99, 99]
print("Second largest:", second_largest(numbers))
