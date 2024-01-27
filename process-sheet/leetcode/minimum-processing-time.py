class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        max_=1
        for i in range(1,len(processorTime)+1):
            exec_ = tasks[(i*4)-1]+processorTime[i-1]
            max_ = max(max_,exec_)
        return max_