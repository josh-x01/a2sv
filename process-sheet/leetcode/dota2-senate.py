class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque()
        r_size = 0
        d_size = 0
        del_d = 0
        del_r = 0
        for sen in senate:
            if sen == 'R':
                r_size += 1
            else:
                d_size += 1
            queue.append(sen)
        
        while d_size != 0 and r_size != 0:
            # print('here')
            current = queue.popleft()
            if current == "R":
                if del_r == 0:
                    del_d += 1
                    d_size -= 1
                    queue.append(current)
                else:
                    del_r -= 1
                
            if current == 'D':
                if del_d == 0:
                    del_r += 1
                    r_size -= 1
                    queue.append(current)
                else:
                    del_d -= 1
        # print(r_size, d_size)
        if r_size != 0:
            return "Radiant"
        else:
            return "Dire"