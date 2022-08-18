# 조금 더 단순하게 구현한 버전

text = "This is a book~!"  # 전체 텍스트
pattern = "is"  # 찾을 패턴

def BruteForce(pattern, text):

    # text를 처음부터 끝까지 순회하면서 (단, pattern의 길이에 맞게)
    for idx in range(len(text) - len(pattern) + 1):
        # pattern을 처음부터 끝까지 순회하면서
        for j in range(len(pattern)):
            # 다르면 break
            if text[idx+j] != pattern[j]:
                break
        # 다른게 없다면 정답이므로, idx(시작점) return
        else:
            return idx
    else:
        return -1

print(BruteForce(pattern, text))