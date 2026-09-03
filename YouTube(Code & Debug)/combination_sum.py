def solve(index,arr,target,total,result):
  if index >=len(arr):
    result.append(arr[index])
    return
  if total == target:
    return 
  
