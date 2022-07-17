
def multiply(l):
    ans = 1
    for i in l:
        ans = ans*i
    
    return ans
        

T = int(input())
dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for tc in range(T):
    n = 9
    doublearr = [list(map(int, input().split())) for _ in range(n)] 
    sqr = []
    col = []
    for i in range(3):
        for j in range(3):
            sqr.append(doublearr[i][j])

    for i in range(n):
        col.append(doublearr[i][0])
        
    for i in col:
        if i in dict:
            dict[i] += 1
    
    for i in sqr:
        if i in dict:
            dict[i] += 1
    
    for i in doublearr[0]:
        if i in dict:
            dict[i] += 1
            
    dicset = []
    for i in range(1, n+1):
        dicset.append(dict.get(i))
        
    dicset = set(dicset)
    
    if len(dicset) > 1:
        print("#{} {}".format(tc+1, 0))
    else: print("#{} {}".format(tc+1, 1))
        
        
    
            
    