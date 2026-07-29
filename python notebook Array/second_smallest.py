def second_smallest(arr):
  n = len(arr)
  
  small = sec_small = float('inf')
  
  for num in arr:
    if num < small:
      sec_small= small
      small = num
    elif small<num<sec_small:
      sec_small = num
  


    
  return sec_small if sec_small != float('inf') else None


arr=[2,5,6,2,1,9,0,8]
print(second_smallest(arr))
