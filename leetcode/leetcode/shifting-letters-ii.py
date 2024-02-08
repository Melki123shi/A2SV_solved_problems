class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)
        shifted_str = ''

        # use prefix sum to store the current update of a character in the string
        for start, end, step in shifts:
            if step == 0:
               prefix_sum[start] -= 1
               prefix_sum[end + 1] += 1
            else:
                prefix_sum[start] += 1
                prefix_sum[end + 1] -= 1

        for ind in range(1, len(prefix_sum)):
            prefix_sum[ind] += prefix_sum[ind - 1]
            
        # Iterate through the prefix_sum to update the characters in the string
        for i in range(len(prefix_sum) - 1):
            prefix_sum[i] %= 26
            if prefix_sum[i] < 0:
                prefix_sum[i] = 26 + prefix_sum[i]
            shifted_str += chr(((ord(s[i]) - 97 + prefix_sum[i]) % 26) + 97)
        
        return shifted_str

        