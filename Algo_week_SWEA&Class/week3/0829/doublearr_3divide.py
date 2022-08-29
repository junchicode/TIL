'''
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 2 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5
'''

for tc in range(int(input())):
    n, min_lim, max_lim = map(int, input().split())
    scores = list(map(int, input().split()))
    score_list = [0] * 101
    result = n
    # 우선, 구간을 슬라이스 할 수 있는 방법
    # 최대값과 최소값을 사이로 슬라이싱을 진행한다
    # 점수 구간을 하나 만들고, 그 사이의 반을 나눠버린다
    # 그 반 인원수들 간의 차이를 비교, result에 저장
    # 단, high와 low구간안을 만족해야 한다.
    for i in scores:
        score_list[i] += 1
    print(score_list)
    for i in range(1,100):
        for j in range(i+1, 101):
            low = sum(score_list[:i])
            middle = sum(score_list[i:j])
            high = sum(score_list[j:])
            
            if min_lim <= low <= max_lim and min_lim <= middle <= max_lim and min_lim <= high <= max_lim:
                outcome = max(low, middle, high) - min(low, middle, high)
                
                if outcome < result:
                    result = outcome

    '''if result == n:
        result = -1'''
    '''print(f'#{tc+1} {result}')'''