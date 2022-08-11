T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]

def total(list):
    sum = 0
    for i in list:
        sum += i
    return sum

for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    cnt=0
    for i in range(1<<len(A)):
        lst=[] #
        for j in range(len(A)):
            if i&(1<<j):
                lst.append(A[j])
        if len(lst)==N and total(lst)==K:
            cnt+=1
    
    print(f"#{T} {cnt}")
            


    
            
        