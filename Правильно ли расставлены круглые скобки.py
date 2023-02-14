"""
Правильно ли расставлены круглые скобки
"""

def is_correct_bracket(text):
    count = 0    
    for c in text:
        if count < 0:
            return False
        elif c == '(':
            count += 1
        elif c == ')':
            count -= 1
    if count == 0:
        return True
    return False

txt = input()

print(is_correct_bracket(txt))