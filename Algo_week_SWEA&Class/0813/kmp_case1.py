def KMP(T, P):

    lps = pre_process(P)

    # i : text를 순회하는 index
    i = 0
    # j : pattern을 순회하는 index
    j = 0

    position = -1
    while i < len(T):
        # 같으면 이동
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            # 다른데 j가 0이 아니라면, i의 자리는 유지한 채 j만 이동하여 비교 시작
            if j != 0:
                j = lps[j - 1]
            # 다른데 j가 0이라면, i를 한칸만 이동하여 처음부터 진행하듯이 진행
            else:
                i += 1
        # j가 pattern을 다 순회하면 성공
        if j == len(P):
            position = i - j
            break

    return position


T = 'abcdabeeababcdabcef'
P = 'eaba'


position = KMP(T, P)
print(position)