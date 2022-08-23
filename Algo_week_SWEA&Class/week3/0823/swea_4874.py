T = int(input())
for tc in range(1, T+1):
    lst = list(map(str, input().split()))
    Stack = []    
    for i in range(len(lst)):
        if lst[i].isdigit():            
            Stack.append(lst[i])        
        else:            
            if lst[i] == '.':
                if len(Stack) == 1:                    
                    print('#{}'.format(tc),end=' ')
                    print(*Stack)                    
                    break                
                else:                    
                    print('#{}'.format(tc), end=' ')                    
                    print('error')                    
                    break            
            if len(Stack) > 1:                
                num1, num2 = int(Stack.pop()), int(Stack.pop())                
                if lst[i] == '+': Stack.append(num2 + num1)                
                if lst[i] == '-': Stack.append(num2 - num1)                
                if lst[i] == '*': Stack.append(num2 * num1)                
                if lst[i] == '/': Stack.append(num2 // num1)            
            else:                
                print('#{}'.format(tc), end=' ')                
                print('error')                
                break
