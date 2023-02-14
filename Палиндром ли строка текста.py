"""
Палиндром ли строка текста
"""

def is_palindrome(text):
    s = "".join(c for c in text.lower() if c.isalpha())
    return s == s[::-1]

txt = input()

print(is_palindrome(txt))