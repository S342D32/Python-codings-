# Bruteforce
# ____________________________________
# def maxConsicutiveOnes(arr,k):
#   n = len(arr)
#   maxi=0
#   for i in range(0,n):
#     zeros = 0
#     for j in range(i,n):
#       if arr[j] ==0:
#         zeros += 1
#       if zeros>k:
#         break
#       maxi = max(maxi,j-i+1)
#   return maxi
# TC=O(N(N+1)/2) == O(N^2)
# SC=O(N)

# Better
# ______________________________


# def maxConsicutiveOnes(arr,k):
#   n = len(arr)
#   maxi =0
#   left =0
#   right =0
#   zeros=0
#   while right <n:
#     if arr[right] ==0:
#       zeros +=1
#     while zeros >k:
#       if arr[left] ==0:
#         zeros-=1
#       left +=1
#     if zeros <=k:
#       maxi = max(maxi,right-left+1)
#     right +=1
#   return maxi

# TC =O(2N)
# SC=O(1)

# Optimal
# _____________________________
def maxConsicutiveOnes(arr,k):
  n = len(arr)
  maxi =0
  left =0
  right =0
  zeros=0
  while right <n:
    if arr[right] ==0:
      zeros +=1
    if zeros >k:
      if arr[left] ==0:
        zeros-=1
      left +=1
    if zeros <=k:
      maxi = max(maxi,right-left+1)
    right +=1
  return maxi
# TC =O(2N)
# SC=O(1)
arr= [1,1,1,0,0,1,0,1,0,0]
print(maxConsicutiveOnes(arr,2))