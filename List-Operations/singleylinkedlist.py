class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_begin(self, data):
        node = Node(data, self.head) # Adding node
        self.head = node # Pointing the new node as the head
    
    def print(self): # Utility function to check the progress
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        ll = ''
        while itr:
            ll += str(itr.data) + '-->'
            itr = itr.next
        print(ll)

    def insert_end(self, data):
        if self.head is None: # If Linked list is empty -> self.head will be None
            self.head = Node(data, None) # The new node will be the head
            return
        
        else:
            temp = self.head # Assigning head to temp
            while temp.next: # Finding the last node
                temp = temp.next 

            temp.next = Node(data, None) # Inserting at end
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)
        
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length(): # If Linked list is empty or invalid length
            raise Exception("Invalid Index")
        
        if index == 0: # If the index is 0, it is head node
            self.head = self.head.next # Removing the head node and pointing to next
            return
        
        count = 0
        itr = self.head
        while itr: # Iterating till it reaches the particular index
            if count == index - 1:
                itr.next = itr.next.next # Removing the particular node
                break
            itr = itr.next
            count += 1

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
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None: # Checks if the linked list is empty
            return
        
        if self.head.data == data_after: # If the node to be inserted is second node
            self.head.next = Node(data_to_insert,self.head.next)

        itr = self.head # Iterate
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
    
    def remove_by_value(self, data):
        if self.head is None: # Checks if the linked list is empty
            return

        if self.head.data == data:  # If the node to be removed is the head node.
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:  # Iterate through the list to find the node to remove.
            if itr.next.data == data:  # Found the node to be removed.
                itr.next = itr.next.next  # Remove the node by skipping it.
                return
            itr = itr.next


# Testing the updated LinkedList class
obj = LinkedList()
obj.insert_begin(1)
obj.insert_begin(111)
obj.print()  
obj.insert_end(777)
obj.print() 
print(obj.get_length())  
obj.remove_at(1)
obj.print()  
obj.insert_at(222, 1)
obj.print()  
obj.insert_after_value(222, 333)
obj.print()  
obj.insert_after_value(333, 555)
obj.print()  
obj.remove_by_value(555)
obj.print()  
obj.remove_by_value(333)
obj.print()  
obj.remove_by_value
