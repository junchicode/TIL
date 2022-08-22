def sqrtotal(a):                                              # 총합을 반환하는 함수
    total = 0
    for i in a:
        total += i
    return total

def maxlist(a):                                               # 길이 2의 리스트에서 작은 값, 큰 값 순으로 바꿔주는 함수
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
    return a
T = int(input())                                              # 입력 구간           
for tc in range(1, T+1):
    N = int(input()) 
    tg = list(map(int, input().split()))
    sqr = [list(map(int, input().split())) for _ in range(N)] 
    newtg = [[tg[0],tg[2]], [tg[1],tg[3]]]                   # 1 1 3 4 처럼 받은 리스트에서 이렇게 뽑으면 범위 설정 가능               
    for i in range(2):
        newtg[i] = maxlist(newtg[i])                         # 작은 것부터 나열 [[1, 3], [1, 4]]

    tglist =[]                                               # 구하려는 크기 안에 있는 원소들을 1차원 배열로 생성
    for i in range(newtg[0][0], newtg[0][1]+1):
        for j in range(newtg[1][0], newtg[1][1]+1):
            tglist.append(sqr[i][j])
                
    sizeoftgsquare = len(tglist)                            # 길이
    totalofsqr = sqrtotal(tglist)                           # 총합
    average  = totalofsqr // sizeoftgsquare                 # 평균  
  
    res =0                                                  # 결과값 저장하는 공간
    for i in tglist:
        if i != average:                                    # 타겟값의 i가 평균이 아닐 때
            if i > average:                                 # i가 평균 보다 크면                                                           
                res += i - average                          # i에서 평균 빼준 값을 결과에 더해주고
            else:                                           # i가 평균보다 작으면               
                res += average - i                          # 평균에서 i빼준 값을 결과에 더해준다

        else:
            pass
    print(f"#{tc} {res}")

        
    

