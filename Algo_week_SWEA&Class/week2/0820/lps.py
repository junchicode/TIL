# LPS 배열
def getLpsArray (target):
    lpsArray = [0]

    i = 1
    j = 0

    while(i < len(target)):
        
        if(target[i] == target[j]): # 같다면 j 를 한 칸 앞( -> )으로 보내줍니다.
            j += 1
            i += 1
            lpsArray.append(j)
        else: # 같지 않다면 현재 문자와 일치하는 문자가 나타나거나 j 가 0번째 칸으로 갈 때까지 이동합니다.
            if(j > 0):
                j -= 1
            elif(j == 0):
                lpsArray.append(0)
                i += 1

    return lpsArray

arr = "abcdabc"
print(getLpsArray(arr))