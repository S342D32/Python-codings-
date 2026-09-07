# brute force
def subset_sum(index,arr,subset,result):
  n =len(arr)
  if index == n:
    result.append(subset.copy())
  if index <n:
    return
  for i in range(index,n):
      subset.append(arr[i]) 
      subset_sum(i+1,arr,subset,result)
      subset.pop()
  return subset_sum

print(subset_sum)



