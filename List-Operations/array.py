class Array:

    def __init__(self):
        self.arr=[]

    
    def insert(self,index,value): # Inserts a new element with the given value at the specified index in the list.
        self.arr.insert(index,value)


    def remove(self,index): # Removes the element at the specified index from the list.
         self.arr.pop(index)


    def get(self,index): # Retrieves the value of the element at the specified index.
        return self.arr[index]
    

    def size(self): # Returns the number of elements currently in the list.
        return len(self.arr)
    
    
    def is_empty(self): # Checks if the list is empty (contains no elements).
        return self.size() == 0
    
    
    def append(self,value): # Adds a new element with the given value at the end of the list.
        self.arr.append(value)
        

    def prepend(self,value): # Adds a new element with the given value at the beginning of the list.
        self.arr.insert(0,value)
    

    def index_of(self,value): # Returns the index of the first occurrence of the given value in the list, or -1 if the value is not found.
        return self.arr.index(value)


    def contains(self, value): # Checks if the list contains the given value.
        return value in self.arr
    

    def clear(self): # Removes all elements from the list, making it empty.
        return self.arr.clear()


obj = Array()
obj.arr = [8,1,2,9,7]
obj.insert(5,3)
obj.remove(3)
obj.get(2)
obj.size()
obj.is_empty()
obj.append(1)
obj.prepend(0)
obj.index_of(1)
obj.contains(2)
obj.clear()
obj.size()