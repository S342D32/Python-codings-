def two_sum(arr, key):
    arr.sort()  # Ensure the array is sorted
    left = 0
    right = len(arr) - 1
    pairs = []
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == key:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < key:
            left += 1
        else:
            right -= 1
    return pairs

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
key = int(input("Enter the key: "))

a = two_sum(arr, key)
print(a)
