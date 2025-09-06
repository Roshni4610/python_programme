# Check for Anagrams

# Check if two strings are anagrams (contain the same characters in different order).

#✅ Method 1: Sorting

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))
