"""
Магическая дата
"""

def is_magic(date):
    lst = [int(i) for i in date.split('.')]
    return lst[0] * lst[1] == lst[2] % 100

date = input()

print(is_magic(date))
