def MaxPointFromCards(arr,k):
  n = len(arr)
  left_sum =0
  right_sum =0
  if n ==k:
    return sum(arr)
  for i in range(0,k):
    left_sum+=arr[i]
  maxi = left_sum
  right_ind = n-1
  for i in range(k-1,-1,-1):
    left_sum-=arr[i]
    right_sum+=arr[right_ind]
    right_ind-=1
    maxi = max(maxi,left_sum+right_sum)
  return maxi

arr =[1,2,3,4,5,6,2,5]
print(MaxPointFromCards(arr,3))
