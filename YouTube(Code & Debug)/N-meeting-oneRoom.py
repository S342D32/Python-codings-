class Meetings:
  def __init__(self,start,end,pos):
    self.start = start
    self.end = end
    self.pos = pos

def NmeetingOneRoom(start,end):
    n = len(start)
    meet = [Meetings(start[i],end[i],i+1) for i in range(n)]
    meet.sort(key = lambda x:(x.end,x.start))
    result =[]
    if n ==0:
      return result
    lastTime = meet[0].end
    for i in range(1,n):
      if meet[i].start > lastTime:
        result.append(meet[i].pos)
        lastTime = meet[i].end
    return result

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
print(NmeetingOneRoom(start, end))
print("Count:", len(NmeetingOneRoom(start, end)))


# Time Complexity (TC)
# - Creating meeting objects: \(O(N)\)
# - Sorting meetings: \(O(N\log N)\)
# - Iterating through meetings: \(O(N)\)
# Therefore,
# O(N)+O(NlogN)+O(N)
# = O(Nlog N)

# SC =O(N)





    