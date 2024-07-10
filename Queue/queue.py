from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,value): # Insert function
        self.queue.appendleft(value)
    
    def dequeue(self): # Delete function
        return self.queue.pop()
    
    def is_empty(self): # Checking if queue is empty or not
        return len(self.queue)==0
    
    def length(self): # Finds the length of queue
        return len(self.queue)
    
obj = Queue()

if __name__ =='__main__':
    obj.enqueue(100)
    obj.enqueue(101)
    obj.enqueue(110)
    obj.enqueue(111)
    print(obj.queue)
    print(obj.dequeue())
    print(obj.length())
    print(obj.dequeue())
    print(obj.length())