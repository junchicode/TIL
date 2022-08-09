def MinVal(A):
    Temp = 0
    for i in A :
        if Temp == 0 or i < Temp :
            Temp = i
    return Temp

def MaxVal(A):
    Temp = 0
    for i in A :
        if Temp == 0 or i > Temp :
            Temp = i
    return Temp
    

T = 11
for tc in range(1, T):

    dump = int(input())
    arr = list(map(int, input().split()))

    for i in range(dump):
        if MaxVal(arr) - MinVal(arr) == 1 or 0:
            break
        else:
            arr[arr.index(MinVal(arr))]+=1
            arr[arr.index(MaxVal(arr))]-=1
        
    print(f"#{tc} {MaxVal(arr)-MinVal(arr)}")


    

        
    