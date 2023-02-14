"""
На вход программе подается натуральное
число n, а затем n строк, затем еще одна
строка — поисковый запрос. Напишите программу,
которая выводит все введенные строки,
в которых встречается поисковый запрос.
"""

strings = []
for _ in range(int(input())):
    string = input()
    strings.append(string)
key = input()
res = []
for s in strings:
    if key.lower() in s.lower():
        res.append(s)
print(*res, sep='\n')