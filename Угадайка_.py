import random

n = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100
 
 
while True: 
  your_number = input('Your number between 1 and 100 is:', )
  if is_valid(your_number) == False:
    print('А может быть все-таки введем целое число от 1 до 100?')
    continue
  else:
    number = int(your_number)
    break