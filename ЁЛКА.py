"""
ЁЛКА
"""

def draw_triangle():
    s, p = '*', ' '
    for i in range(8):
        print(p * (8 - 1 - i) + s * (1 + i * 2))

draw_triangle()