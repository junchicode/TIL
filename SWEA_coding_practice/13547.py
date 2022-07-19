T = int(input())

for i in range(1,T+1):
    fight = input()
    cnto = 0
    cntx = 0
    for j in fight:
        if j == "o":
            cnto += 1
        else:
            cntx += 1
    rest = 15 - len(fight)
    res = rest + cnto    
    
    if res >= 8:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")
        