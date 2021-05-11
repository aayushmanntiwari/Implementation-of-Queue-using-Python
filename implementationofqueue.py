class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,data):
        self.items.insert(0,data)
    
    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return True
        return False
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.items)
print(q.dequeue())
print(q.is_empty())
print(q.peek())
print(q.size())
