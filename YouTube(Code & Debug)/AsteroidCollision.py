def asteroidCollision(arr):
  stack=[]
  n = len(arr)
  for i in range(0,n):
    if arr[i] > 0:
      stack.append(arr[i])
    else:
      while stack and stack[-1] >0 and stack[-1] < abs(arr[i]):
        stack.pop()
      if stack and stack[-1] == abs(arr[i]):
        stack.pop()
      elif len(stack)==0 or stack[-1]<0:

        stack.append(arr[i])
  return stack

arr = [4,7,1,1,2,-3,-7,17,15,-18,-19]
print(asteroidCollision(arr))


# TC:O(2N) bcause we iterate and also pop
# SC:O(N)