"""
На вход программе подается строка текста,
содержащая различные натуральные числа.
Из данной строки формируется список чисел.
Напишите программу, которая меняет местами
минимальный и максимальный элемент этого списка.
"""

s = input().split(' ')
for i in range(len(s)):
    s[i] = int(s[i])
x = s.index(min(s))
y = s.index(max(s))
s[x], s[y] = s[y], s[x]
print(*s)