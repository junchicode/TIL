from queue import PriorityQueue

q = PriorityQueue()

q.put(4)
q.put(3)
q.put(5)
q.put(1)

print(q.get())
print(q.get())
print(q.get())
print(q.get())