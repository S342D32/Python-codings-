# BruteForce
# --------------------------
# def FruitInBasket(fruits):
#   n = len(fruits)
#   max_len=0
#   for i in range(0,n):
#     basket = set()
#     for j in range(i,n):
#       basket.add(fruits[j])
#       if len(basket) >2:
#         break
#       max_len = max(max_len,j-i+1)
#   return max_len
# TC= O(N^2)
# SC= O(1)

# Better
# ------------------------
def FruitInBasket(fruits):
  n = len(fruits)
  max_len=0
  basket=dict()
  L=0
  R=0
  while R <n:
    basket[fruits[R]] = basket.get(fruits[R],0)+1
    while len(basket) >2:
      basket[fruits[L]] -= 1
      if basket[fruits[L]] ==0:
        del basket[fruits[L]]
      L+=1
    if len(basket) <=2:
      max_len  = max(max_len,R-L+1)
    R+=1
  return max_len



print(FruitInBasket([1,3,3,1,1,2,3,1,1,3,2]))
