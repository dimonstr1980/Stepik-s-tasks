"""
Дано натуральное число. Напишите программу, которая вычисляет:
- количество цифр 3 в нем;
- сколько раз в нем встречается последняя цифра;
- количество четных цифр;
- сумму его цифр, больших пяти;
- произведение цифр, больших семи (если цифр больших семи нет,
  то вывести 1, если такая цифра одна, то вывести ее);
- сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
"""
n = int(input())
three = 0  # количество цифр 3 в нем
last = n % 10  # ввод последней цифры
count_last = 0  # сколько раз в нем встречается последняя цифра
count_even = 0  # количество четных цифр
sum_bigger_5 = 0  # сумму его цифр, больших пяти
prod_bigger_7 = 1  # произведение цифр, больших семи
count_from_0_to_5 = 0  # сколько раз в нем встречается цифры 0 и 5
while n != 0:
    last_int = n % 10
    if last_int == last:
        count_last += 1
    if last_int == 3:
        three += 1
    if last_int % 2 == 0:
        count_even += 1
    if last_int > 5:
        sum_bigger_5 += last_int
    if last_int > 7:
        prod_bigger_7 *= last_int
    if last_int == 0 or last_int == 5:
        count_from_0_to_5 += 1
    n //= 10
print(three, count_last, count_even, sum_bigger_5, prod_bigger_7, count_from_0_to_5, sep='\n')
