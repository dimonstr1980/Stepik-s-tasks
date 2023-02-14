"""
Найти все вхождения символа в строке
"""

def find_all(target, symbol):
    return [c for c in range(len(target))
            if target[c] == symbol]
    
s = input()
char = input()

print(find_all(s, char))

# def find_all(target, symbol):
#     array = []
#     for c in range(len(target)):
#         if target[c] == symbol:
#             array.append(c)
#     return array
    
# s = input()
# char = input()

# print(find_all(s, char))