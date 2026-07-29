import random 
def fisher(arr):
    for i in range (len(arr)-1,0,-1):
        j=random.randint(0,i)
        arr[i],arr[j] = arr[j],arr[i]
    return arr
arr = [1, 2, 3, 4, 5]
print(fisher(arr)) 