num = int(input("Enter a no:"))
i =2
is_prime =True
while i <= num//2:
    if num%i ==0:
        is_prime=False
        break
    i +=1
if is_prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
