class Solution:
    def smallestNumber(self, num: int) -> int:
        neg = False
        if num < 0:
            num = abs(num)
            neg = True
        num = [x for x in str(num)]
        num.sort()
        if neg:
            num = num[::-1]
        # print(num)
        i = 0
        zeros = 0
        while i < len(num) - 1:
            if num[i] != '0':
                break
            zeros += 1
            i += 1
        num[i], num[i - zeros] = num[i - zeros], num[i]
        # print(zeros)
        num = int(''.join(num))
        if neg: 
            return -1 * num
        return num