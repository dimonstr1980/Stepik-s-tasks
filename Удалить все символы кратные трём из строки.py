"""
Удалить все символы кратные трём
из строки. 0, 3, 6 ... и т.д.
"""

s = input()
new = ''
for c in range(len(s)):
    if c % 3 != 0:
        new += s[c]
print(new)
