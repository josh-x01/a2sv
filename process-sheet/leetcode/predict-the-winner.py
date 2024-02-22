class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def predict(start,end,player1):
            if end-start<0:
                return 0
            if player1:
                return max(nums[start]+predict(start+1,end,False),nums[end]+predict(start,end-1,False))
            else:
                return min(predict(start+1,end,True),predict(start,end-1,True))
        numsl=len(nums)
        numsSum=sum(nums)
        player1Score=predict(0,numsl-1,True)
        return player1Score>=(numsSum-player1Score)