def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr =list(map(int,input("Enter numbers separated by spaces:").split()))
reverse_array(arr)
print("Reversed Array:", arr)
