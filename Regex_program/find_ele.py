n = int(input("Enter the number of elements:"))

arr = list(map(int, input("Enter an array:").split()))

# Check if the array has at least two elements
if len(arr) < 2:
    print("Array must contain at least two elements")
else:
    left = 0
    right = n - 1
    if arr[0] != arr[1]:
        print(arr[0])
    elif arr[n - 1] != arr[n - 2]:
        print(arr[n - 1])
    else:
        while left <= right:
            mid = left + (right - left) // 2
            pre = mid - 1
            nxt = mid + 1

            if (mid > 0 and arr[pre] != arr[mid]) and (mid < n - 1 and arr[nxt] != arr[mid]):
                print(arr[mid])
                break

            elif mid % 2 == 0:
                if arr[pre] == arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[pre] == arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
