# from collections import ChainMap
# clothes ={'shirts': 2, 'pants': 3, 'shoes': 4}
# electric ={ 'laptop': 5, 'phone': 6, 'tablet': 7}
# food ={ 'bread': 8, 'milk': 9, 'eggs': 10}
# inv = ChainMap(clothes,electric,food)


# inv['jeans' ] = 10
# print(inv)
# print(clothes)

# inv['kurta' ] = 10
# print(inv)
# print(clothes)


# _____________________________-
# from collections import Counter
# s ="missiccippiii"

# print(Counter(s))
# ________________________________
# from collections import namedtuple

# S = namedtuple('student',('name','age','stream','avg'))

# s1 = S('Alexa',23,'MCA',87)
# print(s1)
# __________________________________________

from collections import deque

dq = deque([12,21,43,5,43,21])
dq.append(34)
dq.appendleft(88)
print(dq)