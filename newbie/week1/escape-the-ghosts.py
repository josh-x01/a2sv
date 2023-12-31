class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_cost = abs(target[0]) + abs(target[1])
        for g_x, g_y in ghosts:
            g_cost = abs(g_x - target[0]) + abs(g_y - target[1])
            if (g_cost <= my_cost):
                return False
        return True