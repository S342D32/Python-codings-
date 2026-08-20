
nums =[3,4,5,6,7]
result=[]

def all_sequence(index,subset):
  if index >= len(nums):
    result.append(subset.copy())
    return
  subset.append(nums[index])
  all_sequence(index+1,subset)
  subset.pop()
  all_sequence(index+1,subset)
  return result

print(all_sequence(0,[]))

# TC = O(2^n)
# SC = O(n)