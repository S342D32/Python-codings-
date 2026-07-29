#smallest element in array
def small(arr):
    smallest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest
            

arr =list(map(int,input("Enter numbers separated by spaces:").split()))
b = small(arr)
print(b)


def sec_largest(arr):
    second = largest =arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            second = largest

            largest = arr[i]
        elif arr[i] > second and arr[i] != largest:
            second = arr[i]

    return second
            

arr =[1,4,3,5,6,5]
b = sec_largest(arr)
print(b)

