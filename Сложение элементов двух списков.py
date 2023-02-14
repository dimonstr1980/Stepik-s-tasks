"""
Сложение элементов двух списков
"""
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
# для сложения выбираем любой список для
# назначения диапазона, т.к. они равны :)
c = [a[i] + b[i] for i in range(len(a))]
print(*c)