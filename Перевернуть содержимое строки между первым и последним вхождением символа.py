"""
Перевернуть содержимое строки между
первым и последним вхождением символа 'h'
Пример: 123hTRAPh321 --> 123hPARTh321
"""

s = input()
start = s[:s.find('h') + 1]
mid = s[s.rfind('h') - 1:s.find('h'):-1]
end = s[s.rfind('h'):]
print(f'{start}{mid}{end}')