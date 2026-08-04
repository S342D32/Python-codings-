def reverse(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1, right - 1)

arr = [2, 3, 4, 5, 6, 7]
left = 0
right = len(arr) - 1

reverse(arr, left, right)
print(arr)