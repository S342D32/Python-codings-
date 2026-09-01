def ceil_floor(arr, tar):
    arr.sort()

    floor_val = None
    ceil_val = None

    for num in arr:
        if num <= tar:
            floor_val = num

        if num >= tar and ceil_val is None:
            ceil_val = num

    return floor_val, ceil_val

print(ceil_floor([2,3,4,5,7,3], 4))
# TC=O(nlogn)
# SC=O(1)