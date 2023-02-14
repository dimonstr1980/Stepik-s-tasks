"""
Вывести количество букв самого
длинного слова в тексте
"""
x = list()
for words in input().split():
    x.append(len(words))
print(max(x))

# print(max([len(a) for a in input().split()]))