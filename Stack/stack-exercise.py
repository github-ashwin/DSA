"""
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]"
"""

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



def match(char1,char2):

    check= {
        ')':'(',
        '}':'{',
        ']':'['
    }

    return check[char1] == char2



def check_balance(str):

    stack = Stack()

    for ch in str:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        
        if ch == ')' or ch == '}' or ch == ']':
            if stack.length() == 0:
                return False
            
            if not match(ch,stack.pop()):
                return False
    
    return stack.length() == 0

if __name__ == '__main__':
    print(check_balance("({a+b})"))
    print(check_balance("))"))

