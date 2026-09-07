def combination_sum(index,total,result,subset,arr,target):
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



print(combination_sum(0,0,[],[],[2,3,4,5,6,7],7))

# TC->O(2^n * n)
# SC->O(N)