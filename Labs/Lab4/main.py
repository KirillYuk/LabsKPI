from queue import BiQueue

q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

print(q.peek('highest'))
print(q.peek('lowest'))
print(q.peek('oldest'))
print(q.peek('newest'))
print(q.queue)
