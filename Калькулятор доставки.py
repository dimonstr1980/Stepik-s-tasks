"""
Калькулятор доставки
"""

def get_shipping_cost(quantity):
    delivery = 1000
    extra = 120
    if quantity > 1:
        x = delivery + ((quantity - 1) * extra)
        return x
    return delivery

n = int(input())

print(get_shipping_cost(n))