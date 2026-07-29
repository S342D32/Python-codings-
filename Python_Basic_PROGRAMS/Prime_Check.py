def prime_num(n):
    if n<1:
        return False
    is_prime = True
    for i in range(2,n):
        if n%i ==0:
            is_prime=False
            break
    return is_prime
n =34

if prime_num(n):
    print("prime")
else:
    print("not prime")

