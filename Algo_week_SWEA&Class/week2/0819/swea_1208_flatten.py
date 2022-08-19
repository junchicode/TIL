N = int(input())
boxes = list(map(int, input().split()))

while N > 0:
    maxidx = boxes.index(max(boxes))
    boxes[maxidx] = boxes[maxidx] - 1
    minidx = boxes.index(min(boxes))
    boxes[minidx] = boxes[minidx] + 1
    N = N - 1
print(max(boxes)-min(boxes))
    