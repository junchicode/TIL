s = "abcde"
ls = list(s)

for idx in range(len(s)//2): #c 처음부터 중간까지
    ls[idx], ls[-idx-1] = ls[-idx-1], ls[idx]
    
result = ''.join(ls)
print(result)  