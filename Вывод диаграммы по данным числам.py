"""
На вход подаётся строка из чисел:
Вывод диаграммы по данным числам.
"""

s = input().split()
res = []
for i in s:
    x = int(i) * "+"
    res.append(x)
print('\n'.join(res))