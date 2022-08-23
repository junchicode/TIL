tg = "(A+B)*(C-D)"
stk = []
res = []
prior = {"*":3, "/": 3, "+":2, "-":2, "(": 1}

for t in tg:
    if t == "(":
        stk.append(t)
    elif t.isdigit():
        res.append(t)
    elif t == ")":
        while stk[-1] != '(':
            res.append(stk.pop())
        stk.pop()
    else:
        while stk and 
    
        
        
