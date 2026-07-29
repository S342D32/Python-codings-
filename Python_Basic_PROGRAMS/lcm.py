import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a = 15
b = 20
print(lcm(a, b))
