arr =list(map(int,input("Enter numbers separated by spaces:").split()))
target=int(input("Enter the no."))


def search(arr,target):
    left=0
    right= len(arr)-1
    while left<=right:
        mid =(left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left =mid+1
        else:
            right = mid-1
    return left
print(search(arr,target))



