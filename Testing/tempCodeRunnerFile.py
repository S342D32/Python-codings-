# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def two_sum(arr,target):
    seen ={}
    for i,num in enumerate(arr):
          need = target - num
          if need in seen:
              return [seen[need],i]
          seen[num]=i 
            
        
  
    


arr=[2,4,2,3]
target=7
print(two_sum(arr,target))
