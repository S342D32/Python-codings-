def first_last(arr, tar):
    n = len(arr)
    first = -1
    last = -1

    for i in range(n):
        if arr[i] == tar:
            if first == -1:   # First occurrence
                first = i
            last = i           # Keep updating last occurrence

    return first, last

print(first_last([2,3,6,4,5,6], 6))