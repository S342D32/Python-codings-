def rotate_by_k(arr,k):
  n = len(arr)
  rotation = k%n
  for i in range(0,rotation):
    e = arr.pop()
    arr.insert(0,e)

arr =[2,3,4,5,6]
k = 3
rotate_by_k(arr,k)
print(arr)


