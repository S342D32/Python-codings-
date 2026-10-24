  
  if total ==target:
    return result.append(subset.copy())
  if total > target:
    return
  for i in range(index,len(arr)):
    if i > index and arr[i] == arr[i-1]:
      continue
    subset.append(arr[i])
    combination_sum(i+1,total+ arr[i],result,subset,arr,target)
    subset.pop()
  return result
