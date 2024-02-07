class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        checked = set()
        min_len = float('inf')
        for r in range(len(cards)):
            if cards[r] not in checked:
                checked.add(cards[r])
                continue
            while cards[l] != cards[r] and l != r:
                checked.remove(cards[l])
                l += 1
            min_len = min(min_len, len(cards[l:r]) + 1)
            l += 1
        if min_len == float('inf'):
            return -1
        return min_len