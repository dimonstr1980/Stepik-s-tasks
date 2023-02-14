"""
Сриниваса Рамануджан – индийский математик, славившийся своей интуицией
в области чисел. Когда английский математик Годфри Харди навестил его
однажды в больнице, он обмолвился, что номером такси, на котором он приехал,
было 1729, такое скучное и заурядное число.
На что Рамануджан ответил: "Нет, нет! Это очень интересное число.
Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами".
Другими словами: 1729 == 1**3 + 12**3 == 9**3 + 10**3

Напишите программу, которая находит аналогичные интересные числа.
В ответе запишите первые 5 чисел в порядке возрастания, включая число 1729
"""

for a in range(1, 33): 
    for b in range(1, 33): 
         for c in range(1, 33): 
            for d in range(1, 33): 
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a < c < d < b: 
                    answer = (c ** 3 + d ** 3) 
                    print(answer)