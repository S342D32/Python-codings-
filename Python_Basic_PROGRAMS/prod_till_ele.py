def prod(n):
    prod =1
    while n > 0:
        prod*=n
        n-=1
    return prod
n = int(input("Enter a no.:"))
print(prod(n))