def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(num):
    sum_of_factorials = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += factorial(digit)
        temp //= 10
    return sum_of_factorials == num

# Example usage
numbers_to_check = [1, 2, 145, 40585, 10, 123]
for number in numbers_to_check:
    if is_strong_number(number):
        print(f"{number} is a strong number.")
    else:
        print(f"{number} is not a strong number.")
