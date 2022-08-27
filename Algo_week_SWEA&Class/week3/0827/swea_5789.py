T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0]*(N+1)
    for i in range(1, Q+1):
        s, e = map(int, input().split())
        for j in range(s, e+1):
            box[j] = i
    box.pop(0)
    
    print(f"#{tc}", *box)
