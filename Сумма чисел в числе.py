"""
Сумма чисел в числе
"""

def print_digit_sum(num):
    lst = 0
    while num != 0:
        last_digit = num % 10
        lst += last_digit
        num = num // 10
    print(lst)

n = int(input())

print_digit_sum(n)