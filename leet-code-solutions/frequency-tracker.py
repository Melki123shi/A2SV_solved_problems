class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.tracker = {}

    def add(self, number: int) -> None:
        if number not in self.freq:
            self.freq[number] = 1    
        else:
            self.tracker[self.freq[number]] -= 1
            if self.tracker[self.freq[number]]  == 0:
                del self.tracker[self.freq[number]] 
            self.freq[number] += 1
        if self.freq[number] not in self.tracker:
            self.tracker[self.freq[number]] = 1
        else:
            self.tracker[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            if self.freq[number] == 1:
                if 1 in self.tracker:
                    self.tracker[1] -= 1
                    if self.tracker[1] == 0:
                        del self.tracker[1]
                del self.freq[number]
            else:
                self.tracker[self.freq[number]] -= 1
                if self.tracker[self.freq[number]] == 0:
                    del self.tracker[self.freq[number]]
                self.freq[number] -= 1 
            if number in self.freq:
                if self.freq[number] not in self.tracker:
                    self.tracker[self.freq[number]] = 1
                else:
                    self.tracker[self.freq[number]] += 1
               
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.tracker


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)