def JumpGameGreedy(arr):
  max_index =0
  n = len(arr)
  for i in range(0,n):
    if i > max_index:
      return  False
    max_index = max(max_index,i+arr[i])
  return True

arr =[2,3,4,0,5,6]
print(JumpGameGreedy(arr))
