arr = [1,2,4,6,3,8,6,9]



def count(arr):
    x =[]
    hash_map={}
    for num in arr:
      hash_map[num] = hash_map.get(num,0) +1
    for key in hash_map:
      if hash_map[key] ==1:
         x.append(key)
    return x        
print(count(arr))