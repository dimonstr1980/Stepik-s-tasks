"""
На вход подаётся строка из 4-х
чисел, разделённые точкой.
Выяснить является данное число IP-адресом.
"""

s = input().split(".")
count = 0
for i in s:
    if 0 <= int(i) <= 255:
        count += 1
if count == 4:
    print("ДА")
else:
    print("НЕТ")