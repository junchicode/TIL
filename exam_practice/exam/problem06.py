# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
from hashlib import new


def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    newword = ''
    for i in word:
        toint = ord(i) + n
        if ord(i) > 64 and ord(i) < 91:
            if toint > 90:
                newword += chr(64+(toint - 90))
            else:
                newword += chr(toint)
        elif ord(i) > 96 and ord(i) < 122:
            if toint > 122:
                newword += chr(96+(toint - 122))
            else:
                newword += chr(toint)  
    return newword

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx