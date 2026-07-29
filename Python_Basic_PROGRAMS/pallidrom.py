n = int(input("Enter a number: "))

def palindrome(n):
    rev = 0
    org = n
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev == org

if palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
