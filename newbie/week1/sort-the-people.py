class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        len_ = len(names)
        for broker in range(1, len_):
            for worker in range(broker, 0, -1):
                if heights[worker] >= heights[worker-1]:
                    break
                temp_t = heights[worker]
                heights[worker] = heights[worker-1]
                heights[worker-1] = temp_t
                temp_n = names[worker]
                names[worker] = names[worker-1]
                names[worker-1] = temp_n
        return names[::-1]

