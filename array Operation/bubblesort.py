def bubbleSort(arr):
    n =len(arr)
    for i in range(n):
        
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr = [2,5,0,6,7,0,9,8,4,0]
a =bubbleSort(arr)
print(arr)