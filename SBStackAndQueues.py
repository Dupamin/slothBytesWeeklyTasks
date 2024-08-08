class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
        
    def front(self):
        return self.items[0]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    
class MyStack:   
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        
    def push(self, item):
        self.q2.enqueue(item)
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        if not self.q2.isEmpty():
            deq = self.q2.dequeue()
        while not self.q2.isEmpty():
            self.q1.enqueue(self.q2.dequeue())
        return deq
    
    def top(self):
        while not self.q1.isEmpty():
            self.q2.enqueue(self.q1.dequeue())
        if not self.q2.isEmpty():
            front = self.q2.front()
        while not self.q2.isEmpty():
            self.q1.enqueue(self.q2.dequeue())
        return front
    
    def isEmpty(self):
        return self.q1.isEmpty()
    

myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top()
myStack.pop()
myStack.isEmpty()

print(myStack.q1.items)