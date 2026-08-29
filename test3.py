def three_sum_b(arr,tar):
  my_set = set()
  n=len(arr)
  for i in range(0,n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        if arr[i]+ arr[j]+ arr[k] == tar:
          temp =arr[i],arr[j],arr[k]
          my_set.add(temp)
  return [list(ans) for ans in my_set]


print(three_sum_brute([1,2,3,4,5,6,7,8],10))