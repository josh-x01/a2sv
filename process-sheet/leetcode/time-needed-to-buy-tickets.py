class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue= deque()
        ans = 0
        for i in range(len(tickets)):
            ticket = tickets[i] - 1
            ans += 1
            if ticket == 0 and i == k:
                return ans
            if ticket > 0:
                queue.append([ticket, i])
        
        while queue:
            current_ticket = queue.popleft()
            current_ticket[0] -= 1
            ans += 1
            if current_ticket[0] == 0 and current_ticket[1] == k:
                return ans
            if current_ticket[0] > 0:
                queue.append(current_ticket) 

        
