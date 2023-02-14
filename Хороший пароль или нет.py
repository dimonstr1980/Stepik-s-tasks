"""
Хороший пароль или нет?
"""

def is_password_good(password):
    digit = 0
    lower = 0
    upper = 0
    if len(password) < 8:
        return False
    for c in list(password):
        if c.isdigit():
            digit += 1
        elif c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    if digit > 0 and lower > 0 and upper > 0:
        return True
    else:
        return False
    
txt = input()

print(is_password_good(txt))
