T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = ["0"]*N
    for i in range(Q):
        L,R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = str(i+1)

    box = " ".join(box)
    print(f"#{tc} {box}")


    