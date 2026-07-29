def largest_consecutive_subarray(arr):
    n = len(arr)
    max_len = 0
    for i in range(n - 1):
        min_val = arr[i]
        max_val = arr[i]
        
        for j in range(i + 1, n):
            min_val = min(min_val, arr[j])
            max_val = max(max_val, arr[j])
            
            if max_val - min_val == j - i:
                max_len = max(max_len, j - i + 1)
    
    return max_len

arr = [10, 12, 11, 14, 13]
print(largest_consecutive_subarray(arr))  # Output: 5
