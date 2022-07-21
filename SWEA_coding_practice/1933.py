n = int(input())

def divd(a):
    nl = []
    for i in range(1, n + 1):
        if n % i == 0:
            nl.append(i)
            if i > n//2:
                return nl
                
    
res = divd(n)
for i in res:
    print(i, end = ' ')
        