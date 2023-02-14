"""
Подсчёт артиклей в тексте
"""

s = input().lower().split(' ')
a1 = s.count("a")
a2 = s.count("an")
a3 = s.count("the")
count = a1 + a2 + a3
print(f"Общее количество артиклей: {count}")