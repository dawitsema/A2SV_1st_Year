class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.arr.append(val)
        self.map[val] = len(self.arr) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        idx = self.map[val]
        self.map[self.arr[-1]] = idx
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        self.arr.pop()
        self.map.pop(val)
        
        return True

    def getRandom(self) -> int:
        
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()