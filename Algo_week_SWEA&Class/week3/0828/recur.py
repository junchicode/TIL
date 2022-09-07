def recur(n):
    if n < 2:
        return  n
    else:
        return recur(n-1) + recur(n-2)

print(recur(20))