class ATM:

    def __init__(self):
        self.banknotes = [20, 50, 100, 200, 500]
        self.notes = {note: 0 for note in self.banknotes}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[self.banknotes[i]] += banknotesCount[i]
        
    def withdraw(self, amount: int) -> List[int]:
        withdrawed = [0 for _ in range(5)]
        notes_copy = self.notes.copy()

        i = 4
        while i > -1 and amount > 0:
            if self.banknotes[i] > amount:
                i -= 1
                continue

            if notes_copy[self.banknotes[i]] * self.banknotes[i] <= amount:
                amount -= notes_copy[self.banknotes[i]] * self.banknotes[i]
                withdrawed[i] += notes_copy[self.banknotes[i]]
                notes_copy[self.banknotes[i]] = 0

            else:
                div = amount // self.banknotes[i]
                amount -= div * self.banknotes[i]
                notes_copy[self.banknotes[i]] -= div
                withdrawed[i] = div
            i -= 1
        if amount == 0:
            self.notes = notes_copy
            return withdrawed
        return [-1]      


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)