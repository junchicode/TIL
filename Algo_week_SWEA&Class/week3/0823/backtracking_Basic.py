def recur_btrk(x):
    if 정답이라면:
        정답 출력 또는 저장 etc...
    else: 정답이 아니라면
        for 뻗을 수 있는 모든 자식 노드들에 대해:
            if 정답에 유망하다면:
                자식 노드로 이동
                recur_btrk(x+1)
                부모 노드로 이동