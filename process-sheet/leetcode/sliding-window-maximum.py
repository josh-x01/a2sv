class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = deque()
        start = 0
        result = []
        for i in range(k):
            while max_queue and max_queue[-1] < nums[i]:
                max_queue.pop()
            max_queue.append(nums[i])
        result.append(max_queue[0])

        for end in range(k, len(nums)):
            # add the max queue
            while max_queue and max_queue[-1] < nums[end]:
                max_queue.pop()
            max_queue.append(nums[end])
            # print(max_queue, nums[start])
            num = nums[start]
            if max_queue[0] == num:
                max_queue.popleft()
            start += 1
            result.append(max_queue[0])
        return result

