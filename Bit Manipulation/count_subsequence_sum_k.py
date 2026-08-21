nums = [1,2,4,5,6,7]
k = 8

def backtrack(index,total):
  if total == k:
    return 1
  elif total > k:
    return 0
  if index >= len(nums):
    return 0
  sum = total + nums[index]
  pick = backtrack(index+1,sum)
  sum = total
  not_pick = backtrack(index+1,sum)
  return pick + not_pick


print(backtrack(0,0))

# TC=O(2^n)
# SC=O(n)
