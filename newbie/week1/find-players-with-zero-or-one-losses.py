class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossers = defaultdict(int)
        for winner, losser in matches:
            if winner not in lossers.keys():
                lossers[winner] = 0
            lossers[losser] += 1         
        always_winners = [losser for losser, count in lossers.items() if count == 0]
        only_loss_once = [losser for losser, count in lossers.items() if count == 1]
        always_winners.sort()
        only_loss_once.sort()
        return [always_winners, only_loss_once]