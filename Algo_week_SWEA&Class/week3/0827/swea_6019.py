T = int(input())
for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())
    res = (d/(a+b))*f
    res = format(res, ".10f")
    print(f"#{tc} {res}")