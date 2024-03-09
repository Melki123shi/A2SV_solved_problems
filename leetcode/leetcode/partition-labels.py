class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = defaultdict(int)
        for i, st in enumerate(s):
            last_index[st] = i
        

        end_index = 0
        size = 0
        result = []
        for i in range(len(s)):
            end_index = max(end_index, last_index[s[i]])
            size += 1
            if i == end_index:
                result.append(size)
                size = 0
        return result

        
