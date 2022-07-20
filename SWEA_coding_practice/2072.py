n = int(input())
cnt = 0
for i in range(n):
    sum = 0
    nl = list(map(int, input().split()))
    for j in nl:
        if j%2 == 1:
            sum += j
        else:
            pass
    cnt += 1
    print(f"#{cnt} {sum}")
    