import sys
input = sys.stdin.readline
cum = 0
a = input().rstrip()
for i in a:
    cum += int(i)
    
print(cum)