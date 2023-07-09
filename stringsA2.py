def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s if c in "aeiouAEIOU")

def capitalize(s):
    return s.upper()
