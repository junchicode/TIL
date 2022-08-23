def prefix(tg):
    res = []
    stk = []
    prio = {"+": 1, "*":2}
    for t in tg:
        if t not in "+*":
            res.append(t)
        else:
            while stk and prio[stk[-1]] >= prio[t]:
                res.append(stk.pop())
            stk.append(t)

    while len(stk) != 0:
        res.append(stk.pop())
            
    return "".join(res)

def calc(tg):
    stk = []
    for t in tg:
        if t.isdigit():
            stk.append(t)
        elif stk and t in "*+":
            first = int(stk.pop())
            sec = int(stk.pop())
            if t == "*":
                firstsec = first * sec
            
            elif t == "+":
                firstsec = first + sec
            
            stk.append(firstsec)
    return stk[0]

T=10
for tc in range(1, T+1):
    length = int(input())
    tg = input()
    print(f"#{tc} {calc(prefix(tg))}")

