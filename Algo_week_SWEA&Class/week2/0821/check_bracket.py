def check(string):
    stk = []
    for i in string:
        if i == "(":
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                return -1
    if not stk:
        return 1
    else:
        return -1

string = "(((())))))"

print(check(string))
