# KADANE Algorithm
def max_subarray_sum(arr):
    max_global = arr[0]
    max_current = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global

# Example usage:
arr = [3,4,1,2,5,6]
print(max_subarray_sum(arr))  # Output: 21

