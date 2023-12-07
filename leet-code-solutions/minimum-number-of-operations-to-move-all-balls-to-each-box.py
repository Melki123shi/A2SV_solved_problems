class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indexes = []
        for i,box in enumerate(boxes):
            if box == '1':
                indexes.append(i)
        result = []
        for i,box in enumerate(boxes):
            total = 0
            
            for ind in indexes:
                total += (abs(ind - i))
            result.append(total)
        return result
