"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. 
             This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
             
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
             This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
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

obj = Queue()  

def place_order(orders):
    for item in orders:
        print("Placing order for:",item)
        obj.enqueue(item)
        time.sleep(0.5)

def server_order():
    time.sleep(1)
    while True:
        if not obj.is_empty():
            order = obj.dequeue()
            if order is not None:
                print("Serving order:", order)
            time.sleep(2)
        else:
            break   

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order,args=(orders,))
    t2 = threading.Thread(target=server_order)

    t1.start()
    t2.start()