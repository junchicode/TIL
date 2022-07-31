l = [list(input().split()) for _ in range(3)]

for i in range(3-2+1):
    for j in range(3-2+1):
        let = ""
        for a in range(2):
            for b in range(2):
                let += l[i+a][j+b]
        print(let)

