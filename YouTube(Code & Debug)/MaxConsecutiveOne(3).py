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

def 
arr= [1,1,1,0,0,1,0,1,0,0]
print(maxConsicutiveOnes(arr,2))