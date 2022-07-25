from regex import D


def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    maxi = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > maxi:
            maxi = scores[i]
        else:
            pass
    return maxi
        
        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
    