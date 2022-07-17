import textwrap

t = int(input())
for i in range(t):
    word = []
    n = int(input())
    for j in range(n):
        a,b = input().split()
        for k in range(int(b)):
            word.append(a)
    wordres = "".join(word)
    print('#{}'.format(i+1))
    res = textwrap.fill(wordres, width = 10)
    print(res)
    



      
    
    