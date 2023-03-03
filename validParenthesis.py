class Solution:
    def isValid(self, s: str) -> bool:
        open = ("(","[","{")
        close = (")","]","}")
        stack = []
        for ele in s:
            if ele in open:
                stack.append(ele)
            if ele in close:
                if len(stack)==0:
                    return False
                elif stack[-1]==open[close.index(ele)]:
        
                    stack.pop()
                else:
                    return False
               

        if len(stack)==0:  
            return True
        return False     
