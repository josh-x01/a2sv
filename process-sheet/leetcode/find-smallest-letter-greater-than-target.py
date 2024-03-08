class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        nums = [ord(i) for i in letters]
        print(nums, ord(target))
        ans = bisect_right(nums, ord(target))
        if ans >= len(nums):
            return letters[0]
        # print(ans, chr(nums[ans]))
        return chr(nums[ans])