from queue import BiQueue

q = BiQueue()
q.enqueue("task A", 5)
q.enqueue("task B", 1)
q.enqueue("task C", 3)
q.enqueue("task D", 4)

print("peek")
print(q.peek('highest'))
print(q.peek('lowest'))
print(q.peek('oldest'))
print(q.peek('newest'))

print("\ndequeue")
print(q.dequeue('highest'))
print(q.dequeue('lowest'))
print(q.dequeue('oldest'))
print(q.dequeue('newest'))

print("\nempty queue")
print(q.dequeue('highest'))