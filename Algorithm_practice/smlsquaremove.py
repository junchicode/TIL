l = [list(input().split()) for _ in range(3)]
n = 2
'''col = ""'''
row = ""
for r in range(3):
    col = ""
    for c in range(3-n+1):       
        for di in range(n):
            col += l[r][c+di]
            row += l[c+di][r]
    print(col)
