tc = list(map(int, input().split()))
tclist = []
for i in range(len(tc)):
    if i == 0:
        tclist.append(tc[i])
    elif tc[i] != tc[i-1]:
        tclist.append(tc[i])
        
print(tclist)
    