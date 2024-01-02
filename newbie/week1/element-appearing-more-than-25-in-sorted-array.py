class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        rep_counter = defaultdict(int)
        req_freq = math.ceil(len(arr) * 0.25)
        for num in arr:
            rep_counter[num] += 1
        max_num = float('-inf')
        max_count = float('-inf')
        for num, count in rep_counter.items():
            if count >= req_freq:
                if count > max_count:
                    max_num = num
                    max_count = count
        return max_num
