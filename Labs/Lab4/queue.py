class BiQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
    
    def enqueue(self, item, priority):
        self.queue.append((self.counter, priority,item))
        self.counter +=1

    def dequeue(self, mode):
        if mode == 'highest':
            item = max(self.queue, key=lambda x: x[1])
        elif mode == 'lowest':
            item = min(self.queue, key=lambda x: x[1])
        elif mode == 'oldest':
            item = min(self.queue, key=lambda x: x[0])
        elif mode == 'newest':
            item = max(self.queue, key=lambda x: x[0])

        self.queue.remove(item)
        return item[2]

    def peek(self, mode):
        if mode == 'highest':
            item = max(self.queue, key=lambda x: x[1])
        elif mode == 'lowest':
            item = min(self.queue, key=lambda x: x[1])
        elif mode == 'oldest':
            item = min(self.queue, key=lambda x: x[0])
        elif mode == 'newest':
            item = max(self.queue, key=lambda x: x[0])

        return item[2]