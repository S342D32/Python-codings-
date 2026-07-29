def count_handshakes(num):
    if num == 0:
        return "Enter valid people"
    elif num == 1:
        return "One person can't Handshake"
    else:
        return (num * (num - 1)) // 2

def corona(n):
    results = []
    for _ in range(n):
        num = int(input("Total no. of people: "))
        result = count_handshakes(num)
        results.append(result)
    return results

n = int(input("No. of testCases: "))
results = corona(n)

for result in results:
    print(result)
