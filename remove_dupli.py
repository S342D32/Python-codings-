# def remove_duplicate(arr):
#     if not arr:
#         return 0
#     arr.sort()  # Sort the array first
#     a = 1
#     for i in range(1,len(arr)):
#         if arr[i] != arr[i-1]:
#             arr[a] = arr[i]
#             a += 1
#     return a

# arr = [2, 5, 0, 6, 7, 0, 9, 8, 4, 2, 4, 0]
# new_length = remove_duplicate(arr)
# print("Array without duplicates:", arr[:new_length])

def remove_continuous_duplicate(arr):
    

    k =1
    for i in range(1,len(arr)):
        if arr[i]!= arr[i-1]:
            arr[k]= arr[i]
            k+=1
    return k

arr =[5,8,7,5,5,7,7,6,5,8,7,9]
a = remove_continuous_duplicate(arr)
print(arr[:a])

