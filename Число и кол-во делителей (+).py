"""
На вход программе подается натуральное число n.
Напишите программу, выводящую графическое изображение
делимости чисел от 1 до n включительно. В каждой строке
надо напечатать очередное число и столько символов «+»,
сколько делителей у этого числа.
"""

num = int(input())
for i in range(1, num + 1):
    count = ''
    for j in range(1, i + 1):
        if i % j == 0:
            count += '+'
    print(i, count, sep='')


# def number_of_factors(num):
#     return len([i for i in range(1, num + 1)
#                             if num % i == 0])

# n = int(input())

# print(number_of_factors(n))