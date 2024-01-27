class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        m_c = 0
        n = len(piles)
        i = 1
        while i < 2 * (n // 3):
            m_c += piles[i]
            i += 2
        return m_c