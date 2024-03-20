class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        value = self.timeMap[key]
        if not value:
            return ''

        if timestamp >= value[-1][1]:
            return value[-1][0]

        if timestamp < value[0][1]:
            return ''

        low = 0
        high = len(value)
        while low  + 1 <= high:
            mid = low + (high - low)//2
            if value[mid][1] == timestamp or (value[mid - 1][1] < timestamp and value[mid][1] > timestamp):
                return value[mid - 1][0]

            if value[mid][1] < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        return value[high][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)