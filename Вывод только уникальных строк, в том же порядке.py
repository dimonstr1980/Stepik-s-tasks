"""
На вход программе подается натуральное
число n, а затем n строк. Напишите программу,
которая выводит только уникальные строки,
в том же порядке, в котором они были введены.
"""

words = []
for _ in range(int(input())):
    s = input()
    if s not in words:
        words.append(s)
print(*words, sep='\n')