"""
На вход программе подается одна строка.
Напишите программу, которая определяет
сколько в ней одинаковых соседних символов.
"""
s = input()
total = 0
char = ''
for c in range(len(s)):
    if s[c] is not char:
        char = s[c]
    else:
        total += 1
print(total)