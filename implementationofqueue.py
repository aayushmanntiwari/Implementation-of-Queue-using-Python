class Queue:
    def __init__(self,items):
        self.items = items
    
    def enqueue(self):
        self.items.insert(0,0)
    
    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items is None:
            return True
        return False
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

q = Queue([1,2,3,4])
q.enqueue()
print(q.items)
print(q.dequeue())
print(q.is_empty())
print(q.peek())
print(q.size())