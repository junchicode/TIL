N = 10
q = [0]*N
front = -1
rear = -1

rear += 1       #enq(10)
q[rear] = 10

rear +=1
q[rear] = 20

rear += 1 
q[rear] = 30

front += 1       #deq
print(q[front])

front += 1
print(q[front])

front += 1
print(q[front])