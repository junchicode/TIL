stk = []
tg = "(((())))"
newl = []
for t in tg:
    if t == "(":
        stk.append(t)
    elif t == ")":
        newl.append(stk.pop())
print(stk, newl)