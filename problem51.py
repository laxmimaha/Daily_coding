class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        self.instack=Stack()
        self.outstack=Stack()
        
    def enqueue(self,item):
        self.instack.push(item)
        
    def dequeue(self):
        if not self.outstack.items:
            while self.instack.items:
                self.outstack.push(self.instack.pop())
        return self.outstack.pop()
    
        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())


