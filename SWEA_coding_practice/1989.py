n = int(input())
res = []
for i in range(n):
    word = input()
    if word == word[::-1]:
        res.append('#%i '%(i+1) + "1")
    else:
        res.append('#%i '%(i+1) + "0")

for j in res:
    print(j)
