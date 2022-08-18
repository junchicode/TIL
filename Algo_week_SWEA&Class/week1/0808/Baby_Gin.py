'''
설명
- 0~9 까지의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라고 하고, 3장의 카드가 동일한 번호를 갖는 경우를
triplet이라고 한다
- 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin이라고 부른다
- 6자리의 숫자를 입력받아 baby-gin여부를 판단하는 프로그램을 작성하시오'''

num = 456789
c = [0]*12 # -> 뒤에 두개는 더미

for i in range(6):
    c[num % 10] += 1 # 이거로 1의 자리 숫자를 표현할 수 있음
    num //= 10

'''
# 수가 정해지지 않았을 경우
while num > 0
    c(num%10) += 1
    num //= 10
'''
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2 : print("Baby Gin")
else:
    print("Lose")