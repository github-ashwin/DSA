"""
Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
"""

from collections import deque
import time,threading


class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self,value):
        self.queue.appendleft(value)
    
    def dequeue(self):
        return self.queue.pop()
    
    def is_empty(self):
        return len(self.queue)==0
    
    def length(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[-1]

def pattern(limit):

    obj = Queue()
    obj.enqueue("1")

    for i in range(limit):
        num = obj.front()
        print(num)
        obj.enqueue(num + "0")
        obj.enqueue(num + "1")

        obj.dequeue()


if __name__ == '__main__':
    pattern(10)

