def hash_list(m, n):
    hash = [0] * 11

    for i in m:
        hash[i] += 1

    for j in n:
        hash[j] += 1

    return hash

m = [1,2,3,4,5]
n = [6,7,8,9,10]

print(hash_list(m, n))