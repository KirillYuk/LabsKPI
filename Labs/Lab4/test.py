from queue import BiQueue

print("TESTS")


q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

if q.dequeue('highest') == "A":
    print("dequeue highest: PASS")
else:
    print("dequeue highest: FAIL")

if q.dequeue('lowest') == "B":
    print("dequeue lowest: PASS")
else:
    print("dequeue lowest: FAIL")


q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

if q.dequeue('oldest') == "A":
    print("dequeue oldest: PASS")
else:
    print("dequeue oldest: FAIL")

if q.dequeue('newest') == "C":
    print("dequeue newest: PASS")
else:
    print("dequeue newest: FAIL")


q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

if q.peek('highest') == "A" and len(q.queue) == 3:
    print("peek highest: PASS")
else:
    print("peek highest: FAIL")

if q.peek('lowest') == "B" and len(q.queue) == 3:
    print("peek lowest: PASS")
else:
    print("peek lowest: FAIL")


q = BiQueue()
if q.dequeue('highest') is None:
    print("empty queue: PASS")
else:
    print("empty queue: FAIL")