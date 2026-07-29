# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def first_last(arr,target):
    n= len(arr)
    arr.sort()
    first = -1
    last =-1
    for i in range(n):
        if arr[i] == target:
            if first == -1:
               first = i
            last = i
            
    return first,last
            
            
arr=[3,4,1,7,6,9,1,2,3]
target = 3
print(first_last(arr,target))