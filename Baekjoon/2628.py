from hashlib import new


width, length = map(int, input().split())
numbers = int(input())
cut_list = []
for _ in range(numbers):
    cut_list.append(list(map(int, input().split())))

new_len = [0, length]
new_w = [0, width]
for i in range(numbers):
    if cut_list[i][0] == 0:
        new_len.append(cut_list[i][1])
    else:
        new_w.append(cut_list[i][1])
        
snew_len = sorted(new_len)
snew_w = sorted(new_w)

final_len = []
final_w = []
 
for sl in range(len(snew_len)-1):
    final_len.append(snew_len[sl+1] - snew_len[sl])
    
    
for sw in range(len(snew_w)-1):
    final_w.append(snew_w[sw+1] - snew_w[sw])

print(final_len, final_w)
print(max(final_len)*max(final_w))
    

    
        
    