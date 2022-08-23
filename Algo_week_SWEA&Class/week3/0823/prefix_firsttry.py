tg = "3*(5+2)-9"
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

print(prefix(tg))
        