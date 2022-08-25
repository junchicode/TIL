T = int(input())
for tc in range(1, T+1):    
    N, M = map(int, input().split())
    chz = list(map(int, input().split()))
    pizza = []
    for i in range(1, M+1):
        pizza.append([i,chz[i-1]])
    in_oven = pizza[0:N]
    remain = pizza[N:]

    while len(in_oven) > 1:
        a_pizza = in_oven.pop(0)
        a_pizza[1] //= 2
        if a_pizza[1] == 0:
            if remain:
                in_oven.append(remain.pop(0))
        
        else: # 0이면
            in_oven.append(a_pizza)

    print(f"#{tc} {in_oven[0][0]}")
    
        
        
