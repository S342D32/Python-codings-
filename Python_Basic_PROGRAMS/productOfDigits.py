num = int(input("Enter a number: "))
prod = 1
while num > 0:
    prod = prod * (num % 10)
    # make sure to give bracket to reduce error
    num = num // 10
print(prod)
