def frequency(arr):
  freq={}
  for i in range(len(arr)):
    freq[arr[i]] = freq.get(arr[i],0) +1
  return freq

arr= [9,4,5,7,3,2,3,5,4,3]
print(frequency(arr))