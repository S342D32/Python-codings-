from math import factorial

n = int(input("Enter a no:"))

for i in range(n):
    for j in range(1,n-i+1):
        print(end=" ")
    for r in range(i+1):
        csr = factorial(i)//(factorial(r) * (factorial(i-r)))
        print(csr,end=' ')
    print(' ')