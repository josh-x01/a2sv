class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_dict = Counter(nums)
        min_freq = len(nums)//3
        valid_nums = set()
        for num, count in count_dict.items():
            if count > min_freq:
                valid_nums.add(num)
        return list(valid_nums)
                
            
        
        