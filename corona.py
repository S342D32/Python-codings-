def count_handshakes(num):
    if num ==0:
        print("Enter valid num.")
    elif num ==1:
        print("One person can not do it.")
    else:
        return (num * (num-1))//2
def corona(n):
    results =[]
    for _ in range(n):
         num = int(input("Enter the no.of people:"))
         result = count_handshakes(num)
         results.append(result)
    return results
n = 5

results = corona(n)

for result in results:
    print(result)

    
