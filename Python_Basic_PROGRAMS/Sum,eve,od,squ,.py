N = int(input("Enter a number: "))
i = 2
sum_even = 0
while i <= N:
    # if odd to countthen i =1
    # if sum of square then   sum += i**2
    sum_even += i
    i += 2
print(f"Sum of even numbers: {sum_even}")
