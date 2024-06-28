class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = None
    
    def insert_begin(self, data):
        if self.head is None: # Linked list is empty
            self.head = Node(data, None, None)
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_end(self, data):
        if self.head is None: # If Linked list is empty
            self.head = Node(data, None, None) # The new node will be the head
            return
        
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = Node(data, None, itr)

    def get_length(self): # Getting the list of linked list
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next 

        return count
    
    def insert_at(self, data, index):
        if index < 0 or index > self.get_length(): # If Linked list is empty or invalid length
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_begin(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
        
    def print_forward(self): # From head to tail
        itr = self.head
        ll = ''
        while itr:
            ll += str(itr.data) + '-->'
            itr = itr.next

        print(ll)

    def get_last_node(self): # Getting the last node
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    def print_backwards(self): # From tail to head
        itr = self.get_last_node()
        ll = ''
        while itr:
            ll += str(itr.data) + '-->'
            itr = itr.prev

        print(ll)

    def remove_begin(self): # Removing from the head
        if self.head is None:
            raise Exception("List empty")
        
        if self.head.next is None:
            self.head = None
        
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def remove_end(self): # Removing from the tail
        if self.head is None:
            raise Exception("List empty")
        
        if self.head.next is None:
            self.head = None
        
        else:
            itr = self.get_last_node()
            itr.prev.next = None
        
    def remove_at(self, index): # Removing from sepcific index
        if index < 0 or index > self.get_length(): # If Linked list is empty or invalid length
            raise Exception("Invalid Index")
        
        if index == 0:
            self.remove_begin()
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1


# Testing the updated LinkedList class
obj = DLL()
obj.insert_begin(1)
obj.print_forward()
obj.insert_begin(2)
obj.print_forward()
obj.insert_end(3)
obj.print_forward()
obj.insert_at(4,2)
obj.print_forward()
obj.print_backwards()
obj.remove_begin()
obj.print_forward()
obj.remove_end()
obj.print_forward()
obj.insert_end(10)
obj.print_forward()
obj.remove_at(2)
obj.print_forward()