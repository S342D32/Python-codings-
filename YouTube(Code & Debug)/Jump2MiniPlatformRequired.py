def JumpMiniPlatformRequired(arr,index,jump):
  last_index=arr[-1]
  if index > last_index:
    return jump
  min_jump = float('inf')
  for i in range(1,arr[i]+1):
    min_jump = min(min_jump,JumpMiniPlatformRequired(arr,index+i,jump+1))
  return min_jump

print
    