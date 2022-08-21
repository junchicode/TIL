N = int(input())
a,b,c,d,e = 0,0,0,0,0
while True:
    if N == 1 or N == 0:
        break
    if N % 2 == 0:
        N = N // 2
        a += 1
    elif N % 3 == 0:
        N = N // 3
        b += 1
    elif  N % 5 == 0:
        N = N // 5
        c += 1
    elif N % 7 ==0 :
        N = N // 7
        d += 1
    elif N % 11 == 0:
        N= N // 11
        e += 1
print(a,b,c,d,e)

        
