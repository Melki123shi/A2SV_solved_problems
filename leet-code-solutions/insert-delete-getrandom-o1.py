class RandomizedSet:

    def __init__(self):
        self.randomized_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            self.randomized_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randomized_set:
            self.randomized_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        lst = list(self.randomized_set)
        index = random.randint(0,len(lst) - 1)
        return lst[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()