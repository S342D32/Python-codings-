def LongestSubstringWithoutRepeatChar(arr):
  n = len(arr)
  maxi=0
  for i in range(0,n):
    my_set =set()
    for j in range(i,n):
      if arr[j] in my_set:
        break
      maxi =(max(maxi,j-i+1))
      my_set.add(arr[j])
  return maxi

arr =['C','A','D','R','D','Y','A']
print(LongestSubstringWithoutRepeatChar(arr))


# TC: O(N^2)
# SC:O(N)