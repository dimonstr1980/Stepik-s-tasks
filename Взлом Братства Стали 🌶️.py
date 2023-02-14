"""
Взлом Братства Стали 🌶️
"""

s = input()
for _ in range(int(s[1:])):
    s1 = input()
    if "#" in s1:
        s1 = s1[:s1.find('#')]
    print(s1.rstrip())