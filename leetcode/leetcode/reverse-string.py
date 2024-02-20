class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        def reverse(s, ind = 0):
            if ind == ceil(n / 2 ):
                return 
            
            s[ind], s[n - ind ] = s[n - ind], s[ind]
            reverse(s, ind + 1)

        reverse(s)