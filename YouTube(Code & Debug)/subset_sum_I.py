def subset_sum(index,arr,subset,result):
  n =len(arr)
  if index == n:
     result.append(subset.copy())
     return

  subset.append(arr[index]) 
  subset_sum(index+1,arr,subset,result)
  subset.pop()
  subset_sum(index+1,arr,subset,result)
  return result

print(subset_sum(0,[1,2,3],[],[]))



