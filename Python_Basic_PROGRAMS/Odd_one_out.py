def find_odd_occurrence(arr):
    left, right = 0, len(arr) - 1

    if arr[0] != arr[1]:
        return arr[0]
    elif arr[right] != arr[right - 1]:
        return arr[right]

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            left = mid + 1
        else:
            right = mid - 1

# Example usage
r = int(input("Enter a number: "))


n = list(map(int, input("Enter nums: ").split()))
print(find_odd_occurrence(n))
