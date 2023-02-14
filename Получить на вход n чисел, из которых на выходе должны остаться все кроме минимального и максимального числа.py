"""
Получить на вход n чисел, из которых
на выходе должны остаться все кроме
минимального и максимального числа.
"""

nums = []
for _ in range(int(input())):
    x = int(input())
    nums.append(x)
del nums[nums.index(min(nums))]
del nums[nums.index(max(nums))]
print(*nums, sep='\n')