class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.flips = {index : 0 for index in range(size)}
        self.tracker = {0: size, 1 : 0}
        self.int_count = 0
 
    def fix(self, idx: int) -> None:
        if (self.flips[idx] + self.int_count) % 2 == 0:
            self.flips[idx] += 1
            self.tracker[0] -= 1
            self.tracker[1] += 1

    def unfix(self, idx: int) -> None:
        if (self.flips[idx] + self.int_count) % 2 != 0:
            self.flips[idx] += 1
            self.tracker[0] += 1
            self.tracker[1] -= 1

    def flip(self) -> None:
        self.int_count += 1
        temp = self.tracker[0]
        self.tracker[0] = self.tracker[1]
        self.tracker[1] = temp


    def all(self) -> bool:
        return self.tracker[1] == self.size

    def one(self) -> bool:
        return self.tracker[1] > 0

    def count(self) -> int:
        return self.tracker[1]

    def toString(self) -> str:
        string = ""
        for index in self.flips:
            string += str(int((self.flips[index] + self.int_count) % 2 != 0))
        return string

        
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()