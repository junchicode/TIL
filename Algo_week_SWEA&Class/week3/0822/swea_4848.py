T = int(input())
for tc in range(1, T+1):
    string = input()

    stk = []
    for st in string:
        if len(stk) == 0 or stk[-1] != st:
            stk.append(st)
        else:
            stk.pop()
    print(f"#{tc} {len(stk)}")
        