class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            maxx = max(ceil(summ/(i + 1)), maxx)
        
        return maxx

