def to1array(a):                                               # 타겟 네모를 1차원 배열로 바꿔주기위한 함수
    newa = []  
    for i in a:
        for j in i:
            newa.append(j)
    return newa
T = int(input())                                               # 입력구간
for tc in range(1, T+1):                                       # 입력구간
    N = int(input())
    sqr = [list(map(int, input().split())) for _ in range(N)]
    tgsqr = [list(map(int, input().split())) for _ in range(3)]
    tgsqrarr = to1array(tgsqr)                                  # 타겟을 1차원 배열로
    
    cnt = 0                                                     # 결과값   
    for i in range(N-3+1):
        for j in range(N-3+1):
            sqrcase = []                                        # 검사하는 네모
            for ic in range(3):
                for jc in range(3):
                    sqrcase.append(sqr[i + ic][j + jc])         # sqrcase에 원소하나씩 추가
            
            if tgsqrarr == sqrcase:                             # 타겟과 sqrcase가 같다면
                cnt += 1                                        # 결과값을 늘려준다
            else:
                pass
            
    print(f"#{tc} {cnt}")
                
                