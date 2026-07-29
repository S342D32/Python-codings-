def is_perfect(number):
    # Initialize sum of divisors
    sum_of_divisors = 0
    
    # Find all divisors and add them
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    
    # Check if sum of divisors is equal to the number
    return sum_of_divisors == number

# Input from the user
num = int(input("Enter a number: "))

# Check and print result
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
