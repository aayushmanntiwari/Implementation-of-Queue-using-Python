class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return True
        return False

class Jobs:
    def __init__(self,pages):
        self.pages = pages
    
    def printing_pages(self):
        while self.pages > 0:
            print(self.pages)
            self.pages-=1

    def completed(self):
        if self.pages == 0:
            print('Completed')


class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self,queue):
        if not queue.is_empty():
            self.current_job = queue.dequeue()

    def print_job(self):
        self.current_job.printing_pages()
        self.current_job.completed()
        
        


job = Jobs(10)
queue = Queue()
print_job = Printer()
queue.enqueue(job)
print(queue.items)
print_job.get_job(queue)
print(print_job.current_job)
print_job.print_job()


