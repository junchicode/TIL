# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
from calendar import c


def get_final_position(N, mat, moves):
    pass
    size = len(mat)
    movec = [-1, 1, 0, 0]
    mover = [0, 0, -1, 1]
    current = [0,0]
    for i in moves:
        current[0] += movec[i]
        current[1] += mover[i]
    for i in range(len(current)):
        if 0<=current[0]<size and 0<=current[1]<size:
            return current
        else:
            return None

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]