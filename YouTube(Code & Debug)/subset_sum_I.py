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



# Time Complexity: O(2ⁿ × n)

# Why?

# There are 2 choices for each element: include or exclude.

# With n elements, the recursion generates 2ⁿ subsets.

# For every subset, subset.copy() takes up to O(n) time.
# SC=O(N)