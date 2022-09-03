
N, M = map(int, input().split())
arr = {input() for _ in range(N)}
arrdict = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
for i in arr:
    if '1' in i:
        tg = i
        break
rev = tg[::-1]

newarr = ''
cnt = 0
for i in range(M):
    if rev[i] == '1':
        while cnt != 56:
            cnt += 1
            newarr+=rev[i]
            i += 1
        break
originarr = newarr[::-1]


res = [0]
for i in range(0, 56, 7):
    
    res.append(arrdict[originarr[i:i+7]])
a = []
b = []
for i in range(1,9):
    if i%2 == 1:
        a.append(res[i])
    elif i%2 == 0:
        b.append(res[i])

total = sum(a)*3 + sum(b)
print(total)
if total%10 == 0:
    print('good')
else:
    print('bad')
        

    
    

    
    


            
            
        

