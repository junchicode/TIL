def prefix(tg):
    res = []
    stk = []
    prio = {"(": 1, "+":2, "-":2, "*":3, "/":3}
    for t in tg:
        if t == "(":
            stk.append(t)
        elif t == ")":
            while stk[-1] != "(":
                res.append(stk.pop())
            stk.pop()
        elif t.isdigit():
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
        elif stk and t in "*/+-":
            first = int(stk.pop())
            sec = int(stk.pop())
            if t == "*":
                firstsec = first * sec
            elif t == "/":
                firstsec = sec / first
            elif t == "+":
                firstsec = first + sec
            elif t == "-":
                firstsec = sec - first
            stk.append(firstsec)
    return stk[0]
T = 11
for tc in range(1, T):
    lenoftg = int(input())
    tg = input()
    print(f"#{tc} {calc(prefix(tg))}")

    
