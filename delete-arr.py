arr = list(map(int,input("enter an array:").split()))
val = int(input("enter no:"))
def delete(arr,val):
        k=0
        for i in range(len(arr)):
                if arr[i]!=val:
                        arr[k]=arr[i]
                        k+=1
        return k
k = delete(arr,val)
print(arr[:k])
        