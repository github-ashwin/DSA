class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h =0 
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    

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