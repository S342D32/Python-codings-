def move_zero(arr):
    count=0
    for i in range(len(arr)):
     if arr[i]!=0:
        arr[count],arr[i]= arr[i],arr[count]
        count+=1
    return arr

arr = [2,5,0,6,7,0,9,8,4,0]
a =move_zero(arr)
print(a)