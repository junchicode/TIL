# 텍스트안 타겟의 인덱스를 구해보자

text = "He actually is not a dumb"
target = "is"

lenoftext = len(text)
lenoftarg = len(target)

def brtfrcstr (text, target):
    lenoftext = len(text)
    lenoftarg = len(target)
    for idx in range(lenoftext - lenoftarg + 1):
        for tg in range(lenoftarg):
            if text[idx+tg] != target[tg]:
                break
        else:
            return f"{idx} to {idx + lenoftarg - 1} is range of idx where the target is placed in the text"
    else:
        return "The target not in the text"
print(brtfrcstr(text, target))
