"""
Сумма факториалов числа (n)
n! = 1! + 2! + 3! + ... + n!
"""

num = int(input())
total = 0
product = 1
for i in range(1, num + 1):
    product *= i
    total += product
print(total)