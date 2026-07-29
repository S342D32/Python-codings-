num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print(f"Reversed number is: {rev}")
