class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {5 : 0, 10 : 0, 20 : 0}
        for bill in bills:
            if bill == 20:
                if notes[5] < 1:
                    return False

                if notes[5] < 3 and notes[10] < 1:
                    return False

                if notes[5] > 0 and notes[10] > 0:
                    notes[5] -= 1
                    notes[10] -= 1
                else:
                    notes[5] -= 3
                notes[20] += 1


            elif bill == 10:
                if notes[5] < 1:
                    return False
                
                notes[5] -= 1
                notes[10] += 1
            else:
                notes[5] += 1
        return True
                