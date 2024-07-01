class HashTable:

    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [[] in range(self.MAX_SIZE)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX_SIZE
    
    def get_proberange(self,index):
        return [*range(index,len(self.arr))] + [*range(0,index)]
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        
        probe_range = self.get_proberange(h)
        