"""
На вход программе подается натуральное
число n, затем n строк, затем число k - количество
поисковых запросов, затем сами запросы.
Напишите программу, которая выводит все введенные строки,
в которых встречаются все поисковые запросы.
"""

strings = []
for _ in range(int(input())):
    string = input()
    strings.append(string)
keys = []
for _ in range(int(input())):
    key = input()
    keys.append(key)
res = []
for s in strings:
    count = 0
    for k in keys:
        if k.lower() in s.lower():
            count += 1
            if count == len(keys):
                res.append(s)
print(*res, sep='\n')