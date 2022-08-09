'''
k = 한번 충전으로 최대 이동 가능한 정류장수
N = 종점
M = 충전기 정류장 번호
/n
M 에대한 충전기 위치
'''
T = int(input())
for tc in range(1, T + 1):
    K,N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    charger = [0]*N # 리스트 먼저 뽑아준다
    for i in arr:
        charger[i] = 1 # 

    start = 0
    maxp = 0 + K
    cnt = 0

    while maxp < N: 
        if start == maxp:
            cnt = 0
            break
        if charger[maxp] == 1:
            start = maxp
            maxp = start + K
            cnt += 1
        elif charger[maxp] == 0:
            maxp -= 1

    print(f"#{tc} {cnt}")
        

        
    
    