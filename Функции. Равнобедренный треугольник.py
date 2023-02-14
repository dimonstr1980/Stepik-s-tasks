"""
Равнобедренный треугольник
"""

def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for i in reversed(range(base // 2 + 1)):
        print(fill * i)

fill = input()
base = int(input())

draw_triangle(fill, base)