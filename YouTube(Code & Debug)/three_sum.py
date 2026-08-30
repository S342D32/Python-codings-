def three_sum_optimal(arr,tar):
  arr.sort()
  n = len(arr)
  result=[]
  for i in range(n):
    # Skip duplicate first element
    if i > 0 and arr[i]== arr[i-1]:
      continue
    j = i+1
    k= n-1
    while j < k:
      total_sum = arr[i]+ arr[j]+ arr[k]
      if total_sum < tar:
        j+=1
      elif total_sum >tar:
        k-=1
      else:
        result.append([arr[i],arr[j],arr[k]])
        j+=1
        k-=1
        # Skip duplicate 2nd element
        while j < k and arr[j] ==arr[j-1]:
          j+=1
          # Skip duplicate 3rd element
        while j < k and arr[k] == arr[k+1]:
          k-=1
  return result

print(three_sum_optimal([1,3,4,5,6,2,7,8],10))

# TC= O(nlogn) + O(n^2) = O(n^2)
# SC = O(no of triplates) =O(1)