class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        result = []

        p_array = [0]*26
        for i in p:
            p_array[ord(i)-97] += 1

        s_arr = [0]*26
        for k in s[0:len(p)]:
            s_arr[ord(k)-97] += 1 
        l = 0
        while l < (len(s)-len(p)):
            r = l + len(p)
            if p_array == s_arr:
                result.append(l)
            s_arr[ord(s[l]) - 97] -= 1
            s_arr[ord(s[r]) - 97] += 1
            l += 1
        if p_array == s_arr:
            result.append(l)

        return result

        