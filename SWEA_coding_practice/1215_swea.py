t = 10
length = 8

def list_chunk(source_list, n):
    """
    리스트를 청크 단위로 잘라낸다.
    """
    return [source_list[i:i+n] for i in range(0, len(source_list), n)]

for i in range(t):
    n = int(input())
    tc = [list(input()) for _ in range(length)]
    col = ""
    row = ""
    for r in range(8):
        for c in range(8-n+1):
            
            for di in range(n):
                col += tc[r][c+di]
                row += tc[c+di][r]
                
    collist = list_chunk(col, n)
    rowlist = list_chunk(row, n)
    
    total = 0
    for cc in collist:
        if cc == cc[::-1]:
            total += 1
        else:
            pass
    
    for rr in rowlist:
        if rr == rr[::-1]:
            total += 1
        else:
            pass
    
    print(f"#{i+1} {total}")
        
                
                
                

   
    

                    
                        
                
                
                
    
    
            

                
    