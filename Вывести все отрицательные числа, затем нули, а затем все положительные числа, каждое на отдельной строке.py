"""
На вход программе подается натуральное число
n, а затем n целых чисел. Напишите программу,
которая сначала выводит все отрицательные числа,
затем нули, а затем все положительные числа,
каждое на отдельной строке. Числа должны быть
выведены в том же порядке, в котором они были введены
"""

nums = []
for _ in range(int(input())):
    num = int(input())
    nums.append(num)
negatives = []
zeros = []
positives = []
for n in nums:
    if n < 0:
        negatives.append(n)
    elif n == 0:
        zeros.append(n)
    elif n > 0:
        positives.append(n)
res = negatives + zeros + positives
print(*res, sep='\n')