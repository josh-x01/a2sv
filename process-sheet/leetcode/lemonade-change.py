class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            coins[bill] += 1
            if bill == 10:
                if coins[5] != 0:
                    coins[5] -= 1
                else:
                    return False
            if bill == 20:
                if coins[10] != 0 and coins[5] != 0:
                    coins[10] -= 1
                    coins[5] -= 1
                else:
                    if coins[5] >= 3:
                        coins[5] -= 3
                    else:
                        return False
        return True
        