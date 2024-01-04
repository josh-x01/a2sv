class ATM:
    def __init__(self):
        self.notes = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}
        self.notes_amount = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes_amount[i] += banknotesCount[i]
        # print("deposit:", self.notes_amount)
        # print(self.notes_amount)
        # return self.notes_amount

    def withdraw(self, amount: int) -> List[int]:
        result = [0, 0, 0, 0, 0]
        temp_notes = self.notes_amount.copy()
        for i in range(len(self.notes_amount) - 1, -1, -1):
            if temp_notes[i] > 0 and self.notes[i] <= amount:
                count = amount // self.notes[i]
                if count <= temp_notes[i]:
                    amount = amount % self.notes[i]
                    temp_notes[i] -= count
                    result[i] = count
                else:
                    amount -= temp_notes[i] * self.notes[i]
                    result[i] = temp_notes[i]
                    temp_notes[i] = 0

        if amount > 0:
            # print(self.notes_amount)
            return [-1]
        else:
            self.notes_amount = temp_notes
            # print(self.notes_amount)
            return result



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
