"""
Найти ближайшее простое число после введённого
"""

def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2
    # Я для краткости взял однострочник из решений. Вставьте какой по-душе
    
def get_next_prime(num):
    x = num + 1
    while is_prime(x) is False:
        x += 1
    return x

n = int(input())

print(get_next_prime(n))