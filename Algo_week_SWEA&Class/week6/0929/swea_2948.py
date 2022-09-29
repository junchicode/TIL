T = int(input())
for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    fst = set(list(input().split()))
    sec = set(list(input().split()))
    res = len(fst&sec)
    print(fst|sec)

    print(f'#{tc} {res}')