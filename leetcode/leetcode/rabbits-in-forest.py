class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabits = Counter(answers)
        result = 0
        for key in rabits:
            if key == 0:
                result += rabits[key]

            elif key + 1 > rabits[key]:
                result += key + 1
                
            else:
                result += ceil((rabits[key])/(key + 1)) * (key + 1)  
        
        return result




            
        