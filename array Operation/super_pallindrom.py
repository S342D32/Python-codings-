def is_palindrome(n):
    rev = 0
    org_num = n
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev == org_num

def is_super_palindrome(n):
    sqrt = int(n ** 0.5)
    return is_palindrome(n) and is_palindrome(sqrt) and (sqrt * sqrt == n)

n = 123
if is_super_palindrome(n):
    print("Super Palindrome")
else:
    print("Not Super Palindrome")
