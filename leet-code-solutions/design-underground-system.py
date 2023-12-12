class UndergroundSystem:

    def __init__(self):
        self.traveling = defaultdict(int)
        self.traveled = defaultdict(str)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.traveling[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if self.traveling[id][0] + "_" + stationName in self.traveled:
            self.traveled[self.traveling[id][0] + "_" + stationName].append(t - self.traveling[id][1])
        else:
            self.traveled[self.traveling[id][0] + "_" + stationName]= [t - self.traveling[id][1]]
        del self.traveling[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.traveled[startStation + "_" + endStation])/len(self.traveled[startStation + "_" + endStation])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)