class RecentCounter:

    def __init__(self):
        self.queue = []
        self.size = 0
        self.pointer = 0
        
    def ping(self, t: int) -> int:
        interval = [t - 3000, t]
        self.queue.append(t)
        self.size += 1
        while self.pointer < self.size and self.queue[self.pointer] < interval[0]:
            self.pointer += 1
        return self.size - self.pointer

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)