n = int(input("Enter a number: "))

def armstrong(n):
    sum =0
    temp =n
    while temp>0:
        digit = temp%10
        sum += digit**3
        temp = temp//10
    return sum

if n == armstrong(n):
    print("armstrong")
else:
    print(" not armstrong")


