def subset_sum(index,total,arr,result):
  if index >= len(arr):
     result.append(total)
     return

  sum =total+arr[index] 
  subset_sum(index+1,sum,arr,result)
  sum = total
  subset_sum(index+1,sum,arr,result)
  return result

print(subset_sum(0,0,[1,2,3],[]))



# Time Complexity: O(2ⁿ × n)

# Why?

# There are 2 choices for each element: include or exclude.

# With n elements, the recursion generates 2ⁿ subsets.

# For every subset, subset.copy() takes up to O(n) time.
# SC=O(N)