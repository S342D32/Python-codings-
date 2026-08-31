def binary(arr,tar):
  arr.sort()
  n = len(arr)
  low = 0
  high = n-1
  while low<=high:
    mid = (low+high)//2
    if arr[mid] < tar:
      low=mid+1
    elif arr[mid] > tar:
      high=mid-1
    else:
      return mid
  return -1

print(binary([2,4,5,6,3,7],3))



# TC=O(logn)
# SC=O(1)