class HashTable:
    def __init__(self, sizes=7):
        self.data = [None] * sizes

    def _hash(self,keys):
        hash = 0
        for letters in keys:
            hash = (hash + ord(letters) * 23) % len(self.data)
        return hash

    def printtable (self):
        for i,val in enumerate(self.data):
            print(i, ":", val)

    def selfitems(self,key,values):
        index = self._hash(key)
        if self.data[index] == None:
            self.data[index] = []
        self.data[index].append([key,values])

    def getitem(self,key):
        indexes = self._hash(key)
        if self.data[indexes] is not  None:
            for i in range(len(self.data[indexes])):
                if self.data[indexes] [i][0] == key:
                    return self.data[indexes][i][1]
        return None



myhash = HashTable()
myhash.selfitems('bolt',100)
myhash.selfitems('nuts',222)
print(myhash.getitem('bolt'))
print(myhash.getitem('nuts'))
print(myhash.getitem('washers'))

