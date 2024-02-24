class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_counter = defaultdict(int)
        prefix_sum_counter[0] = 1
        total_subarray = current_sum = 0

        for num in nums:
            current_sum+=num
            difference = current_sum-goal
            if difference in prefix_sum_counter:
                total_subarray+=prefix_sum_counter[difference]
            prefix_sum_counter[current_sum]+=1
        return total_subarray