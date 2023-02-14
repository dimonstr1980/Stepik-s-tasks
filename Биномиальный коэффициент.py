"""
Биномиальный коэффициент (ниже формула)
    n!
----------
k!(n - k!)
"""

def factorial(x):
    mul = 1
    for i in range(2, x + 1):
        mul *= i
    return mul
    
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n = int(input())
k = int(input())

print(compute_binom(n, k))