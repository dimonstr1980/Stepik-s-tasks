"""
Список введённых чисел без нечётных индексов
"""

array = []  # выходной список
for _ in range(int(input())):  # n - цикл
    num = int(input())  # ввод чисел, и нежно
    array.append(num)  # складываем с список
del array[1::2]  #  жестко удаляем нечётные индексы срезом, и
print(array)  # вуаля