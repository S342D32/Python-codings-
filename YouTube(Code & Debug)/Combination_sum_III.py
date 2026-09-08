def solve(index,total,subset,result,arr,target,k):
  if total == target and len(subset) ==k:
    result.append(subset.copy())
    return
  if total > target or len(subset)>k:
    return

  for i in range(index,len(arr)+1):
      sum = total + i
      subset.append(i)
      solve(i + 1,sum,subset,result,arr,target,k)
      subset.pop()
  return result

print(solve(0,0,[],[],[2,3,4,5,6,7],7,2))


# TC=O()