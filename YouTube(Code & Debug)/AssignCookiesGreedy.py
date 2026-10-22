def AssignCookiesGreedy(G,S):
  n = len(G)
  m = len(S)
  left =0
  right =0
  G.sort()
  S.sort()
  count=0
  while left <n and right <n:
    if G[left] <= S[right]:
      count+=1
      left +=1
    right+=1
  return count

# TC=O(NlogN) + O(MlogM) + O(M)
# SC =O(1)
G=[2,3,5,1,5,9,2,4]
S=[9,7,8,4,5,2,8,1]
print(AssignCookiesGreedy(G,S))

