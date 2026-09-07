def subset_sum(index,arr,subset,result):
  n =len(arr)
  if index == n:
    result.append(subset.copy())
  if index > n:
    return
  subset.append(arr[index]) 
  subset_sum(index+1,arr,subset,result)
  subset.pop()
  return subset_sum

print(subset_sum(0,[2,3,4,5,6],[],[]))



