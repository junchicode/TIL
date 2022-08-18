N = int(input())
a = 0
b = 0
c = 0
d = 0
e = 0
while True:
    if N % 2 == 0:
        N = N / 2
        a += 1
    elif N % 3 == 0:
        N = N / 3
        b += 1
    elif N % 5 == 0:
        N = N / 5
        c += 1
    elif N % 7 == 0:
        N = N / 7
        d += 1
    elif N % 11 == 0:
        N = N / 11
        e += 1
    else:
        break

print(a,b,c,d,e)
        