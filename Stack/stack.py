from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self,value): # Insertion
        self.stack.append(value)

    def pop(self): # Deletion
        return self.stack.pop()

    def peek(self): # Just viewing the last element
        return self.stack[-1]
    
    def is_empty(self): # Checking if stack is empty or not
        return len(self.stack)==0
    
    def length(self): # Checking the length of the stack
        return len(self.stack)

def rev_string(str):

    obj = Stack()

    for ch in str:
        obj.push(ch)

    reverse_string = ''

    while obj.is_empty() is not True:
        reverse_string += obj.pop()

    return reverse_string

if __name__ == '__main__':
    print(rev_string("We will conquere COVID-19"))

