class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        monday = 0

        for counter in range(n):
            if counter % 7 == 0:
                monday += 1
                money = monday
            else:
                money += 1

            total_money += money
        return total_money
        