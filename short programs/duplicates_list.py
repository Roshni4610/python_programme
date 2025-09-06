# Remove Duplicates from a List

# Remove duplicate elements from a list without using set().

def remove_duplicates(lst):
    return list({}.fromkeys(lst))

numbers = [1, 2, 2, 3, 4, 1, 5, 3]
print(remove_duplicates(numbers))
