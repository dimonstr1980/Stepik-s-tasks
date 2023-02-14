"""
Списковые выражения
"""
# Список палиндромов в заданном диапазоне
palindromes = [c for c in range(100, 1000) if str(c) == str(c)[::-1]]
print(*palindromes)

# Список кубов заданной последовательности чисел
cubes = [int(i) ** 3 for i in input("Введите последовательность чисел: ").split(' ')]
print(*cubes)

# Вывод слов построчно из введённой строки
words = [s for s in input("Введите свой текст: ").split()]
print(*words, sep='\n')

# Вывод чисел (выборка) из введённой строки
string = [s for s in input("Введите свой текст: ") if s.isdigit()]
print(*string, sep='')

# Вывод квадратов чётных чисел, которые не оканчиваются на цифру 4
string = [int(s) ** 2 for s in input("Введите свой текст: ").split(' ') if int(s) % 2 == 0 and int(s) ** 2 % 10 != 4]
print(*string)