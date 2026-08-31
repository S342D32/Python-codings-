def binary_recursion(arr,tar,low,high):
  arr.sort()
  while low<=high:
    mid = (low+high)//2
    if arr[mid] < tar:
      return binary_recursion(arr,tar,mid+1,high)
    elif arr[mid] > tar:
      return binary_recursion(arr,tar,low,mid-1)
    else:
      return mid
  return -1

arr=[2,4,5,6,3,7]
n = len(arr)
low = 0
high = n-1
print(binary_recursion(arr,3,low,high))

# def binary(arr,tar):
#   arr.sort()
#   n = len(arr)
#   low = 0
#   high = n-1
#   while low<=high:
#     mid = (low+high)//2
#     if arr[mid] < tar:
#       low=mid+1
#     elif arr[mid] > tar:
#       high=mid-1
#     else:
#       return mid
#   return -1

# print(binary([2,4,5,6,3,7],3))



# TC=O(logn)
# SC=O(1)