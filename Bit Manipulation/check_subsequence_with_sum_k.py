nums=[1,3,5,6,7,8]
k =9
result=[]
def check_subsequence_sum_k(index,total,subset):
  if total == k:
    result.append(subset.copy())
    return True
  elif total >k:
    return False
  if index >= len(nums):
    return False
  subset.append(nums[index])
  sum = total + nums[index]
  pick=check_subsequence_sum_k(index+1,sum,subset)
  if pick == True:
    return True
  e= subset.pop()
  sum = total
  not_pick=check_subsequence_sum_k(index+1,sum,subset)
  return not_pick

print(check_subsequence_sum_k(0,0,[]))


# TC=O(2^n)
# SC = O(n)

