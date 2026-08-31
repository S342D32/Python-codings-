def four_sum(arr,tar):
  n = len(arr)
  arr.sort()
  result =[]
  for i in range(0,n):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    for j in range(i+1,n):
      if j>i+1 and arr[j] == arr[j-1]:
        continue
      k=j+1
      l=n-1
      while k < l:
        total_sum = arr[i]+arr[j]+arr[k]+arr[l]
        if total_sum<tar:
          k+=1
        elif total_sum > tar:
          l-=1
        else:
          result.append([arr[i],arr[j],arr[k],arr[l]])
          k+=1
          l-=1
          while k<l and arr[k] == arr[k-1]:
            k+=1
          while k<l and arr[l] == arr[l+1]:
            l-=1
  return result


print(four_sum([1,0,-1,0,-2,2], 0))

# TC = O(N^3)
# SC = O(1)
      