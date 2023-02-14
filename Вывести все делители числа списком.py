"""
Вывести все делители числа списком
"""

num = int(input())
array = []
for i in range(1, num + 1):
    if num % i == 0:
        array.append(i)
print(array)

# def get_days(month):
#     return [i for i in range(1, num + 1)
#                         if num % i == 0]

# num = int(input())

# print(get_days(num))