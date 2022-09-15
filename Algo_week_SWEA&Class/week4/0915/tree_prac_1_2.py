# 3을 루트로 하는 서브트리에 속한 정점의 개수는?
def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0: # 부모가 없으면 
            return i

def preorder(n): # 전위
    global cnt
    if n:
        cnt += 1 #print(n, end = " ") # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n): # 중위
    if n:
        inorder(ch1[n])
        print(n,end = " ") # visit(n)
        inorder(ch2[n])

def postorder(n): # 후위
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end = " ") # visit(n)

root = 1 # 루트를 1이라 가정
V = int(input())
arr = list(map(int, input().split()))
E = V - 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
par = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c  # 첫번째 자식으로
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)
cnt = 0

preorder(3)
print(cnt)
'''print()
inorder(root)
print()
postorder(root)'''