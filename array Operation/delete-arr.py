def delete(arr, val):
    k = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]
            k += 1
    return k

arr = list(map(int,input("Enter array of number separated by comma:").split()))
val = int(input("Enter no. to delete:"))
k = delete(arr, val)
print("New length of array:", k)
print("Array without deleted elements:", arr[:k])
