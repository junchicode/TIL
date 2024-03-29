'''
정점 번호 V = 1~(E+1)
간선 수 
부모-자식 순
4
1 2 1 3 3 4 3 5

for j in range(0, E*2, 2):
p, c = arr[j], arr[j+1]
'''
def preorder(n): # 전위
    if n:
        print(n) # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n): # 중위
    if n:
        inorder(ch1[n])
        print(n) # visit(n)
        inorder(ch2[n])

def postorder(n): # 후위
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n) # visit(n)

root = 1 # 루트를 1이라 가정
E = int(input())
arr = list(map(int, input().split()))
V = E + 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c  # 첫번째 자식으로
    else:
        ch2[p] = c
print(ch1)
print(ch2)
    
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()