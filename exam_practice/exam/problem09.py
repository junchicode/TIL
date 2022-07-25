# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
# M = position
# N = 배열
    #arr = [list(N*"*") for _ in range(N)]
    movec = [-1, 1, 0, 0]
    mover = [0, 0, -1, 1]
    current = list(position)
    movedc = current[0] + movec[M]
    movedr = current[1] + mover[M]
    
    if 0<=movedc<N and 0<=movedr<N:
        return True
    else:
        return False
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
