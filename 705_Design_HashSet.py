class MyHashSet:

    def __init__(self):
        print('call init')
        self.dict = {}
    def __call__(self):
        print('call call')
    def add(self, key: int) -> None:
        self.dict.add(key)

    def remove(self, key: int) -> None:
        self.dict.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.dict else False

if __name__ == '__main__':
    myhash = MyHashSet()
    myhash.add(2)
