class MyHashMap:

    def __init__(self):
        self.hashMap = dict()

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value
        return

    def get(self, key: int) -> int:
        print(key)
        print(self.hashMap)
        print(self.hashMap.get(key))
        if self.hashMap.get(key) is not None:
            print('dhuke')
            return self.hashMap[key]
        return -1

    def remove(self, key: int) -> None:
        if self.hashMap.get(key):
            self.hashMap.pop(key)

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,0)
param_2 = obj.get(1)
print(param_2)