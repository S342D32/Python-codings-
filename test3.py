def three_sum_best(arr,tar):
  result = set()
  n=len(arr)
  for i in range(0,n):
    seen= set()
    for j in range(i+1,n):
      third =  tar -(arr[i]+arr[j])
      if third in seen:
          temp =[arr[i],arr[j],third]
          temp.sort()
          result.add(tuple(temp))
      seen.add(arr[j])

  return [list(ans) for ans in result]


print(three_sum_best([1,2,3,4,5,6,7,8],10))

