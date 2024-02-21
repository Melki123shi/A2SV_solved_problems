class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        prefix_sum = 1
        result = [1]
        val = self.getRow(rowIndex - 1)
        for i in range(1, len(val)):
            prefix_sum += val[i] 
            result.append(prefix_sum)
            prefix_sum -= val[i - 1]
        result.append(1)
        return result

        