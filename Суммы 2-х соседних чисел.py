"""
Суммы 2-х соседних чисел, заданного списка чисел
"""

array = []  # выходной список
sum_two = []  # список для суммы 2-х чисел
for _ in range(int(input())):  # n - цикл
    num = int(input())  # ввод чисел
    sum_two.append(num)  # добавляем число в список для сумм
    if len(sum_two) > 1:  # если в списке более 1 числа, то
        array.append(sum(sum_two))  # складываем их, а
        del sum_two[0]  # первый элемент удаляем
print(array)  # вуаля