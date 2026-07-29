def find_majority_element(arr):
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate if arr.count(candidate) > len(arr) // 2 else None

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(find_majority_element(arr))  # Output: 4
