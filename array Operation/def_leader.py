def leader(arr):
    leader =[]
    max_from_right = arr[-1]
    leader.append(max_from_right)
    for i in range(len(arr)-1,-1,-1):
        leader.append(arr[i])
        max_from_right = arr[i]
    return leader

arr =[2,3,4,7,5,9,2,4]
a = leader(arr)
print(a)
        

        