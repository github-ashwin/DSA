class HashTable:
    def __init__(self):
        self.MAX = 100
        # self.arr = [None for i in range(self.MAX)] Instead of initializing value as None, initialize it as empty array []
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h =0 
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        # self.arr[h] = value
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key: # Checks if element is a tuple and if the key of the tuple is same as the hashkey
                self.arr[h][index] = (key,value)
                found = True
                break
        
        if not found:
            self.arr[h].append(key,value)

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index , element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

obj = HashTable()
temp = obj.get_hash('january 11')
# print(temp)
obj['day 1'] = 120
obj['day 2'] = 230
obj['day 3'] = 340
print(obj.arr)
print(obj['day 2'])
del obj['day 2']
print(obj.arr)