class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(tasks)
        m = len(processorTime)
        tasks.sort()
        processorTime.sort(reverse=True)
        maxx = 0
        for i in range(m):
            begin = i*n//m
            end = (i+1)*n//m
            temp = max(tasks[begin:end]) + processorTime[i]
            maxx = max(temp, maxx)

        return maxx
        
        