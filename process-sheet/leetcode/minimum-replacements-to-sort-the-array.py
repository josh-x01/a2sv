class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        prev_number = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < prev_number:
                prev_number = nums[i]
                continue
            number_of_elements = ceil(nums[i] / prev_number)
            ans +=  number_of_elements - 1
            print(number_of_elements)
            prev_number = nums[i] // number_of_elements
        return ans
