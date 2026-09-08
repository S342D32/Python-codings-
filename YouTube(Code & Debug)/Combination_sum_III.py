def solve(index,total,subset,result,arr,target,k):
  if total == target and len(subset) ==k:
    result.append(subset.copy())
    return
  if total > target or len(subset)>k:
    return

  for i in range(index,len(arr)):
      sum = total + arr[i]
      subset.append(arr[i])
      solve(i + 1,sum,subset,result,arr,target,k)
      subset.pop()
  return result

print(solve(0,0,[],[],[2,3,4,5,6,7],7,2))


# Time Complexity (TC)

# Let: n = number of elements in arr

# k = size of each combination

# TC: O((nCk)×k)

# Reason:

# The algorithm explores all combinations of k elements from n elements.

# There are (
# k
# n
# 	​

# ) such combinations.

# Copying each valid subset (subset.copy()) takes O(k).

# Space Complexity (SC)

# Auxiliary Space: O(k) (recursion stack + current subset).

# Output Space: O((
# k
# n
# 	​

# )×k) (if storing all answers).