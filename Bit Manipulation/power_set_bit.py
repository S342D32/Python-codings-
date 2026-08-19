arr = [2,3,4,7]

def power_set(arr):
  n = len(arr)
  result=[]
  total_subsets = 1<<n
  for num in range(0,total_subsets):
    lst =[]
    for i in range(0,n):
      if num & (1<<i) !=0:
        lst.append(arr[i])
    result.append(lst)
  return result

print(power_set(arr))
