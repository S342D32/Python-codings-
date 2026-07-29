def sort_binary_array(arr):
    zero_count = arr.count(0)
    return [0] * zero_count + [1] * (len(arr) - zero_count)

arr = [1, 0, 1, 0, 1, 0, 0, 1]
print(sort_binary_array(arr))  # Output: [0, 0, 0, 0, 1, 1, 1, 1]
