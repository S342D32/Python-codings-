def second_large(arr):
  large=sec_large =float("-inf")
  n= len(arr)
  for i in range(0,n):
    if arr[i] > large:
      sec_large= large
      large = arr[i]
    elif arr[i] > sec_large and arr[i] != large:
      sec_large= arr[i]
  return sec_large

arr = [2,43,6,7,4]
print(second_large(arr))


