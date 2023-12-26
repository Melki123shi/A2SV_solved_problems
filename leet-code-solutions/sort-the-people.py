class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i, height in enumerate(heights):
            dic[height] = names[i]
        
        heights.sort(reverse=True)
        return [dic[h] for h in heights]

        
