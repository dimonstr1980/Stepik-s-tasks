"""
Пароль банка имеет вид a:b:c, где a, b и c – натуральные числа.
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
"""

def is_valid_password(password):
    s = password.split(':')
    if len(s) > 3:
        return False
    a, b, c = s[0], s[1], s[2]
    if a == a[::-1]:
        if len([i for i in range(1, int(b) + 1) if int(b) % i == 0]) == 2:
            if int(c) % 2 == 0:
                return True
    return False
    
psw = input()

print(is_valid_password(psw))