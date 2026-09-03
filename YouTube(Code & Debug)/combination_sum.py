def solve(index,total,subset,nums,target,result):
  if total == target:
    result.append(subset.copy())
    return
  elif total>target:
    return
  if index>=len(nums):
    return
  sum = total+nums[index]
  subset.append(nums[index])
  solve(index,sum,subset,nums,target,result)
  sum = total
  subset.pop()
  solve(index+1,sum,subset,nums,target,result)

def combination(nums,target):
  result=[]
  solve(0,0,[],nums,target,result)
  return result

print(combination([2,3,4,5,6],7))

# TC=O(2^N)
# SC= O(N)