def merge_inplace(arr1, arr2):
    m, n = len(arr1), len(arr2)
    i, j, k = m - 1, n - 1, m + n - 1
    arr1.extend([0] * n)  # Extend arr1 to hold arr2 elements
    
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    return arr1

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge_inplace(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
