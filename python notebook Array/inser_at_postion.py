arr = list(map(int,input("Enter array elements:").split()))
pos = int(input("Enter the position to add:"))
n = int(input("Enter a no:"))

def insert_element(arr,pos,n):
  r=len(arr)
  arr.append(0)
  
  for i in range(r,pos,-1):
      arr[i]=arr[i-1]
  arr[pos]=n
  return arr

print(insert_element(arr,pos,n))
