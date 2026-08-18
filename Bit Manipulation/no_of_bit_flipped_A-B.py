a = int(input("Enter a: "))
b = int(input("Enter b: "))

x = a ^ b
count = 0

while x > 0:
    if x & 1:
        count += 1

    x = x >> 1

print("Number of bits to flip:", count)