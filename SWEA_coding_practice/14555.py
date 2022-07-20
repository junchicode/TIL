T = int(input())

for i in range(T):
    cnt = 0
    tc = input()
    for j in range(1, len(tc)):
        if tc[j-1] == "|" and tc[j] == ")":
            cnt += 1
        elif tc[j-1] == "(" and tc[j] == "|":
            cnt += 1
        elif tc[j-1] == "(" and tc[j] == ")":
            cnt += 1
        else:
            pass
    print(f"#{i+1} {cnt}")