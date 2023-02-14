"""
Сортировка чисел
"""

s = input().split(' ')
s.sort(key = int)
print(*s)
s.sort(reverse = True, key = int)
print(*s)