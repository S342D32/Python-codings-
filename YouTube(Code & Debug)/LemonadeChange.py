def LemonadeChange(arr):
  five =0
  ten = 0
  n = len(arr)
  for i in range(n):
    if arr[i] ==5:
      five +=1
    elif arr[i] ==10:
      if five >=1:
         five -=1
         ten +=1
      else:
        return False

    else:
      if five >=1 and ten >=1:
        five -=1
        ten-=1

      elif five >=3:
        five -=3
      else:
        return  False
      
  return True

print(LemonadeChange([5,5,5,20,50]))

# TC=O(N)
# SC=O(1)