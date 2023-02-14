"""
Списковые выражения
"""

word = 'Hello'
numbers = [1, 14, 5, 9, 12]
words = ['one', 'two', 'three', 'four', 'five', 'six']
print([0 for i in range(10)])
print([i ** 2 for i in range(1, 8)])
print([i * 10 for i in numbers])
print([c * 2 for c in word])
print([m[0] for m in words])
print([i for i in numbers if i < 10])
print([m[0] for m in words if len(m) == 3])