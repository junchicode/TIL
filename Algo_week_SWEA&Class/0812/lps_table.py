def lps_table(p):
    lps = [0]*len(p)
    # lps 만들기위한 prefix의 인덱스
    j = 0
    for i in range(1, len(p)):
        # prefix의 idx위치에 있는 char과 같으면 lps에 숫자 증가
        if p[i] == p[j]:
            lps[i] = j + 1
            j += 1
        
        else:
            j = 0
            if p[i] == p[j]:
                lps[i] = j-1
                j += 1
        
    return lps

p = 'abcdabcef'
print(lps_table(p))
        