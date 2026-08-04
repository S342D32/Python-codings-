def merge_sort(arr):
  if len(arr)<1:
    return arr

  mid = len(arr)//2
  left_arr = arr[:mid]
  right_arr = arr[mid:]
  left = merge_sort(left_arr)
  right =  merge_sort(right_arr)
  return merge_sort(left,right)