"""
Численный треугольник с заданной высотой,
и порядковым выводом от 1
"""
num = int(input())
line = 1
for i in range(1, num + 1):
    for _ in range(i):
        print(line, end=' ')
        line += 1
    print()