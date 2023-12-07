class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        _set = set()
        for _range in ranges:
            for x in range(_range[0], _range[1]+1):
                _set.add(x)
        print(_set)
        for j in range(left, right + 1):
            if j not in _set:
                return False
        return True