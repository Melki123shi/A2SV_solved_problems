class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0
        ks = k
        for a in 'TF':
            l = 0
            k = ks
            for r in range(len(answerKey)):
                while answerKey[r] != a and k <= 0:
                    while l < r and answerKey[l] == a:
                        l += 1
                    l += 1
                    k += 1
                if answerKey[r] != a and k > 0:
                    k -= 1
                res = max(res, r - l + 1)

                
        return res