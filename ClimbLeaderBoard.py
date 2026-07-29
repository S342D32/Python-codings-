
def climbingLeaderboard(ranked, player):
    # Write your code here
    unique_rank = list(dict.fromkeys(ranked))
    n = len(unique_rank)
    i = n-1
    result =[]
    
    for score in player:
        while i >= 0 and score >= unique_rank[i]:
            i-=1
        result.append(i+2)
    return result
            
ranked =[100,70,70,50,30,10]
player =[5,5,10,25,40]
print(climbingLeaderboard(ranked, player))

