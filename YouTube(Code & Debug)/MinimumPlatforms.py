# def Min_platform(arr, dep):
#     n = len(arr)
#     ans = 0

#     for i in range(n):
#         count = 0

#         for j in range(n):
#             # Is train j present when train i arrives?
#             if arr[j] <= arr[i] <= dep[j]:
#                 count += 1

#         ans = max(ans, count)

#     return ans



# TC=O(N^2)
# SC=O(1)

# ------------------------------------
# Optimal
# ----------------------------------
def Min_platform(arr,dep):
  arr.sort()
  dep.sort()

  ans =1
  count =1
  i =1
  j = 0
  while i < len(arr) and j < len(dep):
    if arr[i] <= dep[j]:
      count +=1
      i+=1
    else:
      count -=1
      j +=1
    ans = max(ans,count)
  return ans

# TC=O(NlogN)
# SC=O(1)



arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(Min_platform(arr, dep))