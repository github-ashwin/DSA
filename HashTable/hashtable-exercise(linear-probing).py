class HashTable:

    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [[] for _ in range(self.MAX_SIZE)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX_SIZE

    def get_proberange(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def __getitem__(self, key):
        h = self.get_hash(key)
        probe_range = self.get_proberange(h)
        for probe_index in probe_range:
            element = self.arr[probe_index]
            if not element:
                return None
            if element[0] == key:
                return element[1]
        return None

    def find_slot(self, key, index):
        probe_range = self.get_proberange(index)
        for probe_index in probe_range:
            if not self.arr[probe_index]:
                return probe_index
            if self.arr[probe_index][0] == key:
                return probe_index
        raise Exception("HashTable full!")

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if not self.arr[h]:
            self.arr[h] = (key, value)
        else:
            new_hash = self.find_slot(key, h)
            self.arr[new_hash] = (key, value)
        print(self.arr)

    def __delitem__(self, key):
        h = self.get_hash(key)
        probe_range = self.get_proberange(h)
        for probe_index in probe_range:
            if not self.arr[probe_index]:
                return
            if self.arr[probe_index][0] == key:
                self


hash_table = HashTable()


hash_table["name"] = "Alice"
hash_table["age"] = 30
hash_table["city"] = "New York"


print(hash_table["name"])  
print(hash_table["age"])   
print(hash_table["city"])  
print(hash_table["country"]) 


del hash_table["age"]


print(hash_table["age"])  