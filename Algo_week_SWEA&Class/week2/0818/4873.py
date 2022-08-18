T = int(input())
for tc in range(1, T+1):
    tg = input()
    stk = []
    for letter in tg:
        if stk and letter == stk[-1]:
            stk.pop()
        else:
            stk.append(letter)

print(f'#{tc} {len(stk)}')
    
    
